import React from 'react'
import CloseIcon from '@mui/icons-material/Close'
import {
  Button,
  Dialog,
  DialogActions,
  DialogTitle,
  IconButton,
  Slide,
  Toolbar,
  Typography,
  useMediaQuery,
} from '@mui/material'
import AppBar from '@mui/material/AppBar'
import DialogContent from '@mui/material/DialogContent'
import { TransitionProps } from '@mui/material/transitions'
import { useCustomTheme } from '@/hooks/useCustomTheme'

interface Props {
  children: React.ReactElement
  open: boolean
  title: string
  onClose: () => void
  SaveButton: React.ReactNode
}

const Transition = React.forwardRef(function Transition(
  props: TransitionProps & {
    children: React.ReactElement
  },
  ref: React.Ref<unknown>,
) {
  return <Slide direction="up" ref={ref} {...props} />
})

export function FormDialog(props: Props) {
  const { children, open, title, onClose, SaveButton } = props

  const theme = useCustomTheme()
  const fullScreen = useMediaQuery(theme.breakpoints.down('md'))

  return (
    <Dialog
      open={open}
      onClose={onClose}
      fullScreen={fullScreen}
      fullWidth
      TransitionComponent={Transition}
      keepMounted
    >
      {fullScreen ? (
        <AppBar
          sx={{ position: 'relative', backgroundColor: (theme) => theme.palette.primary.dark }}
        >
          <Toolbar>
            <IconButton edge="start" color="inherit" onClick={onClose} aria-label="close">
              <CloseIcon />
            </IconButton>
            <Typography sx={{ ml: 2, flex: 1 }} variant="h6" component="div">
              {title}
            </Typography>
            {SaveButton}
          </Toolbar>
        </AppBar>
      ) : (
        <DialogTitle>{title}</DialogTitle>
      )}
      <DialogContent>
        <form>{children}</form>
      </DialogContent>
      <DialogActions>
        <Button onClick={onClose}>Abbrechen</Button>
        {SaveButton}
      </DialogActions>
    </Dialog>
  )
}
