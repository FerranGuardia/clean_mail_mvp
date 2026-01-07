# CleanMail - Professional Gmail Inbox Cleaner

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104.1-009688.svg)](https://fastapi.tiangolo.com/)
[![React](https://img.shields.io/badge/React-18.2.0-61DAFB.svg)](https://reactjs.org/)

Una herramienta web que ayuda a mantener tu bandeja de Gmail profesional mediante reglas basadas en patrones. Especializada en español e inglés para filtrar correos no deseados y rastrear facturas importantes.

**Enfoque Principal**: Mantener el Gmail profesional eliminando "trash/publy" (promociones, social, no-reply) y asegurando que todas las facturas, pedidos y documentos importantes estén perfectamente organizados y etiquetados.

**Objetivo Principal**: Nunca perder una factura importante y mantener la bandeja de entrada limpia para uso profesional.

## 🚀 Quick Start

```bash
# Clone the repository
git clone https://github.com/yourusername/cleanmail.git
cd cleanmail

# Setup development environment
python setup.py

# Configure Google OAuth (see setup instructions below)
# Then start development servers
python start-dev.py
```

**View the application:**
- Landing Page: http://localhost:5173
- API Documentation: http://localhost:8000/docs

## 🎨 **Website Design**

CleanMail features a clean, professional SaaS website design inspired by modern productivity tools:

### **Landing Page Features**
- **Hero Section**: Clear value proposition focused on bill tracking
- **Features Grid**: 6 key professional features with icons
- **How It Works**: 3-step process visualization
- **Professional Footer**: Company info and links

### **Design Principles**
- **Clean & Minimal**: White background with subtle gradients
- **Professional Typography**: Inter font family
- **Blue Color Scheme**: Trustworthy and professional
- **Responsive Design**: Works on all devices
- **Fast Loading**: Optimized for performance

### **Key Sections**
1. **Navigation**: Clean header with logo and CTA
2. **Hero**: Compelling headline + benefits + CTA
3. **Features**: Detailed feature explanations
4. **Process**: Simple 3-step workflow
5. **Footer**: Professional company information

## 🚀 Features

- **Google OAuth Integration**: Login seguro con cuentas de Google
- **Reglas Bilingües**: Patrones pre-configurados para español e inglés
- **Categorías Profesionales**:
  - 🗑️ **Trash**: Promociones, ofertas, no-reply
  - 📱 **Social**: Facebook, Instagram, Twitter, LinkedIn
  - 📄 **Bills**: Facturas, recibos, comprobantes de pago
  - 📦 **Orders**: Pedidos, envíos, confirmaciones
  - ⚙️ **Technical**: Despliegues, alertas técnicas
- **Dashboard Profesional**: Monitorea tu actividad y facturas rastreadas
- **Gmail API Integration**: Integración directa con Gmail para etiquetado automático

## 🏗️ Architecture

### Backend (FastAPI + Python)
- **Framework**: FastAPI for high-performance async API
- **Database**: SQLite (MVP) → PostgreSQL (production)
- **Authentication**: JWT tokens with Google OAuth
- **Gmail Integration**: Google API Python Client

### Frontend (React + Vite)
- **Framework**: React 18 with hooks
- **Build Tool**: Vite for fast development
- **Styling**: Tailwind CSS for modern UI
- **Routing**: React Router for SPA navigation

## 📁 Project Structure

```
cleanmail/
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py              # FastAPI application
│   │   ├── config.py            # Configuration settings
│   │   ├── database.py          # Database connection
│   │   ├── models/              # SQLAlchemy models
│   │   │   ├── user.py
│   │   │   ├── rule.py
│   │   │   └── email_log.py
│   │   ├── schemas/             # Pydantic schemas
│   │   │   ├── user.py
│   │   │   ├── rule.py
│   │   │   └── email_log.py
│   │   ├── routers/             # API endpoints
│   │   │   ├── auth.py          # OAuth & authentication
│   │   │   ├── rules.py         # Rule CRUD operations
│   │   │   ├── emails.py        # Email processing
│   │   │   └── dashboard.py     # Statistics & logs
│   │   ├── services/            # Business logic
│   │   │   ├── auth_service.py  # JWT token management
│   │   │   ├── gmail_service.py # Gmail API wrapper
│   │   │   └── rule_engine.py   # Rule matching logic
│   │   └── utils/               # Helper functions
│   ├── scripts/                 # Utility scripts
│   │   └── init_rules.py        # Initialize built-in rules
│   ├── tests/                   # Unit tests
│   ├── cleanmail.db             # SQLite database (development)
│   ├── requirements.txt         # Python dependencies
│   ├── runtime.txt              # Python version for deployment
│   ├── Procfile                 # Heroku deployment config
│   └── railway.json             # Railway deployment config
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── components/          # React components
│   │   │   └── Navbar.jsx
│   │   ├── pages/               # Page components
│   │   │   ├── Login.jsx
│   │   │   ├── Dashboard.jsx
│   │   │   ├── Rules.jsx
│   │   │   └── Process.jsx
│   │   ├── services/            # API client
│   │   │   └── api.js
│   │   ├── hooks/               # Custom React hooks
│   │   ├── utils/               # Helper functions
│   │   └── App.jsx
│   ├── package.json
│   ├── vite.config.js
│   ├── tailwind.config.js
│   └── postcss.config.js
├── docs/                        # Documentation
└── README.md
```

## 🛠️ Setup & Installation

### Prerequisites

- Python 3.8+
- Node.js 16+
- Google Cloud Console account (for Gmail API)

### Backend Setup

1. **Create virtual environment:**
   ```bash
   python -m venv venv
   venv\Scripts\activate  # Windows
   # source venv/bin/activate  # macOS/Linux
   ```

2. **Install dependencies:**
   ```bash
   cd backend
   pip install -r requirements.txt
   ```

3. **Set up Google OAuth:**
   - Go to [Google Cloud Console](https://console.cloud.google.com/)
   - Create a new project or select existing one
   - Enable Gmail API
   - Create OAuth 2.0 credentials
   - Add authorized redirect URI: `http://localhost:8000/api/auth/callback`

4. **Configure environment variables:**
   Create a `.env` file in the backend directory:
   ```env
   DATABASE_URL=sqlite:///./cleanmail.db
   GOOGLE_CLIENT_ID=your-google-client-id
   GOOGLE_CLIENT_SECRET=your-google-client-secret
   GOOGLE_REDIRECT_URI=http://localhost:8000/api/auth/callback
   SECRET_KEY=your-secret-key-change-in-production
   DEBUG=True
   ```

5. **Initialize database:**
   ```bash
   python -c "from app.database import create_tables; create_tables()"
   ```

6. **Run the development servers:**
   ```bash
   python start-dev.py
   ```
   Or manually:
   ```bash
   # Backend (Terminal 1)
   cd backend && uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

   # Frontend (Terminal 2)
   cd frontend && npm run dev
   ```

### Frontend Setup

1. **Install dependencies:**
   ```bash
   cd frontend
   npm install
   ```

2. **Start development server:**
   ```bash
   npm run dev
   ```

## 🔧 API Endpoints

### Authentication
- `GET /api/auth/google` - Initiate Google OAuth
- `GET /api/auth/callback` - OAuth callback
- `GET /api/auth/me` - Get current user

### Rules
- `GET /api/rules` - List user rules
- `POST /api/rules` - Create rule
- `PUT /api/rules/{id}` - Update rule
- `DELETE /api/rules/{id}` - Delete rule

### Emails
- `GET /api/emails/preview` - Preview emails
- `POST /api/emails/process` - Process emails with rules
- `GET /api/emails/patterns` - Get built-in patterns

### Dashboard
- `GET /api/dashboard/stats` - Get statistics
- `GET /api/dashboard/activity` - Get activity log

## 📊 Data Models

### User
- Google account integration
- OAuth token management
- Profile information

### Rule
- Pattern matching (sender, subject, body, regex)
- Action types (tag, archive, mark_read, move)
- Priority system for rule evaluation

### EmailLog
- Processing history
- Success/failure tracking
- Action audit trail

## 🚀 Deployment

### Backend (Railway)
1. Connect your GitHub repository
2. Set environment variables
3. Deploy automatically

### Frontend (Vercel)
1. Connect GitHub repository
2. Configure build settings
3. Set API base URL environment variable

## 🧪 Development

### Running Tests
```bash
# Backend tests
cd backend
pytest

# Frontend tests (when implemented)
cd frontend
npm test
```

### Code Quality
```bash
# Backend formatting
black .
isort .

# Frontend linting
npm run lint
```

## 🔒 Security

- JWT tokens for API authentication
- Google OAuth 2.0 for user login
- HTTPS required for production
- Secure token storage
- Input validation and sanitization

## 📈 Roadmap

### Phase 1 - MVP ✅
- Motor de reglas bilingüe (español + inglés)
- Categorías profesionales para facturas y pedidos
- Integración Gmail API
- Dashboard profesional
- Autenticación OAuth

### Phase 2 - Enhanced Professional Features
- Interfaz completa de procesamiento
- Reglas personalizadas avanzadas
- Exportación de facturas
- Notificaciones de facturas importantes
- Estadísticas detalladas de gastos

### Phase 3 - AI Integration (Futuro)
- Reconocimiento inteligente de facturas
- Categorización automática avanzada
- Alertas de gastos inusuales
- Sistema híbrido AI + reglas

### Phase 4 - Enterprise Features
- Soporte multi-cuenta
- Integración con sistemas contables
- Reportes financieros automatizados
- API para integraciones empresariales

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Google Gmail API for email integration
- FastAPI for the robust backend framework
- React ecosystem for the modern frontend
- Open source community for inspiration

---

**CleanMail** - Making email organization simple and effective.
