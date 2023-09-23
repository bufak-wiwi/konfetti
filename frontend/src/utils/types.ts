import type { SnackbarProps } from 'notistack'

export interface SnackbarType {
    options: SnackbarProps
    maxSnack: number
}

export interface User {
    id: number
    userName: string
    firstName: string
    lastName: string
    email: string
    phone: string
    isAdmin: boolean
    isEmailConfirmed: boolean
    createdAt: string
    updatedAt: string
}

export interface LocationState {
    from: {
        pathname: string
    }
}
