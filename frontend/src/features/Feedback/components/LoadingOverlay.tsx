import { Backdrop } from '@mui/material'
import CircularProgress from '@mui/material/CircularProgress'

interface Props {
  loading: boolean
}

export function LoadingOverlay(props: Props = { loading: true }) {
  return (
    <Backdrop
      sx={{ color: '#fff', zIndex: (theme) => theme.zIndex.drawer + 1 }}
      open={props.loading}
    >
      <CircularProgress color="inherit" />
    </Backdrop>
  )
}
