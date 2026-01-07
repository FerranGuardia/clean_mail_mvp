"""
Rule model for email processing rules
"""

from sqlalchemy import Column, Integer, String, Text, Boolean, ForeignKey, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.database import Base


class Rule(Base):
    __tablename__ = "rules"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    # Rule definition
    name = Column(String, nullable=False)
    description = Column(Text, nullable=True)

    # Match criteria
    match_type = Column(String, nullable=False)  # sender, subject, body, regex, header
    match_value = Column(String, nullable=False)

    # Action to take
    action_type = Column(String, nullable=False)  # tag, archive, mark_read, move
    action_value = Column(String, nullable=True)  # label name, folder name, etc.

    # Rule settings
    priority = Column(Integer, default=0)  # Lower number = higher priority
    is_active = Column(Boolean, default=True)

    # Metadata
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    # Relationships
    user = relationship("User", back_populates="rules")
    email_logs = relationship("EmailLog", back_populates="rule")
