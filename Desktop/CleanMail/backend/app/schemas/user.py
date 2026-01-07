"""
Pydantic schemas for User model
"""

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    email: EmailStr
    name: Optional[str] = None
    picture: Optional[str] = None


class UserCreate(UserBase):
    google_id: str
    access_token: str
    refresh_token: Optional[str] = None
    token_expires_at: datetime


class UserUpdate(BaseModel):
    name: Optional[str] = None
    picture: Optional[str] = None
    is_active: Optional[bool] = None


class User(UserBase):
    id: int
    google_id: str
    is_active: bool
    created_at: datetime
    updated_at: Optional[datetime]

    class Config:
        from_attributes = True


class UserInDB(User):
    access_token: str
    refresh_token: Optional[str]
    token_expires_at: datetime
