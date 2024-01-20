import { matchPath, useLocation } from 'react-router-dom'
import { Route, routes } from '@/config/routes'

/**
 * Get the current route and the matched params even ouside of of the router context
 */
export const useCurrentRoute = () => {
    const location = useLocation()
    for (const route of routes) {
        const match = matchPath(route, location.pathname)
        if (match) {
            return { route, params: match.params }
        }
    }
    return { route: routes[routes.length - 1] as Route, params: {} }
}
