"""
Emails router - Email processing and Gmail API integration
"""

from typing import List, Dict, Any
from fastapi import APIRouter, Depends, HTTPException, BackgroundTasks, Header
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.user import User
from app.models.rule import Rule
from app.schemas.email_log import EmailLogCreate
from app.services import gmail_service, rule_engine
from app.services.auth_service import verify_token

router = APIRouter()

def get_current_user(authorization: str = Header(None)):
    """Get current user from JWT token"""
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Invalid authentication")
    token = authorization.split(" ")[1]
    user_id = verify_token(token)
    return int(user_id)


@router.get("/preview")
async def preview_emails(
    current_user_id: int = Depends(get_current_user),
    max_results: int = 10,
    db: Session = Depends(get_db)
):
    """Preview emails from user's Gmail inbox"""
    user = db.query(User).filter(User.id == current_user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    try:
        emails = gmail_service.get_emails(user, max_results=max_results)
        return {"emails": emails}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to fetch emails: {str(e)}")


@router.post("/process")
async def process_emails(
    background_tasks: BackgroundTasks,
    current_user_id: int = Depends(get_current_user),
    max_emails: int = 50,
    db: Session = Depends(get_db)
):
    """Process emails using user's rules"""
    user = db.query(User).filter(User.id == current_user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # Add background task for processing
    background_tasks.add_task(process_emails_background, current_user_id, max_emails, db)

    return {"message": "Email processing started in background"}


async def process_emails_background(user_id: int, max_emails: int, db: Session):
    """Background task to process emails"""
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        return

    try:
        # Get user's rules (use built-in rules if no custom rules)
        rules = db.query(Rule).filter(Rule.user_id == user_id, Rule.is_active == True).all()
        if not rules:
            # Use built-in rules if no custom rules exist
            from app.services.rule_engine import get_built_in_rules
            built_in_rules = get_built_in_rules()
            for rule_data in built_in_rules:
                rule = Rule(
                    user_id=user_id,
                    name=rule_data["name"],
                    description=rule_data["description"],
                    match_type=rule_data["match_type"],
                    match_value=rule_data["match_value"],
                    action_type=rule_data["action_type"],
                    action_value=rule_data["action_value"],
                    priority=rule_data["priority"],
                    is_active=True
                )
                db.add(rule)
            db.commit()
            rules = db.query(Rule).filter(Rule.user_id == user_id, Rule.is_active == True).all()

        # Get emails to process
        emails = gmail_service.get_emails(user, max_results=max_emails)

        # Process each email
        for email in emails:
            matched_rule = rule_engine.find_matching_rule(email, rules)

            if matched_rule:
                # Apply the rule
                success = gmail_service.apply_rule(user, email, matched_rule)

                # Log the action
                log_data = EmailLogCreate(
                    user_id=user_id,
                    rule_id=matched_rule.id,
                    gmail_message_id=email["id"],
                    subject=email.get("subject"),
                    sender=email.get("sender"),
                    received_at=email.get("received_at"),
                    applied_action=matched_rule.action_type,
                    action_value=matched_rule.action_value,
                    success=success
                )

                # Save log to database
                from app.models.email_log import EmailLog
                log_entry = EmailLog(**log_data.model_dump())
                db.add(log_entry)
                db.commit()

    except Exception as e:
        # TODO: Log error
        print(f"Error processing emails: {e}")


@router.get("/patterns")
async def get_built_in_patterns():
    """Get built-in email patterns for Spanish/English professional filtering"""
    patterns = {
        # Professional Categories for Bills Tracking
        "bills": {
            "name": "Bills & Invoices",
            "description": "Facturas, recibos, y documentos de pago",
            "match_type": "subject",
            "match_value": "factura|invoice|recibo|billing|comprobante|pdf",
            "action_type": "tag",
            "action_value": "Bills"
        },
        "orders": {
            "name": "Orders & Shipping",
            "description": "Pedidos y notificaciones de envío",
            "match_type": "subject",
            "match_value": "pedido|order|enviado|shipped|entregado|delivered",
            "action_type": "tag",
            "action_value": "Orders"
        },
        # Trash/Publy Categories
        "trash": {
            "name": "Trash & Promotions",
            "description": "Promociones, ofertas y correos no deseados",
            "match_type": "subject",
            "match_value": "oferta|promo|descuento|newsletter|boletín",
            "action_type": "tag",
            "action_value": "Trash"
        },
        "noreply": {
            "name": "No Reply & Automated",
            "description": "Correos automáticos y sin respuesta",
            "match_type": "sender",
            "match_value": "noreply|no-reply|sin-respuesta",
            "action_type": "tag",
            "action_value": "Trash"
        },
        # Social Media
        "social": {
            "name": "Social Media",
            "description": "Notificaciones de redes sociales",
            "match_type": "sender",
            "match_value": "facebook|instagram|twitter|linkedin",
            "action_type": "tag",
            "action_value": "Social"
        },
        # Technical/Deployment
        "technical": {
            "name": "Technical & Deployment",
            "description": "Notificaciones técnicas y de despliegue",
            "match_type": "subject",
            "match_value": "deploy|deployment|despliegue|build|alert|alerta",
            "action_type": "tag",
            "action_value": "Technical"
        }
    }
    return {"patterns": patterns}
