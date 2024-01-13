import asyncComponentLoader from '@/utils/loader'
import { BackHand, SvgIconComponent } from '@mui/icons-material'
import HomeIcon from '@mui/icons-material/Home'
import { FC } from 'react'
import { PathRouteProps } from 'react-router-dom'

export interface RouteItem extends PathRouteProps {
    path: string
    title?: string
    component: FC
}
export interface NavItem extends RouteItem {
    Icon: SvgIconComponent
    /**
     * Whether the whole url should be matched when highlighting the icon.
     */
    end?: boolean
}

export type Route = RouteItem | NavItem

export const adminRoutes: Route[] = []

export const authenticatedRoutes: Route[] = [
    {
        component: asyncComponentLoader(() => import('@/pages/Dashboard')),
        path: '/',
        end: true,
        title: 'Startseite',
        Icon: HomeIcon,
    },
    {
        component: asyncComponentLoader(() => import('@/pages/UserDetails')),
        path: '/user/:id',
        title: 'Profil',
    },
]

export const conferenceRoutes: Route[] = [
    {
        component: asyncComponentLoader(() => import('@/pages/conference/SpeakingList')),
        path: '/conference/:conferenceId/redeliste',
        Icon: BackHand,
        end: true,
        title: 'Redeliste',
    },
]

export const publicRoutes: Route[] = [
    {
        component: asyncComponentLoader(() => import('@/pages/auth/LoginPage')),
        path: '/login',
        title: 'Konfetti',
    },
    {
        component: asyncComponentLoader(() => import('@/pages/auth/RegisterPage')),
        path: '/register',
        title: 'Konfetti',
    },
    {
        component: asyncComponentLoader(() => import('@/pages/auth/ResetPasswordPage')),
        path: '/resetPassword',
        title: 'Passwort zurücksetzen',
    },
    {
        component: asyncComponentLoader(() => import('@/pages/auth/ConfirmMailPage')),
        path: '/verifyEmail',
        title: 'E-Mail bestätigen',
    },
    {
        component: asyncComponentLoader(() => import('@/pages/AccessDenied')),
        path: '/access-denied',
        title: 'Zugriff verweigert',
    },
    {
        component: asyncComponentLoader(() => import('@/pages/NotFound')),
        path: '*',
        title: 'Not Found',
    },
]
export const routes = [...adminRoutes, ...authenticatedRoutes, ...conferenceRoutes, ...publicRoutes]

const isNavItem = (route: Route): route is NavItem => 'Icon' in route

export const adminNavItems = adminRoutes.filter(isNavItem)
export const authenticatedNavItems = authenticatedRoutes.filter(isNavItem)
export const conferenceNavItems = conferenceRoutes.filter(isNavItem)
export const publicNavItems = publicRoutes.filter(isNavItem)
