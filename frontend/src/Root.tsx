import { QueryClient, QueryClientProvider } from '@tanstack/react-query'
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
                    <App />
                </QueryClientProvider>
            </AuthProvider>
        </StrictMode>
    )
}

export default render
