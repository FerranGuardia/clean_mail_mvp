import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import Landing from './pages/Landing'
import Login from './pages/Login'
import Dashboard from './pages/Dashboard'
import Rules from './pages/Rules'
import Process from './pages/Process'
import Navbar from './components/Navbar'

function App() {
  return (
    <Router>
      <div className="min-h-screen bg-white">
        <Routes>
          <Route path="/" element={<Landing />} />
          <Route path="/app/*" element={<AppLayout />} />
        </Routes>
      </div>
    </Router>
  )
}

function AppLayout() {
  return (
    <>
      <Navbar />
      <main className="container mx-auto px-4 py-8">
        <Routes>
          <Route path="/dashboard" element={<Dashboard />} />
          <Route path="/login" element={<Login />} />
          <Route path="/rules" element={<Rules />} />
          <Route path="/process" element={<Process />} />
        </Routes>
      </main>
    </>
  )
}

export default App
