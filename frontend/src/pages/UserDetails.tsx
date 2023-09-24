import { useUpdateUser, useUser } from '@/api'
import PaperCard from '@/components/PaperCard'
import { AlertCard, Loading, useNotifications } from '@/features/Feedback'
import { EmailInput, NumberInput, TextInput } from '@/features/Input'
import DateInput from '@/features/Input/components/DateInput'
import { useAuthentication } from '@/hooks/useAuthentication'
import { useEffect, useState } from 'react'
import { Navigate, useParams } from 'react-router-dom'

export default function UserDetails() {
    const addNotification = useNotifications((state) => state.addNotification)
    const { user, isAdmin } = useAuthentication()
    const params = useParams()
    const { data, isError, isLoading } = useUser(params.id)
    const { mutateAsync, isLoading: isUpdateLoading } = useUpdateUser(params.id)

    const [userCopy, setUserCopy] = useState(data)
    const [editing, setEditing] = useState(false)

    useEffect(() => {
        setUserCopy(data)
    }, [data])

    const onEditCancel = () => {
        setUserCopy(data)
        setEditing(false)
    }

    const onSave = () => {
        // TODO: Validate user
        if (!userCopy) return

        mutateAsync(userCopy)
            .then(() => {
                addNotification({
                    message: 'Der Benutzer wurde erfolgreich gespeichert.',
                    options: { variant: 'success' },
                })
                setEditing(false)
            })
            .catch((err) => {
                console.log('Got err', err)
                addNotification({
                    message: 'Der Benutzer konnte nicht gespeichert werden.',
                    options: { variant: 'error' },
                })
            })
    }

    if (user?.id != params.id && !isAdmin) {
        return <Navigate to="/access-denied" />
    }

    if (isLoading) return <Loading />

    if (isError || !data || !userCopy) {
        return (
            <AlertCard
                severity="error"
                title="Nutzer Infos konnten nicht geladen werden"
                body={`Nutzer mit der Id ${params.id} konnte nicht geladen werden. Bitte versuche es später noch einmal.`}
            />
        )
    }

    return (
        <PaperCard
            title={`Profil von ${data?.firstname} ${data.lastname}`}
            editing={editing}
            onEdit={() => setEditing(true)}
            loading={isUpdateLoading}
            onSave={onSave}
            onEditCancel={onEditCancel}
        >
            <TextInput
                label="Vorname"
                value={userCopy?.firstname}
                setValue={(firstname) => setUserCopy({ ...userCopy, firstname })}
                disabled={!editing}
            />
            <TextInput
                label="Nachname"
                value={userCopy?.lastname}
                setValue={(lastname) => setUserCopy({ ...userCopy, lastname })}
                disabled={!editing}
            />
            <EmailInput email={userCopy?.email} setEmail={(email) => setUserCopy({ ...userCopy, email })} disabled />
            <DateInput
                label="Geburtstag"
                value={userCopy?.birthday}
                setValue={(birthday) => setUserCopy({ ...userCopy, birthday })}
                disabled={!editing}
            />
            <NumberInput
                label="Fachschaftsrat"
                value={userCopy?.councilId}
                setValue={(councilId) => setUserCopy({ ...userCopy, councilId })}
                disabled={!editing}
            />
            <AlertCard
                severity="info"
                dismissable
                title="Diese Seite ist noch in der Entwicklung"
                body="Die Seite ist noch nicht fertig und wird noch weiterentwickelt."
            />
        </PaperCard>
    )
}
