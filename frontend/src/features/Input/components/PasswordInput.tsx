import React, { useState } from 'react'
import { Visibility, VisibilityOff } from '@mui/icons-material'
import {
  FormControl,
  FormHelperText,
  IconButton,
  InputAdornment,
  InputLabel,
  OutlinedInput,
} from '@mui/material'
import { isValidPassword } from '../utils/validation'

type Props = {
  password: string
  setPassword: (password: string) => void
  confirm?: boolean
  isToken?: boolean
  toConfirm?: string
  autoComplete?: string
  disabled?: boolean
}

export function PasswordInput(props: Props) {
  const [showPassword, setShowPassword] = useState(false)
  const {
    password,
    setPassword,
    confirm = false,
    toConfirm = '',
    autoComplete = 'current-password',
    isToken,
    disabled,
  } = props

  const handleMouseDownPassword = (event: React.MouseEvent<HTMLButtonElement>) => {
    event.preventDefault()
  }

  const passwordMatches = () => !confirm || (toConfirm && password === toConfirm)

  const isError = () => {
    return password.length !== 0 && (!isValidPassword(password) || !passwordMatches())
  }

  return (
    <FormControl fullWidth variant="outlined">
      <InputLabel htmlFor={confirm ? 'password-confirm' : 'password'}>
        {confirm ? 'Passwort bestätigen' : isToken ? 'Token' : 'Passwort'}
      </InputLabel>
      <OutlinedInput
        id={confirm ? 'password-confirm' : 'password'}
        type={showPassword ? 'text' : 'password'}
        value={password}
        autoComplete={autoComplete}
        onChange={(e) => setPassword(e.currentTarget.value)}
        error={isError()}
        disabled={disabled}
        label={confirm ? 'Passwort bestätigen' : isToken ? 'Token' : 'Passwort'}
        endAdornment={
          <InputAdornment position="end">
            <IconButton
              aria-label="toggle password visibility"
              onClick={() => setShowPassword(!showPassword)}
              onMouseDown={handleMouseDownPassword}
              edge="end"
            >
              {showPassword ? <Visibility /> : <VisibilityOff />}
            </IconButton>
          </InputAdornment>
        }
      />
      {password !== '' && !confirm && !isValidPassword(password) && (
        <FormHelperText error variant="outlined">
          {isToken ? 'Token' : 'Passwort'} muss zwischen 8 und 32 Zeichen lang sein
        </FormHelperText>
      )}
      {password !== '' && confirm && !passwordMatches() && (
        <FormHelperText error variant="outlined">
          Passwörter stimmen nicht überein
        </FormHelperText>
      )}
    </FormControl>
  )
}
