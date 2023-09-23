import { TextField } from '@mui/material'
import { isValidEmail } from '../utils/validation'

type Props = {
  email: string
  setEmail: (email: string) => void
  autoFocus?: boolean
  disabled?: boolean
}

export function EmailInput(props: Props) {
  const { email, setEmail, disabled = false, autoFocus = false } = props

  return (
    <TextField
      id="email"
      label="E-Mail-Adresse"
      fullWidth
      error={email !== '' && !isValidEmail(email)}
      autoComplete="email"
      value={email}
      helperText={email !== '' && !isValidEmail(email) ? 'Ungültige E-Mail-Adresse' : ''}
      variant="outlined"
      onChange={(e) => setEmail(e.currentTarget.value)}
      disabled={disabled}
      autoFocus={autoFocus}
    />
  )
}
