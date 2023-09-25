import { EmailInput, PasswordInput, isValidEmail, isValidPassword } from '@/features/Input'
import { useAuthentication } from '@/hooks/useAuthentication'
import { LocationState } from '@/utils/types'
import LoadingButton from '@mui/lab/LoadingButton'
import {
    Button,
    Dialog,
    DialogActions,
    DialogContent,
    DialogContentText,
    DialogTitle,
    Divider,
    Grid,
    Link,
    Paper,
    Typography,
} from '@mui/material'
import { Box, Stack } from '@mui/system'
import { useState } from 'react'
import { Link as NavLink, Navigate, useLocation } from 'react-router-dom'

export default function LoginPage() {
    const { loading, user, login, sendResetPassword } = useAuthentication()
    const location = useLocation()

    const [state, setState] = useState({ email: '', password: '', resetPassword: false })

    const isFormValid = () => {
        return isValidEmail(state.email) && isValidPassword(state.password)
    }

    const onSubmit = (e: React.FormEvent) => {
        e.preventDefault()
        login(state.email, state.password)
    }

    const onResetPassword = () => {
        sendResetPassword(state.email)
        setState({ ...state, resetPassword: false })
    }

    if (user) {
        let to = (location.state as LocationState)?.from?.pathname
        if (!to || to === '/access-denied') to = '/'

        return <Navigate to={to} replace />
    }

    function renderPasswordForget() {
        return (
            <Dialog open={state.resetPassword} onClose={() => setState({ ...state, resetPassword: false })}>
                <DialogTitle>Passwort zurücksetzen</DialogTitle>
                <DialogContent>
                    <DialogContentText sx={{ marginBottom: 4 }}>
                        Wenn die von dir eingegebene E-Mail-Adresse im System registriert ist, erhältst du in wenigen
                        Minuten eine E-Mail zum Zurücksetzen des Passworts. Bitte überprüfe auch deinen Spam-Ordner.
                    </DialogContentText>
                    <EmailInput email={state.email} setEmail={(email) => setState({ ...state, email })} />
                </DialogContent>
                <DialogActions>
                    <Button onClick={() => setState({ ...state, resetPassword: false })} color="primary">
                        Abbrechen
                    </Button>
                    <Button color="primary" disabled={!isValidEmail(state.email)} onClick={onResetPassword}>
                        Zurücksetzen
                    </Button>
                </DialogActions>
            </Dialog>
        )
    }

    return (
        <Box sx={{ maxWidth: 500, mx: 'auto', my: 2 }}>
            <form onSubmit={onSubmit}>
                <Paper sx={{ padding: 2 }}>
                    <Stack spacing={1}>
                        <Grid container justifyContent="center">
                            <img src="/logo.svg" alt="Konfetti" style={{ height: 150 }} />
                        </Grid>
                        <EmailInput email={state.email} setEmail={(email) => setState({ ...state, email })} autoFocus />
                        <PasswordInput
                            password={state.password}
                            setPassword={(password) => setState({ ...state, password })}
                            autoComplete="current-password"
                        />
                        <span>
                            <Button
                                variant="text"
                                color="primary"
                                sx={{ ml: 0 }}
                                size="small"
                                onClick={() => setState({ ...state, resetPassword: true })}
                            >
                                Passwort vergessen?
                            </Button>
                        </span>
                        {renderPasswordForget()}
                        <LoadingButton
                            type="submit"
                            size="large"
                            fullWidth
                            loading={loading}
                            disabled={!isFormValid()}
                            variant="contained"
                        >
                            Anmelden
                        </LoadingButton>
                        <Divider flexItem />
                        <Typography variant="body2" align="center">
                            Noch kein Konto?{' '}
                            <Link component={NavLink} to="/register" underline="hover">
                                Hier registrieren
                            </Link>
                            .
                        </Typography>
                    </Stack>
                </Paper>
            </form>
        </Box>
    )
}
