"""
Rules router - CRUD operations for email processing rules
"""

from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.rule import Rule
from app.schemas.rule import RuleCreate, RuleUpdate, Rule as RuleSchema

router = APIRouter()


@router.get("/", response_model=List[RuleSchema])
async def get_rules(
    user_id: int,  # TODO: Get from JWT token
    db: Session = Depends(get_db)
):
    """Get all rules for a user"""
    rules = db.query(Rule).filter(Rule.user_id == user_id).all()
    return rules


@router.post("/", response_model=RuleSchema)
async def create_rule(
    rule: RuleCreate,
    user_id: int,  # TODO: Get from JWT token
    db: Session = Depends(get_db)
):
    """Create a new rule"""
    db_rule = Rule(**rule.model_dump(), user_id=user_id)
    db.add(db_rule)
    db.commit()
    db.refresh(db_rule)
    return db_rule


@router.get("/{rule_id}", response_model=RuleSchema)
async def get_rule(
    rule_id: int,
    user_id: int,  # TODO: Get from JWT token
    db: Session = Depends(get_db)
):
    """Get a specific rule"""
    rule = db.query(Rule).filter(Rule.id == rule_id, Rule.user_id == user_id).first()
    if not rule:
        raise HTTPException(status_code=404, detail="Rule not found")
    return rule


@router.put("/{rule_id}", response_model=RuleSchema)
async def update_rule(
    rule_id: int,
    rule_update: RuleUpdate,
    user_id: int,  # TODO: Get from JWT token
    db: Session = Depends(get_db)
):
    """Update a rule"""
    rule = db.query(Rule).filter(Rule.id == rule_id, Rule.user_id == user_id).first()
    if not rule:
        raise HTTPException(status_code=404, detail="Rule not found")

    for field, value in rule_update.model_dump(exclude_unset=True).items():
        setattr(rule, field, value)

    db.commit()
    db.refresh(rule)
    return rule


@router.delete("/{rule_id}")
async def delete_rule(
    rule_id: int,
    user_id: int,  # TODO: Get from JWT token
    db: Session = Depends(get_db)
):
    """Delete a rule"""
    rule = db.query(Rule).filter(Rule.id == rule_id, Rule.user_id == user_id).first()
    if not rule:
        raise HTTPException(status_code=404, detail="Rule not found")

    db.delete(rule)
    db.commit()
    return {"message": "Rule deleted successfully"}
