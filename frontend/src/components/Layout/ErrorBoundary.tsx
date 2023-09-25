import { Alert, AlertTitle, Button, Card, Container } from '@mui/material'
import React, { useState } from 'react'
import { ErrorBoundary as Boundary } from 'react-error-boundary'
import { useNavigate } from 'react-router-dom'

interface Props {
  children: React.ReactNode
}

type ErrorWithCause = Error & { cause?: string }

interface ErrorState {
  error: ErrorWithCause | null
  componentStack: string
}

export default function ErrorBoundary({ children }: Props) {
  const [errorState, setErrorState] = useState<ErrorState>({ error: null, componentStack: '' })
  const navigate = useNavigate()

  const handleError = (error: ErrorWithCause, componentStack: string) => {
    setErrorState({ error, componentStack })
    console.error(error, componentStack)
  }

  const navigateAndResetError = (resetErrorBoundary: () => void) => {
    navigate(-1)
    resetErrorBoundary()
  }

  return (
    <Boundary
      fallbackRender={({ resetErrorBoundary }) => (
        <Container>
          <Card>
            <Alert severity="error">
              <AlertTitle>Ups... Etwas ist schief gelaufen</AlertTitle>
              Hier muss ein Fehler aufgetreten sein. Bitte versuche es später noch einmal oder
              kontaktiere uns mit einer Beschreibung deiner letzten Aktionen und den unten stehenden
              Informationen.
              <pre style={{ whiteSpace: 'pre-wrap', wordWrap: 'break-word' }}>
                {errorState.error && errorState.error.message}
              </pre>
              <div style={{ display: 'flex', justifyContent: 'space-between' }}>
                <Button
                  size="small"
                  color="inherit"
                  variant="text"
                  onClick={() => navigateAndResetError(resetErrorBoundary)}
                >
                  Zurück
                </Button>
              </div>
            </Alert>
          </Card>
        </Container>
      )}
      onError={(error, { componentStack }) => handleError(error as ErrorWithCause, componentStack)}
      resetKeys={['errorState']}
    >
      {children}
    </Boundary>
  )
}
