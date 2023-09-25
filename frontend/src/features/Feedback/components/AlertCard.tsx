import { useState } from 'react'
import CloseIcon from '@mui/icons-material/Close'
import { Alert, AlertTitle, Button, Card, Collapse, IconButton } from '@mui/material'
import { SxProps, Theme } from '@mui/system'

interface Props {
  children?: React.ReactNode
  severity: 'error' | 'warning' | 'info' | 'success'
  title?: string
  body: string
  sx?: SxProps<Theme>
  onClick?: () => void
  buttonTitle?: string
  dismissable?: boolean
}
export function AlertCard(props: Props) {
  const { children, body, severity, title, buttonTitle, sx, onClick, dismissable } = props
  const [open, setOpen] = useState(true)

  return (
    <Collapse in={open}>
      <Card sx={sx}>
        <Alert
          severity={severity}
          action={
            dismissable && (
              <IconButton
                aria-label="close"
                color="inherit"
                size="small"
                onClick={() => {
                  setOpen(false)
                }}
              >
                <CloseIcon fontSize="inherit" />
              </IconButton>
            )
          }
        >
          {title && <AlertTitle>{title}</AlertTitle>}
          {body}
          {children}
          {onClick && buttonTitle && (
            <>
              <br />
              <br />
              <Button variant="outlined" color={severity} onClick={onClick}>
                {buttonTitle}
              </Button>
            </>
          )}
        </Alert>
      </Card>
    </Collapse>
  )
}
