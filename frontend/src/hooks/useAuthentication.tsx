import { api } from '@/api/api'
import { useConfirm, useNotifications } from '@/features/Feedback'
import { useAuthenticationStore } from '@/store/useAuthenticationStore'
import { User } from '@/utils/types'
import { AxiosError } from 'axios'
import { SnackbarKey } from 'notistack'
import { ReactElement, createContext, useContext, useState } from 'react'

interface CreateUser {
    email: string
    password: string
    lastname: string
    firstname: string
}

interface AuthContext {
    user: User | null
    loading: boolean
    isAdmin: boolean
    login: (email: string, password: string) => void
    register: (user: CreateUser) => void
    logout: () => void
    sendResetPassword: (email: string) => void
    resetPassword: (state: { password: string; token: string; userId: number }) => Promise<void | SnackbarKey>
    confirmEmail: (state: { emailToken: string; userId: number }) => Promise<void | SnackbarKey>
}

const authContext = createContext<AuthContext>({
    user: null,
    loading: false,
    isAdmin: false,
} as AuthContext)

export const AuthProvider = ({ children }: { children: ReactElement }) => {
    const auth = useProvideAuth()
    return <authContext.Provider value={auth}>{children}</authContext.Provider>
}

export const useAuthentication = () => {
    return useContext(authContext)
}

const useProvideAuth = () => {
    const addNotification = useNotifications((state) => state.addNotification)
    const { confirmDialog } = useConfirm()

    const { user, isAdmin, setUser } = useAuthenticationStore()
    const [loading, setLoading] = useState<boolean>(false)

    const login = async (email: string, password: string) => {
        setLoading(true)
        const data = new FormData()
        data.append('username', email)
        data.append('password', password)
        api.post<User>('/login', data)
            .then((result) => {
                setUser(result.data)
                addNotification({ message: 'Anmeldung erfolgreich', options: { variant: 'success' } })
            })
            .catch(() => {
                addNotification({ message: 'Anmeldung fehlgeschlagen.', options: { variant: 'error' } })
            })
            .finally(() => setLoading(false))
    }

    const logout = () => {
        setLoading(true)
        confirmDialog(
            'Willst du dich wirklich abmelden?',
            () => {
                api.post('/logout')
                    .then(() =>
                        addNotification({
                            message: 'Abmeldung erfolgreich',
                            options: { variant: 'success' },
                        })
                    )
                    .finally(() => {
                        setUser(null)
                        setLoading(false)
                    })
            },
            'error'
        )
    }

    const register = async (user: CreateUser) => {
        setLoading(true)
        api.post('/user', user)
            .then((result) => {
                setUser(result.data)
                addNotification({ message: 'Anmeldung erfolgreich', options: { variant: 'success' } })
            })
            .catch((e: AxiosError) => {
                if (e.response?.status === 409) {
                    addNotification({
                        message: 'Es existiert bereits ein Account mit dieser E-Mail-Adresse',
                        options: { variant: 'error' },
                    })
                } else {
                    addNotification({
                        message: 'Anmeldung fehlgeschlagen',
                        options: { variant: 'error' },
                    })
                }
            })
            .finally(() => setLoading(false))
    }

    const sendResetPassword = async (email: string) =>
        api
            .post('/user/sendResetPassword', { email })
            .then(() =>
                addNotification({
                    message: 'Du wirst in wenigen Minuten eine E-Mail zum Zurücksetzen deines Passworts bekommen.',
                    options: { variant: 'success' },
                })
            )
            .catch(() =>
                addNotification({
                    message: 'Ups... hier ist etwas schief gelaufen. Probiere es später noch einmal.',
                    options: { variant: 'error' },
                })
            )

    const resetPassword = async ({
        password,
        token,
        userId,
    }: {
        password: string
        token: string
        userId: number
    }): Promise<void | SnackbarKey> => {
        setLoading(true)
        return api
            .post('/user/resetPassword', { password, passwordToken: token, userId })
            .then(() =>
                addNotification({
                    message: 'Passwort erfolgreich zurückgesetzt',
                    options: { variant: 'success' },
                })
            )
            .catch(() =>
                addNotification({
                    message: 'Ups... hier ist etwas schief gelaufen. Probiere es später noch einmal.',
                    options: { variant: 'error' },
                })
            )
            .finally(() => setLoading(false))
    }

    const confirmEmail = ({
        emailToken,
        userId,
    }: {
        emailToken: string
        userId: number
    }): Promise<void | SnackbarKey> => {
        setLoading(true)
        return api
            .post('/user/confirm', { emailToken, userId })
            .then((result) => {
                addNotification({
                    message: 'E-Mail erfolgreich bestätigt',
                    options: { variant: 'success' },
                })
                setUser(result.data)
            })
            .catch(() =>
                addNotification({
                    message: 'Ups... hier ist etwas schief gelaufen. Probiere es später noch einmal.',
                    options: { variant: 'error' },
                })
            )
            .finally(() => setLoading(false))
    }

    return {
        user,
        loading,
        isAdmin,
        login,
        logout,
        register,
        sendResetPassword,
        resetPassword,
        confirmEmail,
    }
}
