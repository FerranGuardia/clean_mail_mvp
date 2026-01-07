"""
Authentication service - JWT token management
"""

from datetime import datetime, timedelta
from typing import Optional
from jose import jwt
from fastapi import HTTPException, status

from app import config


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    """Create JWT access token for user authentication.

    Args:
        data: Dictionary containing token payload data (typically user ID)
        expires_delta: Optional custom expiration time. If None, uses default from config.

    Returns:
        str: Encoded JWT token string

    Example:
        >>> token = create_access_token({"sub": "user123"})
        >>> print(token)  # eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...
    """
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=config.settings.access_token_expire_minutes)

    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, config.settings.secret_key, algorithm=config.settings.algorithm)
    return encoded_jwt


def verify_token(token: str):
    """Verify and decode JWT access token.

    Args:
        token: JWT token string to verify

    Returns:
        str: User ID extracted from token payload

    Raises:
        HTTPException: If token is invalid, expired, or malformed
            - 401 Unauthorized for invalid credentials

    Example:
        >>> user_id = verify_token("eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...")
        >>> print(user_id)  # user123
    """
    try:
        payload = jwt.decode(token, config.settings.secret_key, algorithms=[config.settings.algorithm])
        user_id: str = payload.get("sub")
        if user_id is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid authentication credentials",
                headers={"WWW-Authenticate": "Bearer"},
            )
        return user_id
    except jwt.PyJWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
