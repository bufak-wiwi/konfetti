import { useConferenceList } from '@/api'
import { SelectInput } from '@/features/Input'
import { conferenceIdAtom } from '@/utils/atoms'
import { useAtom } from 'jotai'
import { useNavigate } from 'react-router-dom'

export default function ConferenceSelection() {
    const navigate = useNavigate()

    const { data } = useConferenceList()
    const [conferenceId, setConferenceId] = useAtom(conferenceIdAtom)

    const onConferenceChange = (id: number) => {
        setConferenceId(id)
        navigate('/')
    }

    if (!data) return null

    return (
        <div style={{ flexGrow: 0, marginRight: 16 }}>
            <SelectInput
                label=""
                options={data.map((conf) => ({ value: conf.id, label: conf.name }))}
                value={conferenceId}
                size="small"
                setValue={onConferenceChange}
            />
        </div>
    )
}
