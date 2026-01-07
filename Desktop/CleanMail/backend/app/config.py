"""
Configuration settings for CleanMail
"""

import os
from typing import Optional
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings"""

    # Database
    database_url: str = "sqlite:///./cleanmail.db"

    # Google OAuth
    google_client_id: Optional[str] = None
    google_client_secret: Optional[str] = None
    google_redirect_uri: str = "http://localhost:8000/api/auth/callback"

    # Security
    secret_key: str = "your-secret-key-change-in-production"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30

    # Gmail API
    gmail_scopes: list = [
        "https://www.googleapis.com/auth/gmail.readonly",
        "https://www.googleapis.com/auth/gmail.modify",
        "https://www.googleapis.com/auth/gmail.labels"
    ]

    # Application
    debug: bool = True
    api_v1_prefix: str = "/api/v1"

    class Config:
        env_file = ".env"
        case_sensitive = False


# Global settings instance
settings = Settings()
