import React from 'react'
import { Close } from '@mui/icons-material'
import {
  Box,
  Button,
  Dialog,
  DialogActions,
  DialogContent,
  DialogTitle,
  IconButton,
  Slide,
  Theme,
  Typography,
} from '@mui/material'
import { TransitionProps } from '@mui/material/transitions'
import { useConfirm } from '../store/useConfirm'

const Transition = React.forwardRef(function Transition(
  props: TransitionProps & {
    children: React.ReactElement
  },
  ref: React.Ref<unknown>,
) {
  return <Slide direction="up" ref={ref} {...props} />
})

export function ConfirmDialog() {
  const { message, color, onSubmit, close } = useConfirm()

  return (
    <Dialog
      open={Boolean(onSubmit)}
      onClose={close}
      maxWidth="sm"
      fullWidth
      aria-labelledby="confirm-dialog"
      TransitionComponent={Transition}
    >
      <DialogTitle>Bist du dir sicher?</DialogTitle>
      <Box position="absolute" top={0} right={0}>
        <IconButton onClick={close}>
          <Close />
        </IconButton>
      </Box>
      <DialogContent>
        <Typography>{message}</Typography>
      </DialogContent>
      <DialogActions>
        <Button onClick={close} color="primary" variant="outlined">
          Abbrechen
        </Button>
        <Button
          sx={{
            backgroundColor: (theme: Theme) => theme.palette[color].main,
            color: (theme: Theme) => theme.palette[color].contrastText,
          }}
          variant="contained"
          onClick={() => {
            if (onSubmit) {
              onSubmit()
            }
            close()
          }}
        >
          Weiter
        </Button>
      </DialogActions>
    </Dialog>
  )
}
