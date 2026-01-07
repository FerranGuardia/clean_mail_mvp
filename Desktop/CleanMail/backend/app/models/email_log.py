"""
Email processing log model
"""

from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.database import Base


class EmailLog(Base):
    __tablename__ = "email_logs"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    rule_id = Column(Integer, ForeignKey("rules.id"), nullable=True)

    # Email information
    gmail_message_id = Column(String, nullable=False)
    subject = Column(String, nullable=True)
    sender = Column(String, nullable=True)
    received_at = Column(DateTime, nullable=True)

    # Processing information
    applied_action = Column(String, nullable=False)  # tag, archive, mark_read, move
    action_value = Column(String, nullable=True)  # label name, etc.
    success = Column(String, default=True)  # True, False, or error message

    # Metadata
    processed_at = Column(DateTime(timezone=True), server_default=func.now())

    # Relationships
    user = relationship("User", back_populates="email_logs")
    rule = relationship("Rule", back_populates="email_logs")
