#!/usr/bin/env python3
"""
CleanMail Development Server Starter
Starts both backend and frontend development servers
"""

import subprocess
import sys
import time
import platform

def run_command(command, shell=True):
    """Run a command in background"""
    if platform.system() == "Windows":
        return subprocess.Popen(command, shell=shell, creationflags=subprocess.CREATE_NEW_CONSOLE)
    else:
        return subprocess.Popen(command, shell=shell)

def main():
    print("🚀 Starting CleanMail Development Servers")
    print("=" * 50)

    # Start backend server
    print("📡 Starting backend server...")
    backend_cmd = "cd backend && uvicorn app.main:app --reload --host 0.0.0.0 --port 8000"
    backend_process = run_command(backend_cmd)

    # Wait a bit for backend to start
    time.sleep(3)

    # Start frontend server
    print("⚛️ Starting frontend server...")
    frontend_cmd = "cd frontend && npm run dev"
    frontend_process = run_command(frontend_cmd)

    print("\n✅ Development servers started!")
    print("📱 Frontend: http://localhost:5173")
    print("🔧 Backend API: http://localhost:8000")
    print("📚 API Docs: http://localhost:8000/docs")
    print("\nPress Ctrl+C to stop all servers")

    try:
        # Keep running until user stops
        backend_process.wait()
        frontend_process.wait()
    except KeyboardInterrupt:
        print("\n🛑 Stopping servers...")
        backend_process.terminate()
        frontend_process.terminate()
        print("✅ All servers stopped")

if __name__ == "__main__":
    main()
