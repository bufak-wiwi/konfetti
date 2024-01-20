import { useConferenceList } from '@/api'
import { SelectInput } from '@/features/Input'
import { useCurrentRoute } from '@/hooks/useCurrentRoute'
import { conferenceIdAtom } from '@/utils/atoms'
import { useAtom } from 'jotai'
import { generatePath, useNavigate } from 'react-router-dom'

export default function ConferenceSelection() {
    const navigate = useNavigate()
    const { route, params } = useCurrentRoute()

    const { data } = useConferenceList()
    const [conferenceId, setConferenceId] = useAtom(conferenceIdAtom)

    // update the conference id and replace the current conferenceId param if given
    const onConferenceChange = (id: number) => {
        setConferenceId(id)
        navigate(generatePath(route.path, { ...params, conferenceId: id }))
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
