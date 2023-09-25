import { isMobile } from '@/utils/functions'
import { SnackbarType } from '@/utils/types'

export const title = 'Konfetti'

export const email = 'luk.corona@gmail.com'

export const repository = 'https://github.com/bufak-wiwi/konfetti'

export const notifications: SnackbarType = {
  options: {
    anchorOrigin: {
      vertical: 'bottom',
      horizontal: 'center',
    },
    autoHideDuration: 5000,
  },
  maxSnack: isMobile ? 3 : 4,
}


export const sidebarWidth = 240
