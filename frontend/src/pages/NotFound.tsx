import { Box, Container, Typography } from '@mui/material'
import NotFoundSVG from '../assets/NotFoundSVG'

function NotFound() {
  return (
    <Container
      sx={{
        height: '100%',
      }}
    >
      <Box sx={{ maxWidth: 500, mx: 'auto' }}>
        <NotFoundSVG width={'100%'} />
      </Box>
      <Typography variant="h2" component="div" sx={{ textAlign: 'center' }}>
        404: Seite nicht gefunden
      </Typography>
    </Container>
  )
}

export default NotFound
