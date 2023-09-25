import { EmailInput, PasswordInput, TextInput, isValidEmail, isValidPassword } from '@/features/Input'
import { useAuthentication } from '@/hooks/useAuthentication'
import { LocationState } from '@/utils/types'
import LoadingButton from '@mui/lab/LoadingButton'
import { Divider, Grid, Link, Paper, Typography } from '@mui/material'
import { Box, Stack } from '@mui/system'
import { useState } from 'react'
import { Link as NavLink, Navigate, useLocation } from 'react-router-dom'

export default function LoginPage() {
    const { loading, user, register } = useAuthentication()
    const location = useLocation()

    const [state, setState] = useState({
        firstname: '',
        lastname: '',
        email: '',
        password: '',
        passwordConfirm: '',
    })

    const isFormValid = () => {
        return isValidEmail(state.email) && isValidPassword(state.password) && state.password === state.passwordConfirm
    }

    const onSubmit = (e: React.FormEvent) => {
        e.preventDefault()
        register(state)
    }

    if (user) {
        let to = (location.state as LocationState)?.from?.pathname
        if (!to || to === '/access-denied') to = '/'

        return <Navigate to={to} replace />
    }

    return (
        <Box sx={{ maxWidth: 500, mx: 'auto', my: 2 }}>
            <form onSubmit={onSubmit}>
                <Paper sx={{ padding: 2 }}>
                    <Stack spacing={1}>
                        <Grid container justifyContent="center">
                            <img src="/logo.svg" alt="Konfetti" style={{ height: 150 }} />
                        </Grid>
                        <TextInput
                            value={state.firstname}
                            label="Vorname"
                            setValue={(firstname) => setState({ ...state, firstname })}
                            validation={() => state.firstname.length > 2}
                            autoFocus
                            helperText="Der Vorname muss mindestens 3 Zeichen lang sein."
                        />
                        <TextInput
                            value={state.lastname}
                            label="Nachname"
                            setValue={(lastname) => setState({ ...state, lastname })}
                            validation={() => state.lastname.length > 2}
                            helperText="Der Nachname muss mindestens 3 Zeichen lang sein."
                        />
                        <EmailInput email={state.email} setEmail={(email) => setState({ ...state, email })} autoFocus />
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
                            Registrieren
                        </LoadingButton>
                        <Divider flexItem />
                        <Typography variant="body2" align="center">
                            Du hast bereits ein Konto?{' '}
                            <Link component={NavLink} to="/login" underline="hover">
                                Hier anmelden
                            </Link>
                            .
                        </Typography>
                    </Stack>
                </Paper>
            </form>
        </Box>
    )
}
