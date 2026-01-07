import { useState, useEffect } from 'react'
import { dashboardAPI } from '../services/api'

const Dashboard = () => {
  const [stats, setStats] = useState(null)
  const [activity, setActivity] = useState([])
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    loadDashboard()
  }, [])

  const loadDashboard = async () => {
    try {
      const [statsResponse, activityResponse] = await Promise.all([
        dashboardAPI.getStats(),
        dashboardAPI.getActivity(10)
      ])
      setStats(statsResponse.data)
      setActivity(activityResponse.data.logs)
    } catch (error) {
      console.error('Error loading dashboard:', error)
    } finally {
      setLoading(false)
    }
  }

  if (loading) {
    return (
      <div className="flex justify-center items-center h-64">
        <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-600"></div>
      </div>
    )
  }

  return (
    <div className="space-y-6">
      <div>
        <h1 className="text-3xl font-bold text-gray-900">Dashboard</h1>
        <p className="text-gray-600 mt-2">Overview of your email cleaning activity</p>
      </div>

      {/* Stats Cards - Professional Focus */}
      {stats && (
        <div className="grid grid-cols-1 md:grid-cols-4 gap-6">
          <div className="bg-white p-6 rounded-lg shadow">
            <h3 className="text-lg font-medium text-gray-900">Active Rules</h3>
            <p className="text-3xl font-bold text-blue-600 mt-2">{stats.total_rules}</p>
          </div>

          <div className="bg-white p-6 rounded-lg shadow">
            <h3 className="text-lg font-medium text-gray-900">Processed Today</h3>
            <p className="text-3xl font-bold text-green-600 mt-2">{stats.processed_today}</p>
          </div>

          <div className="bg-white p-6 rounded-lg shadow">
            <h3 className="text-lg font-medium text-gray-900">Bills Tracked</h3>
            <p className="text-3xl font-bold text-emerald-600 mt-2">{stats.bills_tracked}</p>
          </div>

          <div className="bg-white p-6 rounded-lg shadow">
            <h3 className="text-lg font-medium text-gray-900">Categories Cleaned</h3>
            <p className="text-3xl font-bold text-purple-600 mt-2">{stats.category_breakdown?.length || 0}</p>
          </div>
        </div>
      )}

      {/* Category Breakdown */}
      {stats?.category_breakdown && stats.category_breakdown.length > 0 && (
        <div className="bg-white rounded-lg shadow p-6">
          <h3 className="text-lg font-medium text-gray-900 mb-4">Email Categories</h3>
          <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
            {stats.category_breakdown.map((category) => (
              <div key={category.category} className="text-center p-4 bg-gray-50 rounded-lg">
                <p className="text-2xl font-bold text-gray-900">{category.count}</p>
                <p className="text-sm text-gray-600">{category.category}</p>
              </div>
            ))}
          </div>
        </div>
      )}

      {/* Recent Activity */}
      <div className="bg-white rounded-lg shadow">
        <div className="px-6 py-4 border-b border-gray-200">
          <h3 className="text-lg font-medium text-gray-900">Recent Activity</h3>
        </div>

        <div className="divide-y divide-gray-200">
          {activity.length > 0 ? (
            activity.map((log) => (
              <div key={log.id} className="px-6 py-4">
                <div className="flex items-center justify-between">
                  <div>
                    <p className="text-sm font-medium text-gray-900 truncate">
                      {log.subject || 'No subject'}
                    </p>
                    <p className="text-sm text-gray-500">
                      {log.sender} • Moved to {log.category}
                    </p>
                  </div>
                  <div className="text-right">
                    <span className={`inline-flex px-2 py-1 text-xs font-medium rounded-full ${
                      log.success
                        ? 'bg-green-100 text-green-800'
                        : 'bg-red-100 text-red-800'
                    }`}>
                      {log.success ? 'Success' : 'Failed'}
                    </span>
                    <p className="text-xs text-gray-500 mt-1">
                      {new Date(log.processed_at).toLocaleDateString()}
                    </p>
                  </div>
                </div>
              </div>
            ))
          ) : (
            <div className="px-6 py-8 text-center text-gray-500">
              No activity yet. Start by creating some rules and processing your emails!
            </div>
          )}
        </div>
      </div>
    </div>
  )
}

export default Dashboard
