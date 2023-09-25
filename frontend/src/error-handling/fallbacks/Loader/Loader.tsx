import { Box, Typography } from '@mui/material'

function LoaderErrorBoundaryFallback() {
  return (
    <Box>
      <Typography variant="h5">Seite konnte nicht geladen werden</Typography>
    </Box>
  )
}

export default LoaderErrorBoundaryFallback
