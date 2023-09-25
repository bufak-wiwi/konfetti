import { useEffect, useMemo } from 'react'
import { Route, Routes, useNavigate } from 'react-router-dom'
import { Box, useTheme } from '@mui/material'
import { useAtom } from 'jotai'
import { ejectInterceptors, setupInterceptors } from '@/api'
import { sidebarWidth } from '@/config'
import { Route as RouteItem, adminRoutes, authenticatedRoutes, publicRoutes } from '@/config/routes'
import { useNotifications } from '@/features/Feedback'
import useWindow from '@/hooks/useWindow'
import { confettiAtom, sidebarAtom } from '@/utils/atoms'
import ErrorBoundary from './ErrorBoundary'
import { RequireAdmin, RequireAuth } from './RouteGards'
import Confetti from 'react-confetti'

export default function Pages() {
    const navigate = useNavigate()
    const addNotification = useNotifications((state) => state.addNotification)
    const [sidebarOpen] = useAtom(sidebarAtom)
    const [showConfetti] = useAtom(confettiAtom)
    const { width } = useWindow()
    const theme = useTheme()

    const marginTop = useMemo(() => Number(theme.mixins.toolbar.minHeight || 0), [theme])
    const marginLeft = useMemo(() => (sidebarOpen ? sidebarWidth : width < 600 ? 0 : 72), [sidebarOpen, width])

    // setup axios interceptors
    useEffect(() => {
        setupInterceptors(navigate, addNotification)
        return () => ejectInterceptors()
    }, [addNotification, navigate])

    const renderRoutes = (routes: RouteItem[]) =>
        routes.map(({ path, component: Component }) => <Route key={path} path={path} element={<Component />} />)

    return (
        <Box
            component="main"
            sx={{
                height: `calc(100vh - ${marginTop}px)`,
                marginTop: `${marginTop}px`,
                marginLeft: `${marginLeft}px`,
                padding: theme.spacing(2),
            }}
        >
            <ErrorBoundary>
                {showConfetti && <Confetti />}
                <Routes>
                    {renderRoutes(publicRoutes)}
                    <Route element={<RequireAuth />}>{renderRoutes(authenticatedRoutes)}</Route>
                    <Route element={<RequireAdmin />}>{renderRoutes(adminRoutes)}</Route>
                </Routes>
            </ErrorBoundary>
        </Box>
    )
}
