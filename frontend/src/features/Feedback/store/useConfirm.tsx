import create from 'zustand'

export type Color = 'error' | 'success' | 'warning' | 'info' | 'primary' | 'secondary'

type ConfirmDialogStore = {
  message: string
  color: Color
  onSubmit?: () => void
  close: () => void
  confirmDialog: (message: string, onSubmit: () => void, color?: Color) => void
}

export const useConfirm = create<ConfirmDialogStore>((set) => ({
  message: '',
  color: 'primary',
  onSubmit: undefined,
  close: () => set({ onSubmit: undefined, message: '' }),
  confirmDialog: (message: string, onSubmit: () => void, color: Color = 'primary') =>
    set({
      message,
      onSubmit,
      color,
    }),
}))
