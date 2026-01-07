# 

# **📘 PROJECT DOCUMENT — InboxCleaner MVP**

# **1\. Project Overview**

**Working Title:** InboxCleaner MVP

**Description:**

Herramienta web que mantiene tu Gmail profesional mediante reglas bilingües (español + inglés). Enfocada en eliminar correos "trash/publy" y asegurar que todas las facturas importantes estén perfectamente organizadas.

**Target Users:**

Profesionales que necesitan mantener su bandeja de entrada limpia y organizada, especialmente para rastrear facturas, pedidos y documentos importantes.

**Problem Statement:**

Las bandejas de Gmail se llenan de correos no deseados (promociones, social, no-reply) mientras que las facturas importantes pueden perderse. Las herramientas existentes son demasiado complejas o no manejan español correctamente.

**Solution Summary:**

Un limpiador de email basado en reglas bilingües que detecta patrones específicos (facturas, pedidos, promociones, redes sociales, despliegues técnicos) y los organiza automáticamente en categorías profesionales. Nunca pierdas una factura importante nuevamente.

# 

# 

# 

# **2\. Goals & Non‑Goals**

## **2.1 MVP Goals**

* Login Gmail vía OAuth seguro
* Leer bandeja y metadata de emails
* Detectar patrones bilingües (español + inglés)
* Categorías profesionales: Bills, Orders, Trash, Social, Technical
* Aplicar etiquetas automáticamente
* Dashboard profesional con foco en facturas
* Log de acciones para rastreo de documentos importantes

## **2.2 Non‑Goals (for now)**

* Full AI classification  
* Multi-provider support (Outlook, Yahoo, etc.)  
* Mobile or desktop apps  
* Complex analytics  
* Real-time processing

# **3\. Core Features (MVP)**

* Login Google OAuth seguro
* Obtención de emails (asunto, remitente, headers, preview)
* Detección de patrones bilingües (español + inglés)
* Categorías automáticas: Bills, Orders, Trash, Social, Technical
* Motor de reglas con prioridades
* Etiquetado automático vía Gmail API
* Dashboard profesional enfocado en facturas
* Logs históricos para rastreo de documentos

# 

# 

# 

# **4\. Architecture**

## **4.1 High-Level Flow**

Código

Browser → Backend (Python) → Gmail API → Email Data → Rule Engine → Actions → Dashboard

**4.2 Backend**

* Python (Flask or FastAPI)  
* OAuth handling  
* Rule engine  
* Email processing logic  
* Logging system

## **4.3 Frontend**

* HTML templates (Jinja2)  
* Minimal JavaScript (optional)

## **4.4 Database**

**MVP:** SQLite

**Tables:**

* users  
* rules  
* processed\_emails  
* logs

## **4.5 Deployment**

* Simple VPS or cloud service  
* HTTPS required for OAuth  
* Environment variables for secrets

# 

# **5\. Rule Engine Specification**

## **5.1 Rule Types**

* Sender contains  
* Subject contains  
* Body contains  
* Regex match  
* Header detection  
* Newsletter detection

## **5.2 Actions**

* Apply tag  
* Archive  
* Mark as read  
* Move to folder

## **5.3 Rule Priority**

* Rules evaluated in order  
* First match wins (or allow multiple matches depending on design)

## **5.4 Example Rules**

Código

Rule 1:

  Match: sender contains "noreply"

  Action: tag "No Reply"

  Priority: 1

Rule 2:

  Match: subject contains "invoice"

  Action: tag "Finance"

  Priority: 2

# **6\. Pattern Detection (Built‑In Rules - Español + English)**

## **6.1 Trash/Publy Detection (Eliminar)**

* **No-Reply**: "noreply", "no-reply", "sin-respuesta"
* **Promociones**: "oferta", "promo", "promotion", "descuento", "special offer"
* **Newsletters**: "unsubscribe", "darse de baja", "newsletter", "boletín"
* **Automated**: "no-reply", "automated", "automatizado"

## **6.2 Social Media (Redes Sociales)**

* **Facebook**: "facebook", "facebookmail"
* **Instagram**: "instagram", "instagram.com"
* **Twitter/X**: "twitter", "x.com", "t.co"
* **LinkedIn**: "linkedin", "linked.in"
* **General**: "notification", "notificación", "social"

## **6.3 Bills & Invoices (Facturas - ¡PRIORIDAD!) **

* **Facturas**: "factura", "invoice", "recibo", "receipt", "comprobante"
* **Pagos**: "pago", "paid", "payment", "billing", "facturación"
* **Suscripciones**: "subscription", "suscripción", "renewal", "renovación"
* **PDF**: "pdf", "attachment", "adjunto"

## **6.4 Orders & Shipping (Pedidos)**

* **Pedidos**: "pedido", "order", "orden de compra", "purchase order"
* **Envíos**: "enviado", "shipped", "entregado", "delivered"
* **Estado**: "on the way", "en camino", "arrives today", "llega hoy"
* **Confirmaciones**: "confirmation", "confirmación", "order update"

## **6.5 Technical & Deployment (Técnico)**

* **Despliegues**: "deploy", "deployment", "despliegue", "build", "pipeline"
* **Alertas**: "alert", "alerta", "warning", "advertencia", "error", "failed"
* **Sistemas**: "system", "sistema", "ci/cd", "jenkins", "github actions"

## **6.6 System Headers**

* `Auto-Submitted: auto-generated`
* `Precedence: bulk`
* `List-Unsubscribe:`
* `X-Auto-Response:`

# 

# 

# 

# 

# **7\. Data Model**

## **7.1 User**

* id  
* email  
* oauth\_token  
* created\_at

## **7.2 Rule**

* id  
* user\_id  
* match\_type  
* match\_value  
* action  
* priority

## **7.3 ProcessedEmail**

* id  
* user\_id  
* email\_id  
* applied\_rule  
* timestamp

## **7.4 Logs**

* id  
* event  
* details  
* timestamp

# 

# 

# 

# **8\. Roadmap**

## **Phase 1 — MVP Profesional (Sin AI)**

* Login OAuth Gmail
* Motor de reglas bilingüe español + inglés
* Categorías profesionales: Bills, Orders, Trash, Social, Technical
* Etiquetado automático vía Gmail API
* Dashboard con foco en facturas
* Logging para rastreo de documentos importantes

## **Phase 2 — Funciones Profesionales Avanzadas**

* Interfaz completa de procesamiento de emails
* Reglas personalizadas avanzadas
* Exportación y backup de facturas
* Notificaciones de facturas importantes
* Estadísticas detalladas de gastos y pedidos

## **Phase 3 — AI Integration (Futuro)**

* Reconocimiento inteligente de facturas
* Categorización automática avanzada
* Alertas de gastos inusuales
* Sistema híbrido AI + reglas profesionales

## **Phase 4 — Enterprise & Monetization**

* Multi-cuenta para empresas
* Integración con sistemas contables
* Reportes financieros automatizados
* API para integraciones empresariales
* Sistema de suscripciones premium

# 

# 

# 

# **9\. Tools & Technologies**

## **9.1 Programming**

* Python  
* Flask or FastAPI

## **9.2 APIs**

* Gmail API  
* Google OAuth

## **9.3 Database**

* SQLite (MVP)  
* Postgres (future)

## **9.4 Hosting**

* Render  
* Railway  
* DigitalOcean  
* AWS

## **9.5 Optional AI Providers (Future)**

* Gemini  
* OpenAI  
* Azure OpenAI

# 

# 

# 

# 

# **10\. Investigation Topics**

## **10.1 Gmail API**

* Fetching emails  
* Applying labels  
* Rate limits  
* OAuth scopes

## **10.2 Rule Engine Design**

* Priority systems  
* Performance  
* Extensibility

## **10.3 Pattern Detection**

* Regex  
* Header parsing  
* Newsletter heuristics

## **10.4 AI Integration (Future)**

* Cost estimation  
* Model selection  
* Hybrid architecture

## **10.5 Security**

* OAuth token storage  
* HTTPS  
* User data privacy

# **11\. Open Questions**

* Should rules be global or per-user?  
* Should multiple actions be allowed per rule?  
* Should full email bodies be stored or only metadata?  
* Should processing be real-time or batch-based?  
* How to handle large inboxes efficiently?

# **12\. Notes & Ideas**

(Free space for brainstorming, sketches, thoughts, and future improvements.)

If you want, I can also create:

* a **matching folder structure** for your GitHub repo  
* a **roadmap timeline**  
* a **visual architecture diagram**  
* or a **step-by-step coding plan**

