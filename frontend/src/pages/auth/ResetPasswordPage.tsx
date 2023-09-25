import { useNotifications } from '@/features/Feedback'
import { PasswordInput, isValidPassword } from '@/features/Input'
import { useAuthentication } from '@/hooks/useAuthentication'
import LoadingButton from '@mui/lab/LoadingButton'
import { Grid, Paper, Typography } from '@mui/material'
import { Box, Stack } from '@mui/system'
import { useEffect, useState } from 'react'
import { Navigate, useNavigate, useSearchParams } from 'react-router-dom'

export default function ResetPasswordPage() {
    const navigate = useNavigate()
    const addNotification = useNotifications((state) => state.addNotification)
    const { loading, resetPassword } = useAuthentication()

    const [searchParams] = useSearchParams()
    const tokenIssued = searchParams.get('expiresAt')
    const token = searchParams.get('token')
    const userId = searchParams.get('userId')

    const [state, setState] = useState({ password: '', passwordConfirm: '' })

    useEffect(() => {
        if (!token || !userId) {
            addNotification({ message: 'Ungültiger Link', options: { variant: 'error' } })
        } else if (tokenIssued && new Date(tokenIssued) < new Date()) {
            addNotification({
                message: 'Link abgelaufen. Lass dir einfach eine neue E-Mail zuschicken.',
                options: { variant: 'error' },
            })
        }
        // eslint-disable-next-line react-hooks/exhaustive-deps
    }, [tokenIssued, token, userId])

    const isFormValid = () => {
        return isValidPassword(state.password) && state.password === state.passwordConfirm
    }

    const onSubmit = (e: React.FormEvent) => {
        e.preventDefault()
        if (token && userId) {
            resetPassword({ token, userId: parseInt(userId), password: state.password }).then(() => {
                navigate('/login')
            })
        }
    }

    if (!token || !userId) {
        return <Navigate to="/login" replace />
    }

    if (tokenIssued && new Date(tokenIssued) < new Date()) {
        return <Navigate to="/login" replace />
    }

    return (
        <Box sx={{ maxWidth: 500, mx: 'auto', my: 2 }}>
            <form onSubmit={onSubmit}>
                <Paper sx={{ padding: 2 }}>
                    <Stack spacing={1}>
                        <Grid container justifyContent="center">
                            <img src="/logo.svg" alt="Konfetti" style={{ height: 150 }} />
                        </Grid>
                        <Typography variant="body1" align="center">
                            Jetzt Passwort zurücksetzen:
                        </Typography>
                        <PasswordInput
                            password={state.password}
                            setPassword={(password) => setState({ ...state, password })}
                            autoComplete="current-password"
                        />
                        <PasswordInput
                            password={state.passwordConfirm}
                            confirm
                            toConfirm={state.password}
                            setPassword={(passwordConfirm) => setState({ ...state, passwordConfirm })}
                        />

                        <LoadingButton
                            type="submit"
                            size="large"
                            fullWidth
                            loading={loading}
                            disabled={!isFormValid()}
                            variant="contained"
                        >
                            Passwort zurücksetzen
                        </LoadingButton>
                    </Stack>
                </Paper>
            </form>
        </Box>
    )
}
