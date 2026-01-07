"""
Pydantic schemas for Rule model
"""

from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class RuleBase(BaseModel):
    name: str
    description: Optional[str] = None
    match_type: str  # sender, subject, body, regex, header
    match_value: str
    action_type: str  # tag, archive, mark_read, move
    action_value: Optional[str] = None
    priority: int = 0
    is_active: bool = True


class RuleCreate(RuleBase):
    pass


class RuleUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    match_type: Optional[str] = None
    match_value: Optional[str] = None
    action_type: Optional[str] = None
    action_value: Optional[str] = None
    priority: Optional[int] = None
    is_active: Optional[bool] = None


class Rule(RuleBase):
    id: int
    user_id: int
    created_at: datetime
    updated_at: Optional[datetime]

    class Config:
        from_attributes = True
