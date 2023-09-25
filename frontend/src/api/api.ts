import axios from 'axios'
import { Notification } from '@/features/Feedback'
import { useAuthenticationStore } from '@/store/useAuthenticationStore'

export const api = axios.create({
  baseURL: '/api',
})

export const setupInterceptors = (
  navigate: (path: string) => void,
  addNotification: (notification: Partial<Notification>) => void,
) => {
  api.interceptors.response.use(
    (response) => response,
    (error) => {
      if (error.response?.status === 401) {
        useAuthenticationStore.setState({ user: null, isAdmin: false })
        addNotification({
          message: 'Session abgelaufen. Bitte melde dich erneut an',
          options: { variant: 'error' },
        })
        navigate('/login')
      } else if (error.response?.status === 403) {
        addNotification({
          message: 'Fehlende Berechtigung',
          options: { variant: 'error' },
        })
        navigate('/access-denied')
      }
      return Promise.reject(error)
    },
  )
}

export const ejectInterceptors = () => api.interceptors.response.clear()
