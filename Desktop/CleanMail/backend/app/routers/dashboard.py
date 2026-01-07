"""
Dashboard router - Statistics and overview
"""

from fastapi import APIRouter, Depends, Header, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import func

from app.database import get_db
from app.models.rule import Rule
from app.models.email_log import EmailLog
from app.services.auth_service import verify_token

router = APIRouter()

def get_current_user(authorization: str = Header(None)):
    """Get current user from JWT token"""
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Invalid authentication")
    token = authorization.split(" ")[1]
    user_id = verify_token(token)
    return int(user_id)


@router.get("/stats")
async def get_dashboard_stats(
    current_user_id: int = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Get dashboard statistics for professional email management"""

    # Count active rules
    rules_count = db.query(Rule).filter(Rule.user_id == current_user_id, Rule.is_active == True).count()

    # Count processed emails today
    from datetime import datetime, timedelta
    today = datetime.utcnow().date()
    processed_today = db.query(EmailLog).filter(
        EmailLog.user_id == current_user_id,
        func.date(EmailLog.processed_at) == today
    ).count()

    # Get recent activity (last 10 processed emails)
    recent_activity = db.query(EmailLog).filter(
        EmailLog.user_id == current_user_id
    ).order_by(EmailLog.processed_at.desc()).limit(10).all()

    # Get bill-related emails (professional focus)
    bills_count = db.query(EmailLog).filter(
        EmailLog.user_id == current_user_id,
        EmailLog.applied_action == "tag",
        EmailLog.action_value == "Bills"
    ).count()

    # Get category breakdown
    category_stats = db.query(
        EmailLog.action_value,
        func.count(EmailLog.id).label("count")
    ).filter(
        EmailLog.user_id == current_user_id,
        EmailLog.applied_action == "tag"
    ).group_by(EmailLog.action_value).all()

    # Get rule performance
    rule_performance = db.query(
        Rule.name,
        func.count(EmailLog.id).label("processed_count")
    ).join(EmailLog, Rule.id == EmailLog.rule_id).filter(
        Rule.user_id == current_user_id
    ).group_by(Rule.id, Rule.name).all()

    return {
        "total_rules": rules_count,
        "processed_today": processed_today,
        "bills_tracked": bills_count,
        "category_breakdown": [
            {"category": stat.action_value, "count": stat.count}
            for stat in category_stats
        ],
        "recent_activity": [
            {
                "id": log.id,
                "subject": log.subject,
                "action": log.applied_action,
                "category": log.action_value,
                "success": log.success,
                "processed_at": log.processed_at
            }
            for log in recent_activity
        ],
        "rule_performance": [
            {"rule_name": perf.name, "processed_count": perf.processed_count}
            for perf in rule_performance
        ]
    }


@router.get("/activity")
async def get_activity_log(
    current_user_id: int = Depends(get_current_user),
    limit: int = 50,
    offset: int = 0,
    db: Session = Depends(get_db)
):
    """Get activity log"""
    logs = db.query(EmailLog).filter(
        EmailLog.user_id == current_user_id
    ).order_by(EmailLog.processed_at.desc()).offset(offset).limit(limit).all()

    return {
        "logs": [
            {
                "id": log.id,
                "subject": log.subject,
                "sender": log.sender,
                "action": log.applied_action,
                "success": log.success,
                "processed_at": log.processed_at
            }
            for log in logs
        ],
        "total": len(logs)
    }
