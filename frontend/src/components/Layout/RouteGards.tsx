import { useEffect } from 'react'
import { Navigate, Outlet, useLocation } from 'react-router-dom'
import { useNotifications } from '../../features/Feedback'
import { useAuthentication } from '../../hooks/useAuthentication'

interface RouteProps {
  redirectPath?: string
  children?: JSX.Element
}

interface GeneralRouteProps extends RouteProps {
  isAllowed: boolean
  loading?: boolean
}

/**
 * Route that enforces a custom check before displaying the content
 */
export const RequireCustomCheck = (props: GeneralRouteProps) => {
  const location = useLocation()
  const { isAllowed, loading = false, redirectPath = '/access-denied', children } = props

  if (loading) {
    return <p>Lade...</p>
  }

  if (!isAllowed) {
    return <Navigate to={redirectPath} state={{ from: location }} replace />
  }

  return children ? children : <Outlet />
}

/**
 * Route that forces user to be logged in. Redirects to /login by default
 */
export function RequireAuth({ redirectPath = '/login', children }: RouteProps) {
  const location = useLocation()
  const { user, loading } = useAuthentication()

  if (loading) {
    return <p>Lade...</p>
  }

  if (!user) {
    return <Navigate to={redirectPath} state={{ from: location }} replace />
  }

  return children ? children : <Outlet />
}

/**
 * Route that forces user to be admin. Redirects to /access-denied and prompts a notification
 */
export const RequireAdmin = ({ redirectPath = '/access-denied', children }: RouteProps) => {
  const { isAdmin, loading } = useAuthentication()
  const addNotification = useNotifications((state) => state.addNotification)

  useEffect(() => {
    if (!isAdmin && !loading) {
      addNotification({
        message: 'Du hast nicht die erforderlichen Rechte, um diesen Inhalt zu sehen',
        options: {
          variant: 'error',
        },
      })
    }
  }, [isAdmin, addNotification, loading])

  if (loading) {
    return <p>Lade...</p>
  }

  if (!isAdmin) {
    return <Navigate to={redirectPath} replace />
  }

  return children ? children : <Outlet />
}
