import { Box, Typography } from '@mui/material'
import { messages } from '@/config'

function LoaderErrorBoundaryFallback() {
  return (
    <Box>
      <Typography variant="h5">{messages.loader.fail}</Typography>
    </Box>
  )
}

export default LoaderErrorBoundaryFallback
