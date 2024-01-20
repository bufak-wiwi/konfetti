import { FormControl, InputLabel, MenuItem, Select } from '@mui/material'
import isMobile from 'is-mobile'

type Props<T> = {
    label: string
    value: T | undefined
    options: { value: T; label?: string; disabled?: boolean }[]
    disabled?: boolean
    size?: 'small' | 'medium'
    setValue: (value: T) => void
}

export function SelectInput<T extends string | number | boolean>(props: Props<T>) {
    const { label, value, options, disabled, setValue: onChange, size } = props

    return (
        <FormControl fullWidth variant="outlined">
            <InputLabel htmlFor={label}>{label}</InputLabel>
            <Select
                native={isMobile()}
                label={label}
                id={label}
                size={size}
                value={value ? value : ''}
                disabled={disabled}
                onChange={(e) => onChange(e.target.value as T)}
            >
                {isMobile() && <option aria-label="None" value="" />}
                {options.map((option) =>
                    isMobile() ? (
                        <option
                            value={option.value as string}
                            disabled={option.disabled as boolean}
                            key={option.value as string}
                        >
                            {option.label ? option.label : option.value}
                        </option>
                    ) : (
                        <MenuItem
                            value={option.value as string}
                            disabled={option.disabled}
                            key={option.value as string}
                        >
                            {option.label ? option.label : option.value}
                        </MenuItem>
                    )
                )}
            </Select>
        </FormControl>
    )
}
