#!/usr/bin/env python3
"""
CleanMail Setup Script
Helps set up the development environment
"""

import os
import sys
import subprocess
import platform

def run_command(command, cwd=None):
    """Run a command and return success status"""
    try:
        result = subprocess.run(command, shell=True, cwd=cwd, check=True, capture_output=True, text=True)
        return True, result.stdout
    except subprocess.CalledProcessError as e:
        return False, e.stderr

def main():
    print("CleanMail Setup")
    print("=" * 50)

    # Check Python version
    python_version = sys.version_info
    if python_version < (3, 8):
        print("ERROR: Python 3.8+ required")
        return False

    print(f"OK: Python {python_version.major}.{python_version.minor} detected")

    # Check Node.js
    node_check, node_output = run_command("node --version")
    if not node_check:
        print("ERROR: Node.js not found. Please install Node.js 16+")
        return False

    print(f"OK: Node.js detected: {node_output.strip()}")

    # Setup backend
    print("\nSetting up backend...")

    # Create virtual environment if it doesn't exist
    if not os.path.exists("venv"):
        print("Creating virtual environment...")
        success, output = run_command("python -m venv venv")
        if not success:
            print(f"ERROR: Failed to create virtual environment: {output}")
            return False

    # Activate virtual environment and install dependencies
    if platform.system() == "Windows":
        activate_cmd = "venv\\Scripts\\activate"
        pip_cmd = "venv\\Scripts\\pip"
    else:
        activate_cmd = "source venv/bin/activate"
        pip_cmd = "venv/bin/pip"

    print("Installing Python dependencies...")
    success, output = run_command(f"{pip_cmd} install -r backend/requirements.txt")
    if not success:
        print(f"ERROR: Failed to install Python dependencies: {output}")
        return False

    # Setup frontend
    print("\nSetting up frontend...")
    success, output = run_command("npm install", cwd="frontend")
    if not success:
        print(f"ERROR: Failed to install Node.js dependencies: {output}")
        return False

    # Create .env file if it doesn't exist
    env_file = "backend/.env"
    if not os.path.exists(env_file):
        print("\nCreating environment configuration...")
        env_content = """# Database
DATABASE_URL=sqlite:///./cleanmail.db

# Google OAuth - Get these from Google Cloud Console
GOOGLE_CLIENT_ID=your-google-client-id
GOOGLE_CLIENT_SECRET=your-google-client-secret
GOOGLE_REDIRECT_URI=http://localhost:8000/api/auth/callback

# Security - Change this in production!
SECRET_KEY=your-secret-key-change-in-production
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

# Application
DEBUG=True
"""
        try:
            with open(env_file, 'w') as f:
                f.write(env_content)
            print("OK: Created .env file - Please configure your Google OAuth credentials")
        except Exception as e:
            print(f"ERROR: Failed to create .env file: {e}")

    # Initialize database
    print("\nInitializing database...")
    success, output = run_command(f"{pip_cmd} run python -c \"from app.database import create_tables; create_tables()\"", cwd="backend")
    if not success:
        print(f"WARNING: Database initialization warning: {output}")

    # Initialize built-in rules
    print("\nSetting up professional rules...")
    success, output = run_command(f"{pip_cmd} run python scripts/init_rules.py", cwd="backend")
    if not success:
        print(f"WARNING: Rule initialization warning: {output}")

    print("\nSetup complete!")
    print("\nTo start development:")
    print("1. Configure your Google OAuth credentials in backend/.env")
    print("2. Start backend: cd backend && uvicorn app.main:app --reload")
    print("3. Start frontend: cd frontend && npm run dev")
    print("\nRead the README.md for detailed instructions")

    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
