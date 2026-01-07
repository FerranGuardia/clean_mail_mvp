# CleanMail Deployment Guide

## Overview

CleanMail can be deployed using modern cloud platforms. This guide covers deployment to Railway (backend) and Vercel (frontend).

## Prerequisites

- Google Cloud Console project with Gmail API enabled
- OAuth 2.0 credentials configured
- Domain name (optional, for custom domain)

## Backend Deployment (Railway)

### Railway Setup

1. **Create Railway Account:**
   Visit [Railway.app](https://railway.app) and sign up

2. **Connect Repository:**
   - Click "New Project"
   - Choose "Deploy from GitHub repo"
   - Select your CleanMail repository

3. **Configure Environment:**
   Railway will automatically detect Python and install dependencies

4. **Set Environment Variables:**
   ```
   DATABASE_URL=postgresql://...
   GOOGLE_CLIENT_ID=your-google-client-id
   GOOGLE_CLIENT_SECRET=your-google-client-secret
   GOOGLE_REDIRECT_URI=https://your-backend-url/api/auth/callback
   SECRET_KEY=your-production-secret-key
   DEBUG=False
   ```

5. **Database Setup:**
   - Railway provides PostgreSQL automatically
   - Update `DATABASE_URL` with the provided connection string

### Production Configuration

Update `backend/app/config.py` for production:
```python
class Settings(BaseSettings):
    database_url: str = os.getenv("DATABASE_URL")
    debug: bool = False
    # ... other settings
```

## Frontend Deployment (Vercel)

### Vercel Setup

1. **Create Vercel Account:**
   Visit [Vercel.com](https://vercel.com) and sign up

2. **Connect Repository:**
   - Click "New Project"
   - Import your GitHub repository
   - Select the `frontend` directory

3. **Configure Build Settings:**
   ```
   Framework Preset: Vite
   Root Directory: frontend
   Build Command: npm run build
   Output Directory: dist
   ```

4. **Set Environment Variables:**
   ```
   VITE_API_URL=https://your-backend-url
   ```

### Custom Domain (Optional)

1. **Add Domain in Vercel:**
   - Go to project settings
   - Add your custom domain
   - Follow DNS configuration instructions

2. **Update Google OAuth:**
   - Add production redirect URI in Google Cloud Console
   - Update environment variables with production URLs

## Environment Variables

### Backend (.env)
```env
# Database
DATABASE_URL=postgresql://user:password@host:port/database

# Google OAuth
GOOGLE_CLIENT_ID=your-production-client-id
GOOGLE_CLIENT_SECRET=your-production-client-secret
GOOGLE_REDIRECT_URI=https://your-backend-domain/api/auth/callback

# Security
SECRET_KEY=your-256-bit-secret-key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

# Application
DEBUG=False
API_V1_PREFIX=/api/v1
```

### Frontend (.env.production)
```env
VITE_API_URL=https://your-backend-domain
```

## Database Migration

### From SQLite to PostgreSQL

1. **Export SQLite data:**
   ```bash
   sqlite3 cleanmail.db .dump > backup.sql
   ```

2. **Convert to PostgreSQL format:**
   Use `pgloader` or manual conversion scripts

3. **Import to PostgreSQL:**
   ```sql
   psql $DATABASE_URL < converted_backup.sql
   ```

### Alembic Setup (Future)

```bash
# Initialize Alembic
alembic init alembic

# Create migration
alembic revision --autogenerate -m "Initial migration"

# Apply migration
alembic upgrade head
```

## Security Checklist

### Before Going Live

- [ ] HTTPS enabled on all domains
- [ ] OAuth redirect URIs configured correctly
- [ ] SECRET_KEY changed from default
- [ ] DEBUG=False in production
- [ ] Database credentials secured
- [ ] CORS configured for production domains
- [ ] Rate limiting implemented
- [ ] Input validation active
- [ ] Error logging configured

### Monitoring Setup

1. **Application Monitoring:**
   - Railway provides basic metrics
   - Consider adding Sentry for error tracking

2. **Database Monitoring:**
   - Monitor connection pools
   - Set up alerts for slow queries

3. **Uptime Monitoring:**
   - Use services like UptimeRobot
   - Monitor both frontend and backend

## Performance Optimization

### Backend
- Enable Gzip compression in Railway
- Configure database connection pooling
- Implement caching for Gmail API responses

### Frontend
- Enable Vercel analytics
- Configure image optimization
- Set up CDN for static assets

## Backup Strategy

### Database Backups
- Railway provides automatic PostgreSQL backups
- Configure backup retention policies
- Test backup restoration regularly

### Code Backups
- All code is in Git
- Use GitHub for version control
- Tag releases for production deployments

## Scaling Considerations

### Vertical Scaling
- Upgrade Railway plan for more resources
- Increase database instance size
- Add more memory/CPU as needed

### Horizontal Scaling
- Implement Redis for session storage
- Use load balancers for multiple instances
- Consider API rate limiting

## Troubleshooting Deployment

### Common Issues

**Build Failures:**
- Check build logs in Railway/Vercel
- Verify all dependencies are in requirements.txt/package.json
- Check for platform-specific code

**Runtime Errors:**
- Check environment variables are set correctly
- Verify database connectivity
- Check OAuth configuration

**Performance Issues:**
- Monitor database query performance
- Check for memory leaks
- Optimize API response times

### Logs and Debugging

**Railway Logs:**
```bash
railway logs
```

**Vercel Logs:**
- Access through Vercel dashboard
- Check function logs for serverless functions

**Database Logs:**
- Check Railway database logs
- Monitor slow query logs

## Cost Optimization

### Railway Costs
- Hobby plan: $5/month (sufficient for MVP)
- Pro plan: $10/month (for higher usage)

### Vercel Costs
- Hobby plan: Free
- Pro plan: $20/month (for custom domains)

### Gmail API Costs
- First 1 billion quota units free per month
- Additional quota: $0.00001 per unit
- Monitor API usage in Google Cloud Console

## Maintenance Tasks

### Regular Updates
- Update dependencies monthly
- Monitor security advisories
- Update OAuth client secrets periodically

### Performance Monitoring
- Set up alerts for response times > 2s
- Monitor error rates > 1%
- Track user growth metrics

### Backup Verification
- Test backup restoration quarterly
- Verify backup integrity
- Document recovery procedures

## Rollback Strategy

### Quick Rollback
1. Deploy previous Git commit
2. Restore database from backup if needed
3. Update DNS if domain changed

### Emergency Procedures
- Have backup OAuth credentials ready
- Maintain backup database snapshots
- Document incident response process

---

For production support or issues, refer to the development team or check the troubleshooting section in the main README.
