import { LoadingOverlay } from '@/features/Feedback'
import { useCurrentConference } from '@/hooks/useCurrentConference'
import Typography from '@mui/material/Typography'

export default function SpeakingList() {
    const { conference, isLoading } = useCurrentConference()

    if (isLoading) return <LoadingOverlay loading />

    return (
        <>
            <Typography variant="h3">Redeliste für ID: {conference?.name}</Typography>
        </>
    )
}
