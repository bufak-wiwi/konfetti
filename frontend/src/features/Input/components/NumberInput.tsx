import { FormControl, FormHelperText, InputLabel, OutlinedInput } from '@mui/material'

type Props = {
  value: number
  label: string
  setValue: (value: number) => void
  validation?: (value: number) => boolean
  min?: number
  max?: number
  size?: 'medium' | 'small'
  disabled?: boolean
  helperText?: string
}

export function NumberInput(props: Props) {
  const {
    value,
    setValue,
    label,
    min = 0,
    max = 9999,
    size = 'medium',
    disabled = false,
    validation = () => true,
    helperText = '',
  } = props

  return (
    <FormControl fullWidth variant="outlined">
      <InputLabel htmlFor={label}>{label}</InputLabel>
      <OutlinedInput
        id={label}
        type="number"
        size={size}
        error={value !== 0 && !validation(value)}
        inputProps={{ min, max }}
        value={value}
        onChange={(e) => setValue(parseInt(e.currentTarget.value) || 0)}
        disabled={disabled}
        label={label}
      />
      {value !== 0 && !validation(value) && (
        <FormHelperText error variant="outlined">
          {helperText}
        </FormHelperText>
      )}
    </FormControl>
  )
}
