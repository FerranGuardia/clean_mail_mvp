# CleanMail User Guide

Welcome to CleanMail! This guide will help you get started with organizing your Gmail inbox professionally. CleanMail uses smart rules to automatically categorize and manage your emails, with special focus on tracking important bills and documents.

## 📋 Table of Contents

- [Quick Start](#quick-start)
- [Getting Started](#getting-started)
- [Understanding Categories](#understanding-categories)
- [Using the Dashboard](#using-the-dashboard)
- [Managing Rules](#managing-rules)
- [Processing Emails](#processing-emails)
- [Troubleshooting](#troubleshooting)
- [Best Practices](#best-practices)

## 🚀 Quick Start

1. **Visit CleanMail**: Go to your CleanMail website
2. **Sign In**: Click "Get Started" and sign in with Google
3. **Grant Permissions**: Allow Gmail access for email organization
4. **View Dashboard**: See your email processing statistics
5. **Process Emails**: Click "Process Emails" to organize your inbox

That's it! CleanMail will automatically categorize your emails using professional patterns.

## 🔐 Getting Started

### Signing In

CleanMail uses secure Google OAuth authentication:

1. Click **"Get Started"** or **"Sign In"**
2. Select your Google account
3. Grant Gmail permissions for:
   - Reading your emails
   - Applying labels
   - Managing your inbox
4. You'll be redirected to the dashboard

### First Time Setup

After signing in, CleanMail will:

- ✅ Analyze your Gmail account
- ✅ Set up professional categorization rules
- ✅ Show your email processing dashboard
- ✅ Display activity history

## 📂 Understanding Categories

CleanMail organizes emails into professional categories:

### 🗑️ **Trash** - Items to Remove
- **Promotions & Offers**: Marketing emails, discounts, sales
- **No-Reply Emails**: Automated system messages
- **Newsletters**: Subscription content, blog posts

### 📱 **Social** - Social Media & Networking
- **Facebook Notifications**: Likes, comments, events
- **Instagram & Twitter**: Social media updates
- **LinkedIn**: Professional network notifications

### 📄 **Bills** - Important Financial Documents ⭐
- **Invoices & Receipts**: Payment confirmations
- **Billing Statements**: Monthly bills, subscriptions
- **Financial Documents**: Tax documents, statements

### 📦 **Orders** - Shopping & Purchases
- **Order Confirmations**: Purchase receipts
- **Shipping Updates**: Delivery status, tracking
- **Purchase Alerts**: Order modifications

### ⚙️ **Technical** - System & Deployment
- **Server Alerts**: System notifications
- **Deployment Updates**: Build and release notifications
- **Technical Reports**: System health, errors

## 📊 Using the Dashboard

The dashboard provides insights into your email organization:

### Key Metrics

- **Total Rules**: Active organization rules
- **Processed Today**: Emails organized in the last 24 hours
- **Bills Tracked**: Important financial documents found
- **Category Breakdown**: Distribution across categories

### Recent Activity

View your email processing history:
- Subject lines of processed emails
- Applied categories
- Processing timestamps
- Success status

### Rule Performance

See which rules are most effective:
- Rule names and descriptions
- Number of emails processed
- Success rates

## ⚙️ Managing Rules

### Built-in Rules

CleanMail comes with professional rules pre-configured:

| Category | Pattern | Example |
|----------|---------|---------|
| Bills | `factura\|invoice\|recibo` | "Factura Electrónica #123" |
| Orders | `pedido\|order\|shipped` | "Your order has shipped" |
| Trash | `oferta\|promo\|newsletter` | "50% off sale!" |
| Social | `facebook\|instagram\|linkedin` | "John liked your post" |

### Custom Rules (Future Feature)

You can create custom rules for specific needs:

1. Go to **Rules** section
2. Click **"Create Rule"**
3. Define:
   - **Name**: Descriptive rule name
   - **Match Type**: sender, subject, or content
   - **Pattern**: Text to match
   - **Action**: Tag, archive, or mark as read
   - **Priority**: Rule importance (lower = higher priority)

## 🔄 Processing Emails

### Automatic Processing

CleanMail processes emails in the background:

1. **Click "Process Emails"**
2. Choose number of emails to process (default: 50)
3. Processing happens automatically
4. View results in activity log

### What Happens During Processing

1. **Email Retrieval**: Fetches recent emails from Gmail
2. **Rule Application**: Tests each email against active rules
3. **Action Execution**: Applies matching actions (tags, archive, etc.)
4. **Logging**: Records all actions for transparency
5. **Statistics Update**: Updates dashboard metrics

### Processing Limits

- **Maximum per batch**: 50 emails
- **Gmail API limits**: 1 billion quota units/month (free)
- **Rate limiting**: Prevents quota exhaustion

## 🔍 Troubleshooting

### Common Issues

#### "Processing Failed"
**Symptoms**: Email processing stops with error
**Solutions**:
- Check Gmail API permissions
- Verify internet connection
- Try processing fewer emails at once
- Check dashboard for error details

#### "No Emails Processed"
**Symptoms**: Processing completes but no emails categorized
**Causes**:
- No matching emails found
- Rules may be too specific
- Emails already processed

#### "Login Issues"
**Symptoms**: Can't sign in with Google
**Solutions**:
- Clear browser cache
- Try different browser
- Check Google account permissions
- Verify app permissions in Google account settings

#### "Slow Processing"
**Symptoms**: Processing takes longer than expected
**Causes**:
- Large inbox
- Gmail API rate limits
- Network connectivity
- High server load

### Getting Help

1. **Check Dashboard**: Look for error messages
2. **Review Activity Log**: See processing details
3. **Contact Support**: Use feedback form or GitHub issues
4. **Community**: Check discussions and forums

## 💡 Best Practices

### Email Organization

1. **Regular Processing**: Process emails daily for best results
2. **Review Categories**: Check tagged emails to ensure accuracy
3. **Adjust Rules**: Fine-tune patterns based on your email patterns
4. **Monitor Bills**: Pay special attention to Bills category

### Gmail Integration

1. **Enable Notifications**: Get alerts for important categories
2. **Create Filters**: Use Gmail filters with CleanMail labels
3. **Archive Processed**: Set up auto-archiving for processed emails
4. **Backup Important**: Download important documents from Bills category

### Productivity Tips

1. **Morning Routine**: Start day by processing overnight emails
2. **Category Focus**: Handle Bills and Orders categories first
3. **Rule Refinement**: Adjust rules based on false positives/negatives
4. **Team Coordination**: Share processing results with colleagues

### Security & Privacy

1. **Secure Access**: Always sign out when using shared computers
2. **Permission Review**: Regularly check Google app permissions
3. **Data Awareness**: CleanMail only processes email metadata for organization
4. **Account Security**: Use strong Google account passwords and 2FA

## 📈 Advanced Usage

### Understanding Rule Priority

Rules are applied in priority order (lower numbers first):
- Priority 1: Bills detection (highest priority)
- Priority 2: Orders and shipping
- Priority 3: Social media
- Priority 4: Technical notifications
- Priority 5: Trash and promotions (lowest priority)

### Custom Gmail Filters

Create Gmail filters to work with CleanMail labels:

```
Has label: Bills → Apply label: Important, Mark as read
Has label: Trash → Archive
```

### Integration Ideas

1. **IFTTT/Zapier**: Automate actions based on CleanMail labels
2. **Calendar Integration**: Create events from order confirmations
3. **Document Management**: Export bills to cloud storage
4. **Team Collaboration**: Share processing results

## 🎯 Use Cases

### For Professionals
- **Accountants**: Track all client invoices automatically
- **Managers**: Monitor project-related communications
- **Freelancers**: Organize payment and project emails
- **Business Owners**: Keep financial documents organized

### For Individuals
- **Home Management**: Track utility bills and subscriptions
- **Shopping**: Monitor order confirmations and deliveries
- **Personal Finance**: Organize bank statements and receipts
- **Travel**: Track booking confirmations and itineraries

## 📞 Support & Feedback

### Getting Help

- **Documentation**: Check this user guide first
- **Dashboard Help**: Look for tooltips and help icons
- **Community**: Join discussions for user tips
- **Issues**: Report bugs via GitHub issues

### Providing Feedback

We welcome your feedback to improve CleanMail:

- **Feature Requests**: Suggest new capabilities
- **Bug Reports**: Help us fix issues
- **User Experience**: Share your experience
- **Performance**: Report speed or reliability issues

### Contact Information

- **Email**: Support contact (when available)
- **GitHub**: Issue tracking and feature requests
- **Community**: User discussions and tips

---

**CleanMail** - Making professional email organization simple and automatic. 🚀

*Last updated: January 2025*
