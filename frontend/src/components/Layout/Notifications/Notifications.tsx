import CloseIcon from '@mui/icons-material/Close'
import { IconButton } from '@mui/material'
import { SnackbarProvider } from 'notistack'
import { notifications } from '@/config'
import { useNotifications } from '@/features/Feedback'
import Notifier from './Notifier'

function Notifications() {
  const closeNotification = useNotifications((state) => state.closeNotification)
  return (
    <SnackbarProvider
      maxSnack={notifications.maxSnack}
      action={(snackbarId) => (
        <IconButton onClick={() => closeNotification(snackbarId)} color="inherit">
          <CloseIcon />
        </IconButton>
      )}
    >
      <Notifier />
    </SnackbarProvider>
  )
}

export default Notifications
