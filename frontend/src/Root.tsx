import { LocalizationProvider } from '@mui/x-date-pickers'
import { AdapterDateFns } from '@mui/x-date-pickers/AdapterDateFns'
import { QueryClient, QueryClientProvider } from '@tanstack/react-query'
import deLocale from 'date-fns/locale/de'
import { ComponentType, StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import { AuthProvider } from './hooks/useAuthentication'

const container = document.getElementById('root') as HTMLElement
const root = createRoot(container)

const queryClient = new QueryClient()

function render(App: ComponentType) {
    root.render(
        <StrictMode>
            <AuthProvider>
                <QueryClientProvider client={queryClient}>
                    <LocalizationProvider dateAdapter={AdapterDateFns} adapterLocale={deLocale}>
                        <App />
                    </LocalizationProvider>
                </QueryClientProvider>
            </AuthProvider>
        </StrictMode>
    )
}

export default render
