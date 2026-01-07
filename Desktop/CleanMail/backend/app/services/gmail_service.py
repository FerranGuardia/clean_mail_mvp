"""
Gmail API service - Handle Gmail interactions
"""

from typing import List, Dict, Any
import base64
import re
from datetime import datetime
import requests
from app.models.user import User
from app.models.rule import Rule


def get_emails(user: User, max_results: int = 10) -> List[Dict[str, Any]]:
    """Fetch emails from user's Gmail inbox"""
    # Check if token is expired and refresh if needed
    if is_token_expired(user):
        refresh_access_token(user)

    headers = {"Authorization": f"Bearer {user.access_token}"}

    # Get message list
    messages_url = "https://www.googleapis.com/gmail/v1/users/me/messages"
    params = {
        "maxResults": max_results,
        "labelIds": ["INBOX"],
        "q": "is:unread"  # Only get unread emails for processing
    }

    response = requests.get(messages_url, headers=headers, params=params)
    if response.status_code != 200:
        raise Exception(f"Failed to fetch messages: {response.text}")

    messages_data = response.json()
    messages = []

    # Get full message details
    for message_info in messages_data.get("messages", []):
        message_detail = get_message_detail(user, message_info["id"])
        if message_detail:
            messages.append(message_detail)

    return messages


def get_message_detail(user: User, message_id: str) -> Dict[str, Any]:
    """Get detailed message information"""
    headers = {"Authorization": f"Bearer {user.access_token}"}

    message_url = f"https://www.googleapis.com/gmail/v1/users/me/messages/{message_id}"
    params = {"format": "full"}

    response = requests.get(message_url, headers=headers, params=params)
    if response.status_code != 200:
        return None

    message_data = response.json()

    # Extract headers
    headers = {header["name"]: header["value"] for header in message_data.get("payload", {}).get("headers", [])}

    # Extract body (simplified)
    body = ""
    if "parts" in message_data.get("payload", {}):
        for part in message_data["payload"]["parts"]:
            if part.get("mimeType") == "text/plain":
                body_data = part.get("body", {}).get("data", "")
                if body_data:
                    body = base64.urlsafe_b64decode(body_data).decode("utf-8", errors="ignore")
                    break

    return {
        "id": message_id,
        "subject": headers.get("Subject", ""),
        "sender": headers.get("From", ""),
        "to": headers.get("To", ""),
        "received_at": parse_date(headers.get("Date")),
        "body_preview": body[:200] + "..." if len(body) > 200 else body,
        "labels": message_data.get("labelIds", [])
    }


def apply_rule(user: User, email: Dict[str, Any], rule: Rule) -> bool:
    """Apply a rule to an email"""
    try:
        if rule.action_type == "tag":
            return add_label(user, email["id"], rule.action_value)
        elif rule.action_type == "archive":
            return archive_email(user, email["id"])
        elif rule.action_type == "mark_read":
            return mark_as_read(user, email["id"])
        elif rule.action_type == "move":
            return move_to_folder(user, email["id"], rule.action_value)
        return False
    except Exception as e:
        print(f"Error applying rule {rule.name}: {e}")
        return False


def add_label(user: User, message_id: str, label_name: str) -> bool:
    """Add a label to an email"""
    headers = {"Authorization": f"Bearer {user.access_token}"}

    # First, ensure the label exists
    label_id = get_or_create_label(user, label_name)
    if not label_id:
        return False

    # Add label to message
    modify_url = f"https://www.googleapis.com/gmail/v1/users/me/messages/{message_id}/modify"
    data = {"addLabelIds": [label_id]}

    response = requests.post(modify_url, headers=headers, json=data)
    return response.status_code == 200


def archive_email(user: User, message_id: str) -> bool:
    """Archive an email (remove from inbox)"""
    headers = {"Authorization": f"Bearer {user.access_token}"}

    modify_url = f"https://www.googleapis.com/gmail/v1/users/me/messages/{message_id}/modify"
    data = {"removeLabelIds": ["INBOX"]}

    response = requests.post(modify_url, headers=headers, json=data)
    return response.status_code == 200


def mark_as_read(user: User, message_id: str) -> bool:
    """Mark an email as read"""
    headers = {"Authorization": f"Bearer {user.access_token}"}

    modify_url = f"https://www.googleapis.com/gmail/v1/users/me/messages/{message_id}/modify"
    data = {"removeLabelIds": ["UNREAD"]}

    response = requests.post(modify_url, headers=headers, json=data)
    return response.status_code == 200


def move_to_folder(user: User, message_id: str, folder_name: str) -> bool:
    """Move email to a specific folder/label"""
    # For simplicity, this is the same as adding a label
    return add_label(user, message_id, folder_name)


def get_or_create_label(user: User, label_name: str) -> str:
    """Get label ID or create label if it doesn't exist"""
    headers = {"Authorization": f"Bearer {user.access_token}"}

    # Check if label exists
    labels_url = "https://www.googleapis.com/gmail/v1/users/me/labels"
    response = requests.get(labels_url, headers=headers)

    if response.status_code == 200:
        labels = response.json().get("labels", [])
        for label in labels:
            if label["name"] == label_name:
                return label["id"]

    # Create new label
    create_url = "https://www.googleapis.com/gmail/v1/users/me/labels"
    data = {
        "name": label_name,
        "labelListVisibility": "labelShow",
        "messageListVisibility": "show"
    }

    response = requests.post(create_url, headers=headers, json=data)
    if response.status_code == 200:
        return response.json()["id"]

    return None


def is_token_expired(user: User) -> bool:
    """Check if access token is expired"""
    return datetime.utcnow() >= user.token_expires_at


def refresh_access_token(user: User):
    """Refresh expired access token"""
    # This would need to be implemented with proper token refresh logic
    # For now, we'll assume tokens don't expire during development
    pass


def parse_date(date_string: str) -> datetime:
    """Parse email date string to datetime object"""
    if not date_string:
        return datetime.utcnow()

    # Simple date parsing (you might want to use email.utils.parsedate_to_datetime)
    try:
        # Try RFC 2822 format
        from email.utils import parsedate_to_datetime
        return parsedate_to_datetime(date_string)
    except:
        return datetime.utcnow()
