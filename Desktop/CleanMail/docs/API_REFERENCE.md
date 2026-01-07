# CleanMail API Reference

## Overview

CleanMail provides a REST API for professional Gmail inbox management. The API uses JWT authentication with Google OAuth 2.0 integration.

**Base URL**: `http://localhost:8000/api` (development)  
**Authentication**: Bearer tokens via Google OAuth  
**Format**: JSON for requests and responses

## Authentication Endpoints

### Google OAuth Login
```
GET /api/auth/google
```
Initiates Google OAuth flow with Gmail API permissions.

**Response**: Redirects to Google OAuth consent screen

### OAuth Callback
```
GET /api/auth/callback?code={authorization_code}
```
Handles OAuth callback from Google, exchanges code for tokens, and creates/updates user.

**Parameters**:
- `code`: Authorization code from Google

**Response**: Redirects to frontend with JWT token

### Get Current User
```
GET /api/auth/me
Authorization: Bearer {jwt_token}
```
Returns current authenticated user information.

**Headers**:
- `Authorization: Bearer {jwt_token}`

**Response**:
```json
{
  "id": 1,
  "email": "user@example.com",
  "name": "User Name",
  "picture": "https://..."
}
```

## Rules Endpoints

### List Rules
```
GET /api/rules?user_id={user_id}
Authorization: Bearer {jwt_token}
```
Returns all rules for the specified user.

**Parameters**:
- `user_id`: User ID (currently required, TODO: extract from JWT)

**Response**: Array of rule objects

### Create Rule
```
POST /api/rules?user_id={user_id}
Authorization: Bearer {jwt_token}
Content-Type: application/json

{
  "name": "No Reply Filter",
  "description": "Tag emails from noreply addresses",
  "match_type": "sender",
  "match_value": "noreply",
  "action_type": "tag",
  "action_value": "Trash",
  "priority": 1,
  "is_active": true
}
```

**Parameters**:
- `user_id`: User ID (currently required, TODO: extract from JWT)

**Request Body**:
- `name`: Rule name
- `description`: Rule description
- `match_type`: "sender", "subject", "body", or "regex"
- `match_value`: Pattern to match
- `action_type`: "tag", "archive", "mark_read", "move"
- `action_value`: Action parameter (label name, etc.)
- `priority`: Rule priority (lower numbers = higher priority)
- `is_active`: Whether rule is enabled

### Get Rule
```
GET /api/rules/{rule_id}?user_id={user_id}
Authorization: Bearer {jwt_token}
```
Returns a specific rule by ID.

### Update Rule
```
PUT /api/rules/{rule_id}?user_id={user_id}
Authorization: Bearer {jwt_token}
Content-Type: application/json
```
Updates an existing rule.

### Delete Rule
```
DELETE /api/rules/{rule_id}?user_id={user_id}
Authorization: Bearer {jwt_token}
```
Deletes a rule.

## Email Endpoints

### Preview Emails
```
GET /api/emails/preview?max_results=10
Authorization: Bearer {jwt_token}
```
Returns preview of recent emails from user's Gmail inbox.

**Parameters**:
- `max_results`: Number of emails to preview (default: 10, max: 50)

**Response**:
```json
{
  "emails": [
    {
      "id": "message_id",
      "subject": "Email Subject",
      "sender": "sender@example.com",
      "received_at": "2024-01-01T00:00:00Z",
      "body_preview": "Email preview text...",
      "labels": ["INBOX", "UNREAD"]
    }
  ]
}
```

### Process Emails
```
POST /api/emails/process?max_emails=50
Authorization: Bearer {jwt_token}
```
Processes emails using user's rules (runs in background).

**Parameters**:
- `max_emails`: Maximum emails to process (default: 50)

**Response**:
```json
{
  "message": "Email processing started in background"
}
```

**Notes**:
- Uses user's custom rules if available
- Falls back to built-in professional patterns
- Applies actions: tag, archive, mark_read
- Logs all actions for audit trail

### Get Built-in Patterns
```
GET /api/emails/patterns
Authorization: Bearer {jwt_token}
```
Returns built-in email patterns for professional filtering.

**Response**:
```json
{
  "patterns": {
    "bills": {
      "name": "Bills & Invoices",
      "description": "Facturas, recibos, y documentos de pago",
      "match_type": "subject",
      "match_value": "factura|invoice|recibo|billing|comprobante|pdf",
      "action_type": "tag",
      "action_value": "Bills"
    },
    "orders": { ... },
    "trash": { ... },
    "noreply": { ... },
    "social": { ... },
    "technical": { ... }
  }
}
```

## Dashboard Endpoints

### Get Statistics
```
GET /api/dashboard/stats
Authorization: Bearer {jwt_token}
```
Returns comprehensive dashboard statistics for professional email management.

**Response**:
```json
{
  "total_rules": 12,
  "processed_today": 45,
  "bills_tracked": 23,
  "category_breakdown": [
    {"category": "Bills", "count": 23},
    {"category": "Orders", "count": 15},
    {"category": "Trash", "count": 67}
  ],
  "recent_activity": [
    {
      "id": 123,
      "subject": "Invoice #12345",
      "action": "tag",
      "category": "Bills",
      "success": true,
      "processed_at": "2024-01-01T10:30:00Z"
    }
  ],
  "rule_performance": [
    {"rule_name": "Bills Filter", "processed_count": 23},
    {"rule_name": "Trash Filter", "processed_count": 67}
  ]
}
```

### Get Activity Log
```
GET /api/dashboard/activity?limit=50&offset=0
Authorization: Bearer {jwt_token}
```
Returns paginated activity log of processed emails.

**Parameters**:
- `limit`: Number of records to return (default: 50)
- `offset`: Pagination offset (default: 0)

**Response**:
```json
{
  "logs": [
    {
      "id": 123,
      "subject": "Invoice #12345",
      "sender": "billing@company.com",
      "action": "tag",
      "success": true,
      "processed_at": "2024-01-01T10:30:00Z"
    }
  ],
  "total": 150
}
```

## Authentication

All API endpoints (except OAuth flow) require authentication via JWT Bearer tokens:

```
Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...
```

### Getting Authenticated

1. **Start OAuth Flow**: `GET /api/auth/google`
2. **Handle Callback**: Google redirects to `/api/auth/callback`
3. **Receive Token**: Frontend receives JWT token in redirect
4. **Use Token**: Include in `Authorization` header for API calls

### Token Management

- Tokens are obtained through Google OAuth flow
- No refresh endpoint (OAuth handles token refresh)
- Tokens expire based on OAuth configuration (default: 1 hour)

## Data Types

### Rule Object
```json
{
  "id": 1,
  "user_id": 1,
  "name": "Bills Filter",
  "description": "Tag emails containing invoices and receipts",
  "match_type": "subject",
  "match_value": "factura|invoice|recibo",
  "action_type": "tag",
  "action_value": "Bills",
  "priority": 1,
  "is_active": true,
  "created_at": "2024-01-01T00:00:00Z",
  "updated_at": "2024-01-01T00:00:00Z"
}
```

**Fields**:
- `match_type`: "sender", "subject", "body", "regex", "header"
- `action_type`: "tag", "archive", "mark_read", "move"
- `priority`: Lower numbers = higher priority (0 is highest)
- `is_active`: Whether rule is currently enabled

### Email Preview Object
```json
{
  "id": "message_id",
  "subject": "Email Subject",
  "sender": "sender@example.com",
  "received_at": "2024-01-01T00:00:00Z",
  "body_preview": "Email preview text...",
  "labels": ["INBOX", "UNREAD"]
}
```

### Activity Log Object
```json
{
  "id": 1,
  "user_id": 1,
  "rule_id": 5,
  "gmail_message_id": "18c4b9f8e3d7a2b1",
  "subject": "Factura Electrónica #12345",
  "sender": "facturacion@empresa.com",
  "received_at": "2024-01-01T09:15:00Z",
  "applied_action": "tag",
  "action_value": "Bills",
  "success": true,
  "processed_at": "2024-01-01T10:30:00Z"
}
```

**Fields**:
- `gmail_message_id`: Gmail's unique message identifier
- `applied_action`: Action performed ("tag", "archive", "mark_read", "move")
- `action_value`: Action parameter (label name, etc.)
- `success`: Processing result (true/false or error message)

## Error Responses

All endpoints return errors in the following format:
```json
{
  "detail": "Error message description"
}
```

### HTTP Status Codes

| Code | Description | Common Causes |
|------|-------------|---------------|
| `200` | Success | Operation completed successfully |
| `401` | Unauthorized | Missing/invalid JWT token, expired OAuth |
| `403` | Forbidden | User doesn't own requested resource |
| `404` | Not Found | Rule, user, or email not found |
| `422` | Validation Error | Invalid request data, missing required fields |
| `429` | Too Many Requests | Gmail API rate limit exceeded |
| `500` | Internal Server Error | Server error, Gmail API failure |
| `503` | Service Unavailable | Gmail API temporarily unavailable |

### Common Error Messages

- `"Invalid authentication"` - Missing or malformed Authorization header
- `"User not found"` - User ID doesn't exist in database
- `"Rule not found"` - Rule ID doesn't exist or doesn't belong to user
- `"Failed to fetch emails"` - Gmail API error or invalid tokens
- `"Failed to get access token"` - OAuth flow failed
- `"Failed to get user info"` - Google user info API error

### Rate Limiting

- Gmail API has quota limits (1 billion quota units/month free)
- Email processing is rate-limited to prevent quota exhaustion
- Background processing helps manage API limits
