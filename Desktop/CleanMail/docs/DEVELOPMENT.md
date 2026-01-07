# CleanMail Development Guide

## Getting Started

### Automated Setup
Run the setup script to configure your development environment:
```bash
python setup.py
```

### Manual Setup
If you prefer manual setup, follow these steps:

1. **Backend Setup:**
   ```bash
   python -m venv venv
   venv\Scripts\activate  # Windows
   pip install -r backend/requirements.txt
   ```

2. **Frontend Setup:**
   ```bash
   cd frontend
   npm install
   ```

3. **Google OAuth Setup:**
   - Visit [Google Cloud Console](https://console.cloud.google.com/)
   - Create/select a project
   - Enable Gmail API
   - Create OAuth 2.0 credentials
   - Configure authorized redirect URI: `http://localhost:8000/api/auth/callback`

4. **Environment Configuration:**
   Copy `.env.example` to `.env` and fill in your credentials.

## Development Workflow

### Running the Application

1. **Start Backend:**
   ```bash
   cd backend
   uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
   ```

2. **Start Frontend:**
   ```bash
   cd frontend
   npm run dev
   ```

3. **Access Application:**
   - Frontend: http://localhost:5173
   - Backend API: http://localhost:8000
   - API Docs: http://localhost:8000/docs

### Code Quality

#### Backend
```bash
# Format code
black .
isort .

# Run tests (when implemented)
pytest
```

#### Frontend
```bash
# Lint code
npm run lint

# Format code (when configured)
npm run format
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
