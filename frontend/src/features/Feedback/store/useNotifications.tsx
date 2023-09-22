import type { OptionsObject, SnackbarKey, SnackbarMessage } from 'notistack'
import create from 'zustand'
import { notifications as notificationsDefaults } from '@/config'

export interface Notification {
  message: SnackbarMessage
  options: OptionsObject
  dismissed: boolean
}

interface NotificationState {
  notifications: Notification[]
  addNotification: (notification: Partial<Notification>) => SnackbarKey
  closeNotification: (key: SnackbarKey, dismissAll?: boolean) => void
  removeNotification: (key: SnackbarKey) => void
}

export const useNotifications = create<NotificationState>((set) => ({
  notifications: [],
  addNotification: (notification) => {
    const id = notification.message?.toString() || 'default' // use message as key to prevent duplicate renders
    set((state) => ({
      notifications: [
        ...state.notifications,
        {
          ...notification,
          message: notification.message,
          dismissed: false,
          options: {
            ...notificationsDefaults.options,
            ...notification.options,
            key: id,
          },
        },
      ],
    }))
    return id
  },
  closeNotification: (key, dismissAll = false) => {
    set((state) => ({
      notifications: state.notifications.map((x) =>
        dismissAll || x.options.key === key ? { ...x, dismissed: true } : { ...x },
      ),
    }))
  },
  removeNotification: (key) =>
    set((state) => ({ notifications: state.notifications.filter((x) => x.options.key !== key) })),
}))
