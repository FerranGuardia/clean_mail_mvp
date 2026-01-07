#!/usr/bin/env python3
"""
Initialize built-in professional rules for CleanMail
Run this script to populate the database with default rules
"""

import sys
import os

# Add the app directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from app.database import SessionLocal, create_tables
from app.models.rule import Rule
from app.services.rule_engine import get_built_in_rules

def init_builtin_rules():
    """Initialize the database with built-in professional rules"""
    print("Initializing CleanMail professional rules...")

    # Create tables if they don't exist
    create_tables()

    db = SessionLocal()
    try:
        # Check if rules already exist
        existing_rules = db.query(Rule).filter(Rule.user_id == 0).count()  # user_id 0 = built-in
        if existing_rules > 0:
            print(f"Built-in rules already exist ({existing_rules} rules found)")
            return

        # Get built-in rules
        builtin_rules = get_built_in_rules()

        # Create rules in database
        for rule_data in builtin_rules:
            rule = Rule(
                user_id=0,  # 0 = built-in rules
                name=rule_data["name"],
                description=rule_data["description"],
                match_type=rule_data["match_type"],
                match_value=rule_data["match_value"],
                action_type=rule_data["action_type"],
                action_value=rule_data.get("action_value"),
                priority=rule_data["priority"],
                is_active=True
            )
            db.add(rule)

        db.commit()
        print(f"✅ Successfully created {len(builtin_rules)} built-in professional rules")
        print("\n📋 Rules created:")
        for rule in builtin_rules:
            print(f"  • {rule['name']} → {rule['action_value']}")

    except Exception as e:
        db.rollback()
        print(f"❌ Error initializing rules: {e}")
        return False
    finally:
        db.close()

    return True

if __name__ == "__main__":
    success = init_builtin_rules()
    if success:
        print("\n🎯 CleanMail is ready with professional bill-tracking rules!")
        print("Your Gmail will stay clean and all invoices will be properly tracked.")
    sys.exit(0 if success else 1)
