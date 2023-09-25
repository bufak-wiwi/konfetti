import { Box, Container, Typography } from '@mui/material'
import AccessDeniedSVG from '../assets/AccessDeniedSVG'

function NotFound() {
  return (
    <Container
      sx={{
        height: '100%',
      }}
    >
      <Box sx={{ maxWidth: 500, mx: 'auto' }}>
        <AccessDeniedSVG width={'100%'} />
      </Box>
      <Typography variant="h2" component="div" sx={{ textAlign: 'center' }}>
        403: Fehlende Berechtigungen
      </Typography>
    </Container>
  )
}

export default NotFound
