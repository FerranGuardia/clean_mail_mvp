# 🚀 CleanMail First Deployment Guide

## Welcome to Your First Deployment!

This guide will walk you through deploying CleanMail to production using Railway (backend) and Vercel (frontend). We'll use the free tiers to get you started.

---

## 📋 Prerequisites Checklist

Before we start, make sure you have:

- ✅ **GitHub Repository**: Your CleanMail code pushed to GitHub
- ✅ **Google Cloud Console**: Gmail API enabled with OAuth credentials
- ✅ **Railway Account**: Created at https://railway.app
- ✅ **Vercel Account**: Created at https://vercel.com

---

## 🎯 Step 1: Deploy Backend to Railway

### 1.1 Create Railway Project

1. Go to https://railway.app and sign in
2. Click **"New Project"**
3. Select **"Deploy from GitHub repo"**
4. Find and select your `CleanMail` repository
5. Click **"Deploy"**

Railway will automatically detect it's a Python project and start building.

### 1.2 Configure Environment Variables

1. In your Railway project dashboard, go to **"Variables"** tab
2. Add these environment variables:

```
DATABASE_URL=sqlite:///./cleanmail.db
GOOGLE_CLIENT_ID=your-google-client-id-here
GOOGLE_CLIENT_SECRET=your-google-client-secret-here
GOOGLE_REDIRECT_URI=https://your-railway-domain.up.railway.app/api/auth/callback
SECRET_KEY=your-super-secret-production-key-change-this-12345
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
DEBUG=False
API_V1_PREFIX=/api/v1
```

**⚠️ IMPORTANT:** Replace the Google OAuth values with your actual credentials from Google Cloud Console.

### 1.3 Get Your Backend URL

After deployment, Railway will give you a domain like:
`https://cleanmail-backend.up.railway.app`

**Copy this URL** - you'll need it for the frontend deployment.

---

## 🎨 Step 2: Deploy Frontend to Vercel

### 2.1 Create Vercel Project

1. Go to https://vercel.com and sign in
2. Click **"New Project"**
3. Import your GitHub repository
4. Configure the project:
   - **Framework Preset**: Vite
   - **Root Directory**: `frontend`
   - **Build Command**: `npm run build`
   - **Output Directory**: `dist`

### 2.2 Set Environment Variables

1. In Vercel project settings, go to **"Environment Variables"**
2. Add this variable:

```
VITE_API_URL=https://your-railway-domain.up.railway.app
```

**Replace with your actual Railway backend URL.**

### 2.3 Deploy

1. Click **"Deploy"**
2. Wait for the build to complete
3. Vercel will give you a domain like: `https://cleanmail.vercel.app`

---

## 🔧 Step 3: Update Google OAuth (Production)

### 3.1 Update Redirect URI

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Navigate to **"APIs & Services"** → **"Credentials"**
3. Edit your OAuth 2.0 Client ID
4. Add your production redirect URI:
   ```
   https://your-railway-domain.up.railway.app/api/auth/callback
   ```

### 3.2 Update Environment Variables

In Railway, update the `GOOGLE_REDIRECT_URI` with your actual Railway domain.

---

## 🧪 Step 4: Test Your Deployment

### 4.1 Test Backend API

1. Visit: `https://your-railway-domain.up.railway.app/health`
2. You should see: `{"status": "healthy"}`

3. Visit: `https://your-railway-domain.up.railway.app/docs`
4. You should see the FastAPI documentation

### 4.2 Test Frontend

1. Visit: `https://your-vercel-domain.vercel.app`
2. You should see the CleanMail landing page

3. Try the login flow:
   - Click "Get Started" or "Sign In"
   - You should be redirected to Google OAuth
   - After login, you should return to the dashboard

---

## 🔍 Troubleshooting Common Issues

### Issue: Backend Build Fails
**Solution:** Check Railway logs. Make sure all dependencies are in `requirements.txt`.

### Issue: Frontend Build Fails
**Solution:** Check Vercel logs. Make sure `npm install` works locally.

### Issue: Google OAuth Not Working
**Solution:**
- Check that redirect URI exactly matches in Google Cloud Console
- Verify environment variables are set correctly in Railway
- Make sure your Google account is added as a test user

### Issue: Frontend Can't Connect to Backend
**Solution:** Check that `VITE_API_URL` in Vercel matches your Railway domain exactly.

---

## 💰 Cost Breakdown (Free Tiers)

- **Railway**: Free tier (512MB RAM, 1GB disk)
- **Vercel**: Free tier (unlimited deployments)
- **Google Cloud**: Free tier (1B Gmail API calls/month)
- **Domain**: Free Vercel subdomain

**Total Cost: $0/month** 🎉

---

## 🚀 Next Steps After Deployment

### Immediate Actions:
1. **Share your app** with friends for feedback
2. **Test the email processing** with real Gmail accounts
3. **Collect user feedback** and note any issues

### Growth Actions:
1. **Add analytics** (Google Analytics in Vercel)
2. **Set up monitoring** (Railway provides basic metrics)
3. **Create a Product Hunt page** for launch
4. **Write a blog post** about your journey

### Technical Improvements:
1. **Add error logging** (Sentry integration)
2. **Implement user feedback** collection
3. **Add loading states** and better UX
4. **Set up automated backups**

---

## 📞 Need Help?

If something doesn't work:

1. **Check the logs:**
   - Railway: Project dashboard → "Logs" tab
   - Vercel: Project dashboard → "Functions" → "Logs"

2. **Verify environment variables** are set correctly

3. **Test locally first** to make sure everything works

4. **Check the detailed deployment docs** in `docs/DEPLOYMENT.md`

---

## 🎉 Congratulations!

You've successfully deployed your first SaaS application! CleanMail is now live and ready for users.

**Share your deployment:**
- Post on Twitter/LinkedIn: "Just deployed my first SaaS app! 🚀"
- Show it to friends and get feedback
- Consider submitting to Product Hunt

**Next milestone:** Get your first 10 users! 🎯

---

*This guide was created specifically for CleanMail's first deployment. For future deployments, refer to the comprehensive docs in `docs/DEPLOYMENT.md`.*
