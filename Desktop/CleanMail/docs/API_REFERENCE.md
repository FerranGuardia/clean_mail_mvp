# CleanMail API Reference

## Authentication Endpoints

### Google OAuth Login
```
GET /api/auth/google
```
Initiates Google OAuth flow. Redirects to Google for authentication.

### OAuth Callback
```
GET /api/auth/callback?code={authorization_code}
```
Handles OAuth callback from Google. Exchanges code for tokens and creates/updates user.

### Get Current User
```
GET /api/auth/me
Authorization: Bearer {jwt_token}
```
Returns current user information.

## Rules Endpoints

### List Rules
```
GET /api/rules
Authorization: Bearer {jwt_token}
```
Returns all rules for the authenticated user.

### Create Rule
```
POST /api/rules
Authorization: Bearer {jwt_token}
Content-Type: application/json

{
  "name": "No Reply Filter",
  "description": "Tag emails from noreply addresses",
  "match_type": "sender",
  "match_value": "noreply",
  "action_type": "tag",
  "action_value": "No Reply",
  "priority": 1
}
```

### Update Rule
```
PUT /api/rules/{rule_id}
Authorization: Bearer {jwt_token}
Content-Type: application/json
```

### Delete Rule
```
DELETE /api/rules/{rule_id}
Authorization: Bearer {jwt_token}
```

## Email Endpoints

### Preview Emails
```
GET /api/emails/preview?max_results=10
Authorization: Bearer {jwt_token}
```
Returns preview of emails from user's inbox.

### Process Emails
```
POST /api/emails/process
Authorization: Bearer {jwt_token}
Content-Type: application/json

{
  "max_emails": 50
}
```

### Get Built-in Patterns
```
GET /api/emails/patterns
Authorization: Bearer {jwt_token}
```
Returns suggested rule patterns.

## Dashboard Endpoints

### Get Statistics
```
GET /api/dashboard/stats
Authorization: Bearer {jwt_token}
```
Returns dashboard statistics.

### Get Activity Log
```
GET /api/dashboard/activity?limit=50&offset=0
Authorization: Bearer {jwt_token}
```
Returns recent activity log.

## Data Types

### Rule Object
```json
{
  "id": 1,
  "user_id": 1,
  "name": "Newsletter Filter",
  "description": "Handle newsletter emails",
  "match_type": "sender",
  "match_value": "newsletter",
  "action_type": "tag",
  "action_value": "Newsletter",
  "priority": 0,
  "is_active": true,
  "created_at": "2024-01-01T00:00:00Z",
  "updated_at": "2024-01-01T00:00:00Z"
}
```

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
  "subject": "Email Subject",
  "sender": "sender@example.com",
  "action": "tag",
  "success": true,
  "processed_at": "2024-01-01T00:00:00Z"
}
```

## Error Responses

All endpoints return errors in the following format:
```json
{
  "detail": "Error message description"
}
```

Common HTTP status codes:
- `200` - Success
- `401` - Unauthorized (invalid/missing token)
- `403` - Forbidden (insufficient permissions)
- `404` - Not found
- `422` - Validation error
- `500` - Internal server error
