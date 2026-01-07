# CleanMail Backend

## Environment Variables

Create a `.env` file in this directory with the following variables:

```env
# Database
DATABASE_URL=sqlite:///./cleanmail.db

# Google OAuth - Get these from Google Cloud Console
GOOGLE_CLIENT_ID=your-google-client-id
GOOGLE_CLIENT_SECRET=your-google-client-secret
GOOGLE_REDIRECT_URI=https://your-backend-domain.up.railway.app/api/auth/callback

# Security
SECRET_KEY=your-production-secret-key-change-this
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

# Application
DEBUG=False
API_V1_PREFIX=/api/v1
```

## Google OAuth Setup

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a project or select existing one
3. Enable Gmail API
4. Create OAuth 2.0 credentials
5. Add your production domain to authorized redirect URIs

## Railway Deployment

1. Connect your GitHub repository to Railway
2. Set the environment variables above in Railway dashboard
3. Deploy automatically

## Local Development

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```
