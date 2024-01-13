import Typography from '@mui/material/Typography'
import { useParams } from 'react-router-dom'

export default function SpeakingList() {
    const params = useParams()
    const conferenceId = params.conferenceId
    return (
        <>
            <Typography variant="h3">Redeliste für ID: {conferenceId}</Typography>
        </>
    )
}
