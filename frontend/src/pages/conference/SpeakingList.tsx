import { useSpeakingList } from '@/api'
import { useCurrentConference } from '@/hooks/useCurrentConference'
import { LoadingButton } from '@mui/lab'
import Typography from '@mui/material/Typography'

export default function SpeakingList() {
    const { conference } = useCurrentConference()
    const { data: speakingList, isFetching, refetch } = useSpeakingList()

    return (
        <>
            <Typography variant="h3">Redeliste für ID: {conference?.name}</Typography>
            <LoadingButton loading={isFetching} onClick={() => refetch()}>
                Redeliste aktualisieren
            </LoadingButton>
            <br />
            <ul>
                {speakingList?.map((entry) => (
                    <li>{entry.name}</li>
                ))}
            </ul>
        </>
    )
}
