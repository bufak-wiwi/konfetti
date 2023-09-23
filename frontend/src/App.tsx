import { BrowserRouter } from 'react-router-dom'
import CssBaseline from '@mui/material/CssBaseline'
import { ThemeProvider } from '@mui/material/styles'
import Header from '@/components/Layout/Header'
import Notifications from '@/components/Layout/Notifications'
import Sidebar from '@/components/Layout/Sidebar'
import { withErrorHandler } from '@/error-handling'
import AppErrorBoundaryFallback from '@/error-handling/fallbacks/App'
import Pages from './components/Layout/Pages'
import { ConfirmDialog } from './features/Feedback'
import { useCustomTheme } from './hooks/useCustomTheme'

function App() {
  const theme = useCustomTheme()

  return (
    <ThemeProvider theme={theme}>
      <CssBaseline enableColorScheme />
      <Notifications />
      <ConfirmDialog />
      <BrowserRouter>
        <Header />
        <Sidebar />
        <Pages />
      </BrowserRouter>
    </ThemeProvider>
  )
}

export default withErrorHandler(App, AppErrorBoundaryFallback)
