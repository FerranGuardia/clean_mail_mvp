"""
Rule engine - Match emails against rules and determine actions
"""

import re
from typing import Dict, Any, Optional
from app.models.rule import Rule


def find_matching_rule(email: Dict[str, Any], rules: list[Rule]) -> Optional[Rule]:
    """
    Find the first matching rule for an email
    Rules are evaluated in priority order (lower priority number = higher priority)
    """
    # Sort rules by priority (ascending)
    sorted_rules = sorted(rules, key=lambda r: r.priority)

    for rule in sorted_rules:
        if matches_rule(email, rule):
            return rule

    return None


def matches_rule(email: Dict[str, Any], rule: Rule) -> bool:
    """Check if an email matches a specific rule"""
    match_target = get_match_target(email, rule.match_type)
    if not match_target:
        return False

    if rule.match_type == "regex":
        try:
            return bool(re.search(rule.match_value, match_target, re.IGNORECASE))
        except re.error:
            return False
    else:
        # Simple substring match (case insensitive)
        return rule.match_value.lower() in match_target.lower()


def get_match_target(email: Dict[str, Any], match_type: str) -> str:
    """Get the target string to match against based on match type"""
    if match_type == "sender":
        return email.get("sender", "")
    elif match_type == "subject":
        return email.get("subject", "")
    elif match_type == "body":
        return email.get("body_preview", "")
    elif match_type == "header":
        # For header matching, we'd need to check all headers
        # For now, just check common headers
        headers_to_check = [
            email.get("sender", ""),
            email.get("to", ""),
            email.get("subject", "")
        ]
        return " ".join(headers_to_check)
    elif match_type == "regex":
        # For regex, we can match against combined content
        return f"{email.get('sender', '')} {email.get('subject', '')} {email.get('body_preview', '')}"
    else:
        return ""


def get_built_in_rules() -> list[Dict[str, Any]]:
    """Get built-in rules for Spanish and English email patterns"""
    return [
        # === TRASH/PUBLY EMAILS ===
        {
            "name": "No Reply Emails",
            "description": "Tag emails from noreply addresses (Spanish & English)",
            "match_type": "sender",
            "match_value": "noreply|no-reply|sin-respuesta",
            "action_type": "tag",
            "action_value": "Trash",
            "priority": 1
        },
        {
            "name": "Promotional Emails",
            "description": "Tag promotional and marketing emails",
            "match_type": "subject",
            "match_value": "promo|promotion|oferta|descuento|oferta especial|special offer",
            "action_type": "tag",
            "action_value": "Trash",
            "priority": 2
        },
        {
            "name": "Newsletter Detection",
            "description": "Tag newsletter and subscription emails",
            "match_type": "body",
            "match_value": "unsubscribe|darse de baja|newsletter|boletín|suscripción",
            "action_type": "tag",
            "action_value": "Trash",
            "priority": 3
        },

        # === SOCIAL MEDIA ===
        {
            "name": "Facebook Notifications",
            "description": "Tag Facebook notifications",
            "match_type": "sender",
            "match_value": "facebook|facebookmail",
            "action_type": "tag",
            "action_value": "Social",
            "priority": 4
        },
        {
            "name": "Instagram Notifications",
            "description": "Tag Instagram notifications",
            "match_type": "sender",
            "match_value": "instagram|instagram.com",
            "action_type": "tag",
            "action_value": "Social",
            "priority": 5
        },
        {
            "name": "Twitter/X Notifications",
            "description": "Tag Twitter/X notifications",
            "match_type": "sender",
            "match_value": "twitter|x.com|t.co",
            "action_type": "tag",
            "action_value": "Social",
            "priority": 6
        },
        {
            "name": "LinkedIn Notifications",
            "description": "Tag LinkedIn notifications",
            "match_type": "sender",
            "match_value": "linkedin|linked.in",
            "action_type": "tag",
            "action_value": "Social",
            "priority": 7
        },

        # === DEPLOYMENT & TECHNICAL ===
        {
            "name": "Deployment Notifications",
            "description": "Tag deployment and technical notifications",
            "match_type": "subject",
            "match_value": "deploy|deployment|despliegue|build|pipeline|ci/cd|jenkins|github actions",
            "action_type": "tag",
            "action_value": "Technical",
            "priority": 8
        },
        {
            "name": "System Alerts",
            "description": "Tag system and monitoring alerts",
            "match_type": "subject",
            "match_value": "alert|alerta|warning|advertencia|error|failed|falló",
            "action_type": "tag",
            "action_value": "Technical",
            "priority": 9
        },

        # === ORDERS & BILLING (PROFESSIONAL FOCUS) ===
        {
            "name": "Order Confirmations",
            "description": "Tag order confirmations and updates",
            "match_type": "subject",
            "match_value": "order confirmation|pedido confirmado|your order|tu pedido|orden de compra",
            "action_type": "tag",
            "action_value": "Orders",
            "priority": 10
        },
        {
            "name": "Shipping Notifications",
            "description": "Tag shipping and delivery notifications",
            "match_type": "subject",
            "match_value": "shipped|enviado|delivered|entregado|on the way|en camino|arrives today|llega hoy",
            "action_type": "tag",
            "action_value": "Orders",
            "priority": 11
        },
        {
            "name": "Invoice Detection",
            "description": "Tag invoices and billing documents",
            "match_type": "subject",
            "match_value": "invoice|factura|billing|facturación|recibo|comprobante|pdf",
            "action_type": "tag",
            "action_value": "Bills",
            "priority": 12
        },
        {
            "name": "Payment Receipts",
            "description": "Tag payment confirmations and receipts",
            "match_type": "subject",
            "match_value": "payment|paid|pago|pagado|receipt|recibo|transaction|transacción",
            "action_type": "tag",
            "action_value": "Bills",
            "priority": 13
        },
        {
            "name": "Subscription Billing",
            "description": "Tag subscription and recurring billing emails",
            "match_type": "subject",
            "match_value": "subscription|suscripción|renewal|renovación|billing cycle|ciclo de facturación",
            "action_type": "tag",
            "action_value": "Bills",
            "priority": 14
        },

        # === AMAZON SPECIFIC ===
        {
            "name": "Amazon Orders",
            "description": "Tag Amazon order notifications",
            "match_type": "sender",
            "match_value": "amazon|amazon.com|order-update",
            "action_type": "tag",
            "action_value": "Orders",
            "priority": 15
        }
    ]


def validate_rule(rule_data: Dict[str, Any]) -> list[str]:
    """Validate rule data and return list of errors"""
    errors = []

    # Required fields
    required_fields = ["name", "match_type", "match_value", "action_type"]
    for field in required_fields:
        if not rule_data.get(field):
            errors.append(f"{field} is required")

    # Validate match_type
    valid_match_types = ["sender", "subject", "body", "regex", "header"]
    if rule_data.get("match_type") and rule_data["match_type"] not in valid_match_types:
        errors.append(f"match_type must be one of: {', '.join(valid_match_types)}")

    # Validate action_type
    valid_action_types = ["tag", "archive", "mark_read", "move"]
    if rule_data.get("action_type") and rule_data["action_type"] not in valid_action_types:
        errors.append(f"action_type must be one of: {', '.join(valid_action_types)}")

    # Validate action_value for certain actions
    if rule_data.get("action_type") in ["tag", "move"] and not rule_data.get("action_value"):
        errors.append("action_value is required for tag and move actions")

    # Validate regex
    if rule_data.get("match_type") == "regex":
        try:
            re.compile(rule_data["match_value"])
        except re.error as e:
            errors.append(f"Invalid regex pattern: {e}")

    return errors
