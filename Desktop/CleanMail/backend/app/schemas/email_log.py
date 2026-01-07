"""
Pydantic schemas for EmailLog model
"""

from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class EmailLogBase(BaseModel):
    gmail_message_id: str
    subject: Optional[str] = None
    sender: Optional[str] = None
    received_at: Optional[datetime] = None
    applied_action: str
    action_value: Optional[str] = None
    success: bool = True


class EmailLogCreate(EmailLogBase):
    user_id: int
    rule_id: Optional[int] = None


class EmailLog(EmailLogBase):
    id: int
    user_id: int
    rule_id: Optional[int]
    processed_at: datetime

    class Config:
        from_attributes = True
