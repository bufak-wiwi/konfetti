import { TextField } from '@mui/material'

type Props = {
  value: string
  label: string
  setValue: (text: string) => void
  validation?: (text: string) => boolean
  autoFocus?: boolean
  disabled?: boolean
  helperText?: string
}

export function TextInput(props: Props) {
  const {
    value,
    setValue,
    label,
    disabled = false,
    autoFocus = false,
    validation = () => true,
    helperText = '',
  } = props

  return (
    <TextField
      label={label}
      fullWidth
      error={value !== '' && !validation(value)}
      autoComplete=""
      value={value}
      helperText={value !== '' && !validation(value) ? helperText : ''}
      variant="outlined"
      onChange={(e) => setValue(e.currentTarget.value)}
      disabled={disabled}
      autoFocus={autoFocus}
    />
  )
}
