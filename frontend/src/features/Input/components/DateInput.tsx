import { DateTimePicker, DatePicker } from '@mui/x-date-pickers'

type Props = {
    value: string
    setValue: (value: string) => void
    label: string
    withTime?: boolean
    autoFocus?: boolean
    disabled?: boolean
}

export default function DateInput(props: Props) {
    const { value, setValue, label, withTime = false, disabled = false, autoFocus = false } = props

    if (withTime) {
        return (
            <DateTimePicker
                label={label}
                value={new Date(value)}
                onChange={(date) => setValue((date || new Date()).toString())}
                disabled={disabled}
                autoFocus={autoFocus}
                ampm={false}
            />
        )
    }

    return (
        <DatePicker
            label={label}
            value={new Date(value)}
            onChange={(date) => setValue((date || new Date()).toString())}
            disabled={disabled}
            autoFocus={autoFocus}
        />
    )
}
