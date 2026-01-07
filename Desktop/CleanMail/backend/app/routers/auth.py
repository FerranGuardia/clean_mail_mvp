"""
Authentication router - Google OAuth integration
"""

from datetime import datetime, timedelta
from typing import Optional
from fastapi import APIRouter, Depends, HTTPException, status, Header
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
import requests

from app import config
from app.database import get_db
from app.models.user import User
from app.schemas.user import UserCreate
from app.services.auth_service import create_access_token, verify_token

router = APIRouter()


@router.get("/google")
async def google_login():
    """Initiate Google OAuth flow"""
    google_auth_url = (
        "https://accounts.google.com/o/oauth2/auth?"
        f"client_id={config.settings.google_client_id}&"
        "response_type=code&"
        f"scope={' '.join(config.settings.gmail_scopes)}&"
        f"redirect_uri={config.settings.google_redirect_uri}&"
        "access_type=offline&"
        "prompt=consent"
    )
    return RedirectResponse(google_auth_url)


@router.get("/callback")
async def google_callback(code: str, db: Session = Depends(get_db)):
    """Handle Google OAuth callback"""
    # Exchange code for tokens
    token_data = {
        "client_id": config.settings.google_client_id,
        "client_secret": config.settings.google_client_secret,
        "code": code,
        "grant_type": "authorization_code",
        "redirect_uri": config.settings.google_redirect_uri,
    }

    token_response = requests.post("https://oauth2.googleapis.com/token", data=token_data)
    if token_response.status_code != 200:
        raise HTTPException(status_code=400, detail="Failed to get access token")

    tokens = token_response.json()

    # Get user info from Google
    user_response = requests.get(
        "https://www.googleapis.com/oauth2/v2/userinfo",
        headers={"Authorization": f"Bearer {tokens['access_token']}"}
    )

    if user_response.status_code != 200:
        raise HTTPException(status_code=400, detail="Failed to get user info")

    user_info = user_response.json()

    # Calculate token expiry
    expires_at = datetime.utcnow() + timedelta(seconds=tokens["expires_in"])

    # Create or update user
    user = db.query(User).filter(User.google_id == user_info["id"]).first()

    if user:
        # Update existing user
        user.access_token = tokens["access_token"]
        user.refresh_token = tokens.get("refresh_token")
        user.token_expires_at = expires_at
        user.name = user_info.get("name")
        user.picture = user_info.get("picture")
    else:
        # Create new user
        user_data = UserCreate(
            email=user_info["email"],
            google_id=user_info["id"],
            name=user_info.get("name"),
            picture=user_info.get("picture"),
            access_token=tokens["access_token"],
            refresh_token=tokens.get("refresh_token"),
            token_expires_at=expires_at,
        )
        user = User(**user_data.model_dump())
        db.add(user)

    db.commit()
    db.refresh(user)

    # Create JWT token for our app
    access_token = create_access_token(data={"sub": str(user.id)})

    # Redirect to frontend with token
    frontend_url = "http://localhost:5173/auth/callback"
    return RedirectResponse(f"{frontend_url}?token={access_token}")


@router.get("/me")
async def get_current_user(
    authorization: str = Header(None),
    db: Session = Depends(get_db)
):
    """Get current user information"""
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Invalid authentication")
    token = authorization.split(" ")[1]
    user_id = verify_token(token)

    user = db.query(User).filter(User.id == int(user_id)).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return {
        "id": user.id,
        "email": user.email,
        "name": user.name,
        "picture": user.picture
    }
