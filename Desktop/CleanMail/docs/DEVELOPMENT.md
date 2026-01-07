# CleanMail Development Guide

## Getting Started

### Prerequisites

- **Python 3.8+**: Required for FastAPI backend
- **Node.js 16+**: Required for React frontend
- **Git**: For version control
- **Google Cloud Account**: For Gmail API access

### Automated Setup

The easiest way to get started is using the automated setup script:

```bash
# Clone the repository
git clone https://github.com/yourusername/cleanmail.git
cd cleanmail

# Run automated setup
python setup.py
```

The setup script will:
- Create Python virtual environment
- Install all dependencies
- Set up basic configuration
- Initialize SQLite database
- Create environment variables template

### Manual Setup

If you prefer manual setup:

1. **Clone Repository:**
   ```bash
   git clone https://github.com/yourusername/cleanmail.git
   cd cleanmail
   ```

2. **Backend Setup:**
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # macOS/Linux
   source venv/bin/activate

   pip install -r backend/requirements.txt
   ```

3. **Frontend Setup:**
   ```bash
   cd frontend
   npm install
   cd ..
   ```

4. **Google OAuth Setup:**
   - Visit [Google Cloud Console](https://console.cloud.google.com/)
   - Create/select a project
   - Enable Gmail API
   - Create OAuth 2.0 credentials
   - Set redirect URI: `http://localhost:8000/api/auth/callback`

5. **Environment Configuration:**
   Create `backend/.env` with your credentials (see setup script output)

## Development Workflow

### Running the Application

#### Option 1: Automated Development Server
```bash
python start-dev.py
```
This starts both backend and frontend servers simultaneously.

#### Option 2: Manual Server Start

**Terminal 1 - Backend:**
```bash
cd backend
# Activate virtual environment if not using automated setup
venv\Scripts\activate  # Windows
source venv/bin/activate  # macOS/Linux

uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

**Terminal 2 - Frontend:**
```bash
cd frontend
npm run dev
```

### Accessing the Application

- **Landing Page**: http://localhost:5173
- **App Dashboard**: http://localhost:5173/app/dashboard (after login)
- **Backend API**: http://localhost:8000
- **API Documentation**: http://localhost:8000/docs
- **API Alternative Docs**: http://localhost:8000/redoc

### Code Quality

#### Backend
```bash
# Format code with Black
black backend/

# Sort imports with isort
isort backend/

# Run tests
pytest backend/tests/

# Run tests with coverage
pytest --cov=backend/app --cov-report=html

# Type checking (future)
mypy backend/app/
```

#### Frontend
```bash
# Lint code
npm run lint

# Format code
npm run format

# Type checking (future)
npm run type-check

# Run tests
npm test

# Build for production
npm run build
```

### Development Tools

#### VS Code Extensions (Recommended)
- Python (Microsoft)
- Pylance (Microsoft)
- Black Formatter (Microsoft)
- isort (Microsoft)
- Prettier (Prettier)
- ESLint (Microsoft)
- Auto Rename Tag (Jun Han)
- Tailwind CSS IntelliSense (Tailwind Labs)

#### Pre-commit Hooks (Future)
Consider setting up pre-commit hooks for automatic code quality:
```bash
pip install pre-commit
pre-commit install
```

### Environment Management

#### Python Virtual Environment
```bash
# Create virtual environment
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (macOS/Linux)
source venv/bin/activate

# Deactivate
deactivate
```

#### Node Version Management
Consider using nvm for Node.js version management:
```bash
# Install nvm (Windows)
choco install nvm

# Install and use Node 18
nvm install 18
nvm use 18
```

## Architecture Overview

### Backend Structure
- **FastAPI App**: Main application in `app/main.py`
- **Routers**: API endpoints organized by feature
- **Services**: Business logic and external integrations
- **Models**: Database schemas with SQLAlchemy
- **Schemas**: Pydantic models for validation

### Frontend Structure
- **React App**: Component-based UI with hooks
- **Pages**: Route-based page components
- **Services**: API client and external integrations
- **Components**: Reusable UI components

### Modern Development Practices

#### API Testing Tools
```bash
# HTTPie for command-line API testing
pip install httpie
http GET http://localhost:8000/health
http POST http://localhost:8000/api/auth/me Authorization:"Bearer YOUR_TOKEN"

# Or use the interactive API docs at http://localhost:8000/docs
```

#### Debugging Techniques

**Backend Debugging:**
```python
# Add debug prints
print(f"Debug: user_id={user_id}, rule_count={len(rules)}")

# Use Python debugger
import pdb; pdb.set_trace()

# Structured logging
import logging
logging.basicConfig(level=logging.DEBUG)
logger.info("Processing emails for user %s", user_id)
```

**Frontend Debugging:**
- React Developer Tools browser extension
- Browser dev tools for network inspection
- `console.log()` for quick debugging
- Check React component state with DevTools

#### Performance Monitoring

**Backend:**
- Use `/health` endpoint for basic monitoring
- Monitor API response times
- Check database query performance with SQLAlchemy logging

**Frontend:**
- Browser dev tools performance tab
- Bundle analyzer: `npm run build && npx vite-bundle-analyzer dist/assets/*.js`
- React DevTools Profiler for component performance

## Database Management

### SQLite (Development)
The MVP uses SQLite for simplicity. Database file: `backend/cleanmail.db`

### Schema Changes
When models change, update the database:
```python
from app.database import create_tables
create_tables()
```

### Future Migration to PostgreSQL
For production, we'll use PostgreSQL with Alembic for migrations.

## API Design Principles

### RESTful Endpoints
- Use HTTP methods appropriately (GET, POST, PUT, DELETE)
- Resource-based URLs
- Consistent response formats

### Authentication
- JWT tokens for API access
- Google OAuth for user login
- Token refresh handling

### Error Handling
- Consistent error response format
- Appropriate HTTP status codes
- Detailed error messages for debugging

## Testing Strategy

### Backend Tests
```python
# tests/test_auth.py
def test_google_oauth_flow():
    # Test OAuth integration

# tests/test_rule_engine.py
def test_rule_matching():
    # Test rule evaluation logic
```

### Frontend Tests
```javascript
// Component tests
describe('Login Component', () => {
  it('renders login button', () => {
    // Test component rendering
  })
})
```

## Deployment

### Development
- SQLite database
- Local file storage
- Debug mode enabled

### Production Checklist
- [ ] PostgreSQL database
- [ ] Environment variables configured
- [ ] HTTPS enabled
- [ ] CORS configured
- [ ] Logging configured
- [ ] Monitoring set up

### Docker Support (Future)
```dockerfile
# backend/Dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

## Security Considerations

### OAuth Implementation
- Secure state parameter handling
- Token storage and refresh
- Scope limitations

### API Security
- Input validation with Pydantic
- SQL injection prevention
- Rate limiting (future)

### Data Privacy
- Minimal data collection
- User consent for Gmail access
- Secure token handling

## Performance Optimization

### Backend
- Async operations with FastAPI
- Database connection pooling
- Caching for frequent queries

### Frontend
- Code splitting with Vite
- Lazy loading for routes
- Optimized bundle size

## Monitoring & Logging

### Application Logs
```python
import logging
logger = logging.getLogger(__name__)
logger.info("Processing emails for user %s", user_id)
```

### Error Tracking
- Sentry integration (future)
- Structured logging
- Error aggregation

## Contributing

### Code Style
- **Python**: Black formatting, Google docstrings
- **JavaScript**: ESLint configuration, descriptive comments
- **Commits**: Conventional commit format

### Pull Request Process
1. Create feature branch from `main`
2. Implement changes with tests
3. Update documentation
4. Submit PR with description
5. Code review and approval
6. Merge to main

### Branch Strategy
- `main`: Production-ready code
- `feature/*`: New features
- `bugfix/*`: Bug fixes
- `hotfix/*`: Urgent production fixes

## Troubleshooting

### Common Issues

**Backend won't start:**
- Check virtual environment activation
- Verify all dependencies installed
- Check `.env` configuration

**Frontend build fails:**
- Clear `node_modules` and reinstall
- Check Node.js version compatibility
- Verify environment variables

**OAuth not working:**
- Verify Google Cloud Console configuration
- Check redirect URI matches exactly
- Ensure Gmail API is enabled

**Database errors:**
- Check SQLite file permissions
- Verify schema matches models
- Check foreign key constraints

### Debug Mode
Enable debug logging:
```bash
# Backend
DEBUG=True python -m uvicorn app.main:app --reload

# Frontend
npm run dev -- --mode development
```

## Resources

### Documentation
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [React Documentation](https://react.dev/)
- [Google Gmail API](https://developers.google.com/gmail/api)
- [Tailwind CSS](https://tailwindcss.com/)

### Tools
- [Postman](https://www.postman.com/) - API testing
- [SQLite Browser](https://sqlitebrowser.org/) - Database inspection
- [React DevTools](https://react.dev/learn/react-developer-tools) - Component debugging
