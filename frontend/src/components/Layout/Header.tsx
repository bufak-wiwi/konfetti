import { sidebarWidth } from '@/config'
import { useAuthentication } from '@/hooks/useAuthentication'
import { useCurrentRoute } from '@/hooks/useCurrentRoute'
import { sidebarAtom } from '@/utils/atoms'
import MenuIcon from '@mui/icons-material/Menu'
import { Toolbar, Typography } from '@mui/material'
import MuiAppBar, { AppBarProps as MuiAppBarProps } from '@mui/material/AppBar'
import IconButton from '@mui/material/IconButton'
import { styled } from '@mui/material/styles'
import { useAtom } from 'jotai'
import ConferenceSelection from './ConferenceSelection'
import ProfileButton from './ProfileButton'

interface AppBarProps extends MuiAppBarProps {
    open?: boolean
}

const AppBar = styled(MuiAppBar, {
    shouldForwardProp: (prop) => prop !== 'open',
})<AppBarProps>(({ theme, open }) => ({
    zIndex: theme.zIndex.drawer + 1,
    transition: theme.transitions.create(['width', 'margin'], {
        easing: theme.transitions.easing.sharp,
        duration: theme.transitions.duration.leavingScreen,
    }),
    ...(open && {
        marginLeft: sidebarWidth,
        width: `calc(100% - ${sidebarWidth}px)`,
        transition: theme.transitions.create(['width', 'margin'], {
            easing: theme.transitions.easing.sharp,
            duration: theme.transitions.duration.enteringScreen,
        }),
    }),
}))

export default function Header() {
    const [open, setOpen] = useAtom(sidebarAtom)
    const route = useCurrentRoute()
    const { user } = useAuthentication()

    return (
        <AppBar position="fixed" open={open} enableColorOnDark>
            <Toolbar>
                <IconButton
                    color="inherit"
                    aria-label="open drawer"
                    onClick={() => setOpen(true)}
                    edge="start"
                    sx={{
                        marginRight: '36px',
                        ...(open && { display: 'none' }),
                    }}
                >
                    <MenuIcon />
                </IconButton>
                <Typography variant="h6" noWrap component="div" sx={{ flexGrow: 1 }}>
                    {route?.title || 'Konfetti'}
                </Typography>
                {user && <ConferenceSelection />}
                <ProfileButton />
            </Toolbar>
        </AppBar>
    )
}
