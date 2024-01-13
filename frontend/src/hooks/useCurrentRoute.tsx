import { matchPath, useLocation } from 'react-router-dom'
import { Route, routes } from '@/config/routes'

export const useCurrentRoute = () => {
    const location = useLocation()
    for (const route of routes) {
        if (matchPath(route, location.pathname)) {
            return route
        }
    }
    return routes[routes.length - 1] as Route
}
