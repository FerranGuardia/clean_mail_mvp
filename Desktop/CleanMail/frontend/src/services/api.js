import axios from 'axios'

const API_BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000'

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
})

// Request interceptor to add auth token
api.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem('token')
    if (token) {
      config.headers.Authorization = `Bearer ${token}`
    }
    return config
  },
  (error) => {
    return Promise.reject(error)
  }
)

// Response interceptor to handle errors
api.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response?.status === 401) {
      // Token expired or invalid
      localStorage.removeItem('token')
      window.location.href = '/login'
    }
    return Promise.reject(error)
  }
)

export const authAPI = {
  login: () => {
    // Redirect to Google OAuth
    window.location.href = `${API_BASE_URL}/api/auth/google`
  },

  logout: () => {
    localStorage.removeItem('token')
    window.location.href = '/login'
  },

  getCurrentUser: () => api.get('/api/auth/me'),
}

export const rulesAPI = {
  getRules: () => api.get('/api/rules'),
  createRule: (rule) => api.post('/api/rules', rule),
  updateRule: (id, rule) => api.put(`/api/rules/${id}`, rule),
  deleteRule: (id) => api.delete(`/api/rules/${id}`),
}

export const emailsAPI = {
  previewEmails: (maxResults = 10) => api.get(`/api/emails/preview?max_results=${maxResults}`),
  processEmails: (maxEmails = 50) => api.post('/api/emails/process', { max_emails: maxEmails }),
  getPatterns: () => api.get('/api/emails/patterns'),
}

export const dashboardAPI = {
  getStats: () => api.get('/api/dashboard/stats'),
  getActivity: (limit = 50, offset = 0) => api.get(`/api/dashboard/activity?limit=${limit}&offset=${offset}`),
}

export default api
