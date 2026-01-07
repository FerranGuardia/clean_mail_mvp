# CleanMail Documentation

Welcome to the CleanMail documentation! This directory contains comprehensive documentation for the CleanMail project - a professional Gmail inbox cleaner with rule-based email organization.

## 📚 Documentation Overview

CleanMail is a web application that helps professionals maintain clean Gmail inboxes by automatically organizing emails using bilingual rules (Spanish and English). It specializes in tracking important documents like bills and invoices while removing promotional content.

## 🚀 Quick Links

| Document | Description |
|----------|-------------|
| [**Main README**](../README.md) | Project overview, features, and quick start guide |
| [**API Reference**](API_REFERENCE.md) | Complete API documentation for developers |
| [**Development Guide**](DEVELOPMENT.md) | Setup, development workflow, and coding standards |
| [**Deployment Guide**](DEPLOYMENT.md) | Production deployment instructions |
| [**Contributing Guide**](../CONTRIBUTING.md) | How to contribute to the project |
| [**Changelog**](../CHANGELOG.md) | Version history and release notes |

## 📖 Documentation by Audience

### 👥 For Users

If you're looking to use CleanMail:

1. **Getting Started**: Read the [Main README](../README.md) for project overview
2. **Setup**: Follow the installation instructions in the README
3. **Usage**: See the Features section and How It Works in the README

### 👨‍💻 For Developers

If you're contributing to CleanMail:

1. **Setup**: Follow the [Development Guide](DEVELOPMENT.md)
2. **Contributing**: Read the [Contributing Guide](../CONTRIBUTING.md)
3. **API**: Check the [API Reference](API_REFERENCE.md)
4. **Deployment**: See the [Deployment Guide](DEPLOYMENT.md)

### 🏗️ For DevOps/Deployers

If you're deploying CleanMail:

1. **Deployment**: Start with the [Deployment Guide](DEPLOYMENT.md)
2. **Configuration**: Check environment variables in the guides
3. **Troubleshooting**: See troubleshooting sections in deployment docs

## 🏛️ Architecture Overview

### Backend (FastAPI + Python)
- **Framework**: FastAPI for high-performance async API
- **Database**: SQLite (development) / PostgreSQL (production)
- **Authentication**: JWT tokens with Google OAuth 2.0
- **Gmail Integration**: Google API Python Client

### Frontend (React + Vite)
- **Framework**: React 18 with modern hooks
- **Build Tool**: Vite for fast development
- **Styling**: Tailwind CSS for responsive design
- **State Management**: React hooks and context

### Key Components
- **Rule Engine**: Pattern matching for email categorization
- **OAuth Service**: Secure Google authentication
- **Gmail Service**: Email processing and labeling
- **Dashboard**: Statistics and activity monitoring

## 📋 Features

### Core Features
- ✅ Google OAuth secure authentication
- ✅ Bilingual rule patterns (Spanish + English)
- ✅ Professional email categories (Bills, Orders, Trash, Social, Technical)
- ✅ Automatic Gmail labeling
- ✅ Professional dashboard with statistics
- ✅ Activity logging and audit trail

### Professional Categories
- 🗑️ **Trash**: Promotions, no-reply emails, newsletters
- 📱 **Social**: Facebook, Instagram, Twitter, LinkedIn
- 📄 **Bills**: Invoices, receipts, payment confirmations
- 📦 **Orders**: Purchase orders, shipping updates
- ⚙️ **Technical**: Deployment alerts, system notifications

## 🛠️ Development Tools

### Backend Tools
- **Testing**: pytest for unit testing
- **Code Quality**: Black (formatting), isort (imports), flake8 (linting)
- **Documentation**: FastAPI automatic docs, Google-style docstrings

### Frontend Tools
- **Build**: Vite for fast development and building
- **Styling**: Tailwind CSS with PostCSS
- **Code Quality**: ESLint for JavaScript linting

### Development Scripts
- `setup.py`: Automated development environment setup
- `start-dev.py`: Start both backend and frontend servers
- `check-deployment-ready.py`: Pre-deployment checklist

## 🚀 Deployment Options

### Recommended Stack
- **Backend**: Railway (easy Python deployment)
- **Frontend**: Vercel (optimal React deployment)
- **Database**: PostgreSQL (Railway provides automatically)

### Alternative Options
- **Backend**: Heroku, DigitalOcean, AWS
- **Frontend**: Netlify, GitHub Pages
- **Database**: Any PostgreSQL provider

## 🔒 Security

- OAuth 2.0 secure authentication
- JWT token management
- HTTPS required for production
- Input validation and sanitization
- Secure credential storage
- Minimal data collection

## 📊 Roadmap

### Phase 1 ✅ (Current)
- MVP with core rule-based processing
- Professional email categorization
- Basic dashboard and logging

### Phase 2 🔄 (Next)
- Enhanced customization interface
- Advanced rule patterns
- Performance optimizations

### Phase 3 🚀 (Future)
- AI-powered email classification
- Multi-account support
- Advanced analytics

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guide](../CONTRIBUTING.md) for:

- Development setup instructions
- Coding standards and best practices
- Pull request guidelines
- Testing requirements
- Documentation standards

### Ways to Contribute
- 🐛 Bug fixes and issue reports
- ✨ New features and enhancements
- 📚 Documentation improvements
- 🧪 Additional test coverage
- 🎨 UI/UX improvements

## 📞 Support

### Getting Help
1. **Documentation**: Check this docs folder first
2. **Issues**: Search existing GitHub issues
3. **Discussions**: Use GitHub Discussions for questions
4. **Community**: Join our community discussions

### Common Issues
- OAuth configuration problems
- Gmail API quota issues
- Deployment configuration
- Database migration issues

## 📈 Project Status

- **Version**: 1.0.0
- **Status**: MVP Ready for Production
- **License**: MIT
- **Python Version**: 3.8+
- **Node Version**: 16+

## 🔗 External Links

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [React Documentation](https://react.dev/)
- [Google Gmail API](https://developers.google.com/gmail/api)
- [Railway Documentation](https://docs.railway.app/)
- [Vercel Documentation](https://vercel.com/docs)

---

**CleanMail** - Making email organization simple and effective for professionals worldwide. 🚀

For questions or feedback, please [open an issue](https://github.com/yourusername/cleanmail/issues) or start a [discussion](https://github.com/yourusername/cleanmail/discussions).
