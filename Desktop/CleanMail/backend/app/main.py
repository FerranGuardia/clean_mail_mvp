"""
CleanMail - Gmail Inbox Cleaner MVP
FastAPI Backend Application
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import auth, rules, emails, dashboard

# Create FastAPI app
app = FastAPI(
    title="CleanMail API",
    description="Gmail Inbox Cleaner - Rule-based email organization",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# CORS middleware for frontend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:3000"],  # Vite dev server & React dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth.router, prefix="/api/auth", tags=["Authentication"])
app.include_router(rules.router, prefix="/api/rules", tags=["Rules"])
app.include_router(emails.router, prefix="/api/emails", tags=["Emails"])
app.include_router(dashboard.router, prefix="/api/dashboard", tags=["Dashboard"])

@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "message": "Welcome to CleanMail API",
        "version": "1.0.0",
        "docs": "/docs"
    }

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy"}
