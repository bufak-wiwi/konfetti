import { useEffect } from 'react'
import { Navigate, Outlet, useLocation, useParams } from 'react-router-dom'
import { LoadingOverlay, useNotifications } from '../../features/Feedback'
import { useAuthentication } from '../../hooks/useAuthentication'
import { useAtom } from 'jotai'
import { conferenceIdAtom } from '@/utils/atoms'
import { useConferenceList } from '@/api'

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
        return <LoadingOverlay loading={true} />
    }

    if (!isAllowed) {
        return <Navigate to={redirectPath} state={{ from: location }} replace />
    }

    return children ? children : <Outlet />
}

/**
 * Route enforces a valid `conferenceId` in the path or redirects to the dashboard
 */
export function RequireConference({ children }: RouteProps) {
    const params = useParams()
    const givenId = parseInt(params.conferenceId || '0')

    const [currentId, setConferenceId] = useAtom(conferenceIdAtom)
    const { data, isLoading } = useConferenceList()

    const addNotification = useNotifications((state) => state.addNotification)

    // update conference Id for url change
    useEffect(() => {
        if (!data) {
            return
        }

        if (!givenId || !data.some((x) => x.id === givenId)) {
            addNotification({
                message: 'Es konnte keine Konferenz mit dieser ID gefunden werden.',
                options: {
                    variant: 'error',
                },
            })
            return
        }

        // update conferenceId to the new ID
        if (givenId && currentId !== givenId) {
            setConferenceId(givenId)
        }
    }, [givenId, data])

    if (isLoading || !data) {
        return <LoadingOverlay loading={true} />
    }

    if (!givenId || !data.some((x) => x.id === givenId)) {
        return <Navigate to={'/'} replace />
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
        return <LoadingOverlay loading={true} />
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
        return <LoadingOverlay loading={true} />
    }

    if (!isAdmin) {
        return <Navigate to={redirectPath} replace />
    }

    return children ? children : <Outlet />
}
