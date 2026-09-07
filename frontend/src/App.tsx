import { Navigate, Route, Routes } from 'react-router-dom'
import { AppShell } from './components/layout/AppShell'
import { Dashboard } from './pages/Dashboard'
import { PlaceholderPage } from './pages/PlaceholderPage'

function App() {
  return <Routes><Route element={<AppShell />}><Route path="/dashboard" element={<Dashboard />} /><Route path="/village-intelligence/:villageId?" element={<PlaceholderPage title="Village Intelligence" />} /><Route path="/solar-potential" element={<PlaceholderPage title="Solar Potential" />} /><Route path="/financial-analysis" element={<PlaceholderPage title="Financial Analysis" />} /><Route path="/priority-ranking" element={<PlaceholderPage title="Priority Ranking" />} /><Route path="/investment-optimizer" element={<PlaceholderPage title="Investment Optimizer" />} /><Route path="/lifecycle-monitoring" element={<PlaceholderPage title="Lifecycle Monitoring" />} /><Route path="*" element={<Navigate replace to="/dashboard" />} /></Route></Routes>
}

export default App
