import React from 'react'
import { useLocation, useNavigate } from 'react-router-dom'
import { AccountTree, DarkMode, LightMode, Logout } from '@mui/icons-material'
import {
  Avatar,
  Button,
  Divider,
  IconButton,
  ListItemIcon,
  Menu,
  MenuItem,
  Switch,
  Tooltip,
} from '@mui/material'
import { useDarkMode } from '@/store/useDarkMode'
import { useAuthentication } from '../../hooks/useAuthentication'

export default function ProfileButton() {
  const navigate = useNavigate()
  const location = useLocation()
  const { darkMode, toggleDarkMode } = useDarkMode()
  const { user, logout } = useAuthentication()

  // Menu
  const [anchorEl, setAnchorEl] = React.useState<null | HTMLElement>(null)
  const open = Boolean(anchorEl)
  const handleClick = (event: React.MouseEvent<HTMLButtonElement>) => {
    setAnchorEl(event.currentTarget)
  }
  const handleClose = () => setAnchorEl(null)

  if (location.pathname === '/login' || location.pathname === '/register') {
    return (
      <Button color="inherit" onClick={() => navigate('/')}>
        Startseite
      </Button>
    )
  }

  if (!user) {
    return (
      <Button color="inherit" onClick={() => navigate('/login', { state: { from: location } })}>
        Anmelden
      </Button>
    )
  }

  return (
    <React.Fragment>
      {user.firstName} {user.lastName}
      <Tooltip title="Kontoeinstellungen">
        <IconButton size="large" color="inherit" onClick={handleClick}>
          <Avatar
            sx={{ backgroundColor: 'primary', width: 40, height: 40 }}
            alt={user.firstName || undefined}
          />
        </IconButton>
      </Tooltip>
      <Menu
        anchorEl={anchorEl}
        open={open}
        onClose={handleClose}
        onClick={handleClose}
        PaperProps={{
          elevation: 0,
          sx: {
            overflow: 'visible',
            filter: 'drop-shadow(0px 2px 8px rgba(0,0,0,0.32))',
            mt: 1.5,
            '& .MuiAvatar-root': {
              width: 32,
              height: 32,
              ml: -0.5,
              mr: 1,
            },
            '&:before': {
              content: '""',
              display: 'block',
              position: 'absolute',
              top: 0,
              right: 24,
              width: 10,
              height: 10,
              bgcolor: 'background.paper',
              transform: 'translateY(-50%) rotate(45deg)',
              zIndex: 0,
            },
          },
        }}
        transformOrigin={{ horizontal: 'right', vertical: 'top' }}
        anchorOrigin={{ horizontal: 'right', vertical: 'bottom' }}
      >
        <MenuItem onClick={() => navigate(`/user/${user.id}`)}>
          <Avatar sx={{ backgroundColor: 'secondary' }} alt={user.firstName || undefined} />
          {user.firstName} {user.lastName}
        </MenuItem>
        <Divider />
        <MenuItem
          onClick={(e) => {
            e.stopPropagation()
            toggleDarkMode()
          }}
        >
          <ListItemIcon>
            {darkMode ? <DarkMode fontSize="small" /> : <LightMode fontSize="small" />}
          </ListItemIcon>
          Darkmode
          <Switch checked={!!darkMode} />
        </MenuItem>
        <MenuItem onClick={() => navigate(`/bet/${user.id}`)}>
          <ListItemIcon>
            <AccountTree fontSize="small" />
          </ListItemIcon>
          Mein Tipp
        </MenuItem>
        <Divider />
        <MenuItem onClick={logout}>
          <ListItemIcon>
            <Logout fontSize="small" />
          </ListItemIcon>
          Abmelden
        </MenuItem>
      </Menu>
    </React.Fragment>
  )
}
