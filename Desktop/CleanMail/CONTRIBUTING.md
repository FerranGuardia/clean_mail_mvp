# Contributing to CleanMail

Thank you for your interest in contributing to CleanMail! We welcome contributions from developers of all skill levels. This document provides guidelines and information for contributors.

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Workflow](#development-workflow)
- [Coding Standards](#coding-standards)
- [Testing](#testing)
- [Submitting Changes](#submitting-changes)
- [Reporting Issues](#reporting-issues)
- [Documentation](#documentation)

## 🤝 Code of Conduct

This project follows a code of conduct to ensure a welcoming environment for all contributors. By participating, you agree to:

- Be respectful and inclusive
- Focus on constructive feedback
- Accept responsibility for mistakes
- Show empathy towards other contributors
- Help create a positive community

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- Node.js 16 or higher
- Git
- Google Cloud Console account (for Gmail API development)

### Setup Development Environment

1. **Fork and Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/cleanmail.git
   cd cleanmail
   ```

2. **Set up the Development Environment**
   ```bash
   python setup.py
   ```

3. **Configure Google OAuth**
   - Go to [Google Cloud Console](https://console.cloud.google.com/)
   - Create a project or select existing one
   - Enable Gmail API
   - Create OAuth 2.0 credentials
   - Set redirect URI to `http://localhost:8000/api/auth/callback`
   - Update `backend/.env` with your credentials

4. **Start Development Servers**
   ```bash
   python start-dev.py
   ```

## 🔄 Development Workflow

### Branch Strategy

We use a simple branching strategy:

- `main`: Production-ready code
- `feature/*`: New features (e.g., `feature/user-dashboard`)
- `bugfix/*`: Bug fixes (e.g., `bugfix/oauth-redirect`)
- `hotfix/*`: Urgent production fixes

### Making Changes

1. **Create a Feature Branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make Your Changes**
   - Write clean, well-documented code
   - Follow the coding standards below
   - Add tests for new functionality
   - Update documentation as needed

3. **Test Your Changes**
   ```bash
   # Backend tests
   cd backend && python -m pytest

   # Frontend tests (when implemented)
   cd frontend && npm test

   # Manual testing
   python start-dev.py
   ```

4. **Commit Your Changes**
   ```bash
   git add .
   git commit -m "feat: add user dashboard component

   - Add new dashboard page
   - Implement statistics display
   - Add responsive design

   Closes #123"
   ```

## 📝 Coding Standards

### Python (Backend)

- **Style**: Follow PEP 8
- **Formatting**: Use Black formatter
- **Imports**: Use isort for import sorting
- **Docstrings**: Use Google-style docstrings
- **Type Hints**: Add type hints where possible

```python
"""Example of proper Python code style."""

from typing import Optional
import fastapi
from app.services import user_service

def get_user(user_id: int) -> Optional[dict]:
    """Retrieve user information by ID.

    Args:
        user_id: The unique identifier for the user.

    Returns:
        User data as dictionary or None if not found.
    """
    return user_service.get_user_by_id(user_id)
```

### JavaScript/React (Frontend)

- **Style**: Use ESLint configuration
- **Formatting**: Use Prettier (when configured)
- **Components**: Use functional components with hooks
- **Naming**: Use PascalCase for components, camelCase for functions
- **Imports**: Group imports (React, third-party, local)

```javascript
// Good component example
import React, { useState, useEffect } from 'react';
import { api } from '../services/api';

const UserDashboard = () => {
  const [user, setUser] = useState(null);

  useEffect(() => {
    const fetchUser = async () => {
      try {
        const userData = await api.getCurrentUser();
        setUser(userData);
      } catch (error) {
        console.error('Failed to fetch user:', error);
      }
    };

    fetchUser();
  }, []);

  return (
    <div className="dashboard">
      {user && <h1>Welcome, {user.name}!</h1>}
    </div>
  );
};

export default UserDashboard;
```

### Commit Messages

Follow conventional commit format:

```
type(scope): description

[optional body]

[optional footer]
```

**Types:**
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting, etc.)
- `refactor`: Code refactoring
- `test`: Adding or updating tests
- `chore`: Maintenance tasks

**Examples:**
```
feat(auth): add Google OAuth integration
fix(api): resolve user token refresh issue
docs(readme): update installation instructions
```

## 🧪 Testing

### Backend Testing

```bash
cd backend

# Run all tests
pytest

# Run specific test file
pytest tests/test_auth.py

# Run with coverage
pytest --cov=app --cov-report=html

# Run tests in watch mode (if pytest-watch installed)
ptw
```

### Frontend Testing

```bash
cd frontend

# Run tests
npm test

# Run tests in watch mode
npm run test:watch

# Run tests with coverage
npm run test:coverage
```

### Test Structure

```
backend/tests/
├── __init__.py
├── conftest.py          # Pytest fixtures
├── test_auth.py         # Authentication tests
├── test_rules.py        # Rule engine tests
├── test_emails.py       # Email processing tests
└── test_dashboard.py    # Dashboard tests
```

## 📤 Submitting Changes

### Pull Request Process

1. **Ensure Your Branch is Up to Date**
   ```bash
   git checkout main
   git pull origin main
   git checkout your-feature-branch
   git rebase main
   ```

2. **Create a Pull Request**
   - Go to GitHub and create a PR from your branch to `main`
   - Fill out the PR template with:
     - Clear title describing the changes
     - Detailed description of what was implemented
     - Screenshots/videos for UI changes
     - Link to related issues

3. **Code Review**
   - Address review feedback
   - Make requested changes
   - Ensure CI checks pass

4. **Merge**
   - Once approved, your PR will be merged by a maintainer
   - Delete your feature branch after merging

### PR Checklist

- [ ] Code follows project coding standards
- [ ] Tests added/updated and passing
- [ ] Documentation updated if needed
- [ ] Commit messages follow conventional format
- [ ] PR description is clear and detailed
- [ ] CI checks are passing
- [ ] Reviewed by at least one maintainer

## 🐛 Reporting Issues

### Bug Reports

When reporting bugs, please include:

1. **Clear Title**: Summarize the issue
2. **Description**: Detailed description of the problem
3. **Steps to Reproduce**: Step-by-step instructions
4. **Expected Behavior**: What should happen
5. **Actual Behavior**: What actually happens
6. **Environment**: OS, browser, Python/Node versions
7. **Screenshots**: If applicable
8. **Additional Context**: Any other relevant information

### Feature Requests

For feature requests, please include:

1. **Clear Title**: Feature name or summary
2. **Description**: Detailed description of the feature
3. **Use Case**: Why is this feature needed?
4. **Proposed Solution**: How should it work?
5. **Alternatives**: Other approaches considered
6. **Additional Context**: Mockups, examples, etc.

## 📚 Documentation

### Types of Documentation

- **Code Documentation**: Docstrings, comments, READMEs
- **User Documentation**: User guides, tutorials
- **API Documentation**: Endpoint documentation, examples
- **Deployment Documentation**: Setup and deployment guides

### Documentation Standards

- Use Markdown for all documentation
- Keep language clear and concise
- Include code examples where helpful
- Update documentation with code changes
- Test all instructions and examples

### Where to Find Documentation

- `README.md`: Project overview and setup
- `docs/`: Detailed documentation
- `backend/README.md`: Backend-specific setup
- `frontend/README.md`: Frontend-specific setup
- Code comments and docstrings

## 🎯 Areas for Contribution

### High Priority

- [ ] Unit tests for backend services
- [ ] Frontend component tests
- [ ] Performance optimization
- [ ] Error handling improvements
- [ ] User experience enhancements

### Medium Priority

- [ ] API documentation improvements
- [ ] Code refactoring
- [ ] Additional rule patterns
- [ ] Mobile responsiveness
- [ ] Internationalization

### Future Ideas

- [ ] AI-powered email classification
- [ ] Multi-account support
- [ ] Advanced analytics
- [ ] Integration with other email providers
- [ ] Mobile app development

## 🙏 Recognition

Contributors will be recognized in:
- Repository contributors list
- Changelog entries
- Release notes
- Project documentation

Thank you for contributing to CleanMail! Your efforts help make email organization simple and effective for users worldwide. 🚀
