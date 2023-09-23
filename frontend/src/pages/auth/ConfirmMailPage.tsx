import { useEffect } from 'react'
import { Navigate, useNavigate, useSearchParams } from 'react-router-dom'
import { AlertCard, Loading, useNotifications } from '@/features/Feedback'
import { useAuthentication } from '@/hooks/useAuthentication'

export default function ConfirmMailPage() {
    const navigate = useNavigate()
    const addNotification = useNotifications((state) => state.addNotification)

    const { user, loading, confirmEmail } = useAuthentication()
    const [searchParams] = useSearchParams()
    const token = searchParams.get('token')
    const userId = searchParams.get('userId')

    useEffect(() => {
        if (user?.status === 'confirmed' && user.id === Number(userId)) {
            addNotification({
                message: 'E-Mail Adresse wurde bereits bestätigt',
                options: { variant: 'success' },
            })
        } else if (!token || !userId) {
            addNotification({ message: 'Ungültiger Link', options: { variant: 'error' } })
        } else {
            confirmEmail({ emailToken: token, userId: parseInt(userId) })
        }
        // eslint-disable-next-line react-hooks/exhaustive-deps
    }, [])

    if (loading) {
        return <Loading />
    }

    if (!token || !userId) {
        return <Navigate to="/login" replace />
    }

    return (
        <AlertCard
            title="E-Mail erfolgreich bestätigt"
            body="Deine E-Mail-Adresse wurde erfolgreich bestätigt"
            severity="success"
            buttonTitle="Jetzt Anmelden"
            onClick={() => navigate('/')}
        />
    )
}
