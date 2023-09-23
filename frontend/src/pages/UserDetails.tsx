import { useEffect, useState } from 'react'
import { Navigate, useParams } from 'react-router-dom'
import { useUpdateUser, useUser } from '@/api'
import PaperCard from '@/components/PaperCard'
import { AlertCard, Loading, useConfirm, useNotifications } from '@/features/Feedback'
import { EmailInput, TextInput } from '@/features/Input'
import { useAuthentication } from '@/hooks/useAuthentication'

export default function UserDetails() {
  const confirm = useConfirm((state) => state.confirmDialog)
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
    if (!userCopy) return

    confirm(
      `Soll der Benutzer ${userCopy.firstName} gespeichert werden? Dieser wird dabei von allen Geräten ausgeloggt.`,
      () => {
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
      },
    )
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
        title={`Profil von ${data?.firstName} ${data.lastName}`}
        editing={editing}
        onEdit={isAdmin ? () => setEditing(true) : undefined}
        loading={isUpdateLoading}
        onSave={onSave}
        onEditCancel={onEditCancel}
      >
        {!isAdmin && (
          <AlertCard
            severity="info"
            dismissable
            title="Diese Seite ist noch in der Entwicklung"
            body="Die Seite ist noch nicht fertig und wird noch weiterentwickelt."
          />
        )}
        <TextInput
          label="Vorname"
          value={userCopy?.firstName}
          setValue={(firstName) => setUserCopy({ ...userCopy, firstName })}
          disabled={!editing}
        />
        <TextInput
          label="Nachname"
          value={userCopy?.lastName}
          setValue={(lastName) => setUserCopy({ ...userCopy, lastName })}
          disabled={!editing}
        />
        <EmailInput
          email={userCopy?.email}
          setEmail={(email) => setUserCopy({ ...userCopy, email })}
          disabled={!editing}
        />
      </PaperCard>

  )
}
