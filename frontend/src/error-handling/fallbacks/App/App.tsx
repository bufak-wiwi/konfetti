import EmailIcon from '@mui/icons-material/Email'
import RestartIcon from '@mui/icons-material/RestartAlt'
import { Box, Button, Paper, Typography } from '@mui/material'
import { email } from '@/config'

function AppErrorBoundaryFallback() {
  return (
    <Box sx={{ width: '100%', height: '100%' }}>
      <Paper sx={{ p: 5, mx: 'auto', mt: 4, maxWidth: 500 }}>
        <Typography variant="h5" component="h3">
          Oooops... Sorry, I guess, something went wrong. You can:
        </Typography>
        <Button
          startIcon={<EmailIcon />}
          variant="outlined"
          target="_blank"
          rel="noreferrer"
          href={`mailto: ${email}`}
          sx={{ my: 3 }}
        >
          {`contact with author by this email - ${email}`}
        </Button>
        <Typography component="h6">or</Typography>
        <Button
          startIcon={<RestartIcon />}
          sx={{ mt: 3 }}
          variant="outlined"
          onClick={window.location.reload}
        >
          Press here to reset the application
        </Button>
      </Paper>
    </Box>
  )
}

export default AppErrorBoundaryFallback
