#!/usr/bin/env python3
"""
CleanMail Deployment Readiness Checker
Checks if your project is ready for deployment
"""

import os
import sys
import subprocess
import json

def check_file_exists(filepath, description):
    """Check if a file exists"""
    if os.path.exists(filepath):
        print(f"[OK] {description}: {filepath}")
        return True
    else:
        print(f"[MISSING] {description}: {filepath}")
        return False

def check_command(command, description):
    """Check if a command runs successfully"""
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"[OK] {description}")
            return True
        else:
            print(f"[FAILED] {description}: {result.stderr}")
            return False
    except Exception as e:
        print(f"[ERROR] {description}: {e}")
        return False

def check_frontend_build():
    """Check if frontend builds successfully"""
    print("\n[BUILD] Checking frontend build...")
    os.chdir('frontend')
    success = check_command("npm run build", "Frontend build")
    os.chdir('..')
    return success

def check_backend_imports():
    """Check if backend imports successfully"""
    print("\n[PYTHON] Checking backend imports...")
    os.chdir('backend')
    success = check_command("python -c \"import app.main; print('Backend imports OK')\"", "Backend import")
    os.chdir('..')
    return success

def main():
    print("CleanMail Deployment Readiness Check")
    print("=" * 50)

    checks_passed = 0
    total_checks = 0

    # File existence checks
    print("\n[FILES] Checking required files...")

    files_to_check = [
        ('frontend/package.json', 'Frontend package.json'),
        ('frontend/vercel.json', 'Vercel config'),
        ('backend/requirements.txt', 'Backend requirements'),
        ('backend/railway.json', 'Railway config'),
        ('backend/runtime.txt', 'Python version config'),
    ]

    for filepath, description in files_to_check:
        total_checks += 1
        if check_file_exists(filepath, description):
            checks_passed += 1

    # Build checks
    total_checks += 1
    if check_frontend_build():
        checks_passed += 1

    total_checks += 1
    if check_backend_imports():
        checks_passed += 1

    # Summary
    print("\n" + "=" * 50)
    print(f"Deployment Readiness: {checks_passed}/{total_checks} checks passed")

    if checks_passed == total_checks:
        print("SUCCESS: Your CleanMail project is ready for deployment!")
        print("\nNext steps:")
        print("1. Push your code to GitHub")
        print("2. Deploy backend to Railway")
        print("3. Deploy frontend to Vercel")
        print("4. Follow the deployment guide in DEPLOYMENT_GUIDE.md")
    else:
        print("WARNING: Some checks failed. Please fix the issues before deploying.")
        print("Check the error messages above for details.")

    return checks_passed == total_checks

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
