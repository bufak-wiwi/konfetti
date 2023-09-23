import { useDarkMode } from '@/store/useDarkMode'
import { confettiAtom } from '@/utils/atoms'
import { DarkMode, LightMode, Logout } from '@mui/icons-material'
import CelebrationIcon from '@mui/icons-material/Celebration'
import SentimentVeryDissatisfiedIcon from '@mui/icons-material/SentimentVeryDissatisfied'
import {
    Avatar,
    Button,
    Divider,
    IconButton,
    ListItemIcon,
    ListItemText,
    Menu,
    MenuItem,
    Switch,
    Tooltip,
} from '@mui/material'
import { useAtom } from 'jotai'
import React from 'react'
import { useLocation, useNavigate } from 'react-router-dom'
import { useAuthentication } from '../../hooks/useAuthentication'

export default function ProfileButton() {
    const navigate = useNavigate()
    const location = useLocation()
    const { darkMode, toggleDarkMode } = useDarkMode()
    const [showConfetti, setShowConfetti] = useAtom(confettiAtom)
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
            {user.firstname} {user.lastname}
            <Tooltip title="Kontoeinstellungen">
                <IconButton size="large" color="inherit" onClick={handleClick}>
                    <Avatar
                        sx={{ backgroundColor: 'primary', width: 40, height: 40 }}
                        alt={user.firstname || undefined}
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
                    <Avatar sx={{ backgroundColor: 'secondary' }} alt={user.firstname || undefined} />
                    <ListItemText>
                        {user.firstname} {user.lastname}
                    </ListItemText>
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
                    <ListItemText>Darkmode</ListItemText>
                    <Switch checked={!!darkMode} edge="end" />
                </MenuItem>
                <MenuItem
                    onClick={(e) => {
                        e.stopPropagation()
                        setShowConfetti((bool) => !bool)
                    }}
                >
                    <ListItemIcon>
                        {showConfetti ? (
                            <CelebrationIcon fontSize="small" />
                        ) : (
                            <SentimentVeryDissatisfiedIcon fontSize="small" />
                        )}
                    </ListItemIcon>
                    <ListItemText>Konfetti</ListItemText>
                    <Switch checked={showConfetti} edge="end" />
                </MenuItem>
                <Divider />
                <MenuItem onClick={logout}>
                    <ListItemIcon>
                        <Logout fontSize="small" />
                    </ListItemIcon>
                    <ListItemText>Abmelden</ListItemText>
                </MenuItem>
            </Menu>
        </React.Fragment>
    )
}
