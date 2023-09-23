import { sidebarWidth } from '@/config'
import { adminNavItems, authenticatedNavItems, publicNavItems } from '@/config/routes'
import { sidebarAtom } from '@/utils/atoms'
import { isMobile, isNavActive } from '@/utils/functions'
import ChevronLeftIcon from '@mui/icons-material/ChevronLeft'
import Divider from '@mui/material/Divider'
import MuiDrawer from '@mui/material/Drawer'
import IconButton from '@mui/material/IconButton'
import List from '@mui/material/List'
import ListItem from '@mui/material/ListItem'
import ListItemIcon from '@mui/material/ListItemIcon'
import ListItemText from '@mui/material/ListItemText'
import { CSSObject, Theme, styled } from '@mui/material/styles'
import { useAtom } from 'jotai'
import { useLocation, useNavigate } from 'react-router-dom'
import { useAuthentication } from '../../hooks/useAuthentication'

const openedMixin = (theme: Theme): CSSObject => ({
  width: sidebarWidth,
  transition: theme.transitions.create('width', {
    easing: theme.transitions.easing.sharp,
    duration: theme.transitions.duration.enteringScreen,
  }),
  overflowX: 'hidden',
})

const closedMixin = (theme: Theme): CSSObject => ({
  transition: theme.transitions.create('width', {
    easing: theme.transitions.easing.sharp,
    duration: theme.transitions.duration.leavingScreen,
  }),
  overflowX: 'hidden',
  width: '0px', //`calc(${theme.spacing(7)} + 1px)`,
  [theme.breakpoints.up('sm')]: {
    width: `calc(${theme.spacing(9)} + 1px)`,
  },
})

export const SidebarHeader = styled('div')(({ theme }) => ({
  display: 'flex',
  alignItems: 'center',
  justifyContent: 'flex-end',
  padding: theme.spacing(0, 1),
  // necessary for content to be below app bar
  ...theme.mixins.toolbar,
}))

const Drawer = styled(MuiDrawer, { shouldForwardProp: (prop) => prop !== 'open' })(
  ({ theme, open }) => ({
    width: sidebarWidth,
    flexShrink: 0,
    whiteSpace: 'nowrap',
    boxSizing: 'border-box',
    ...(open && {
      ...openedMixin(theme),
      '& .MuiDrawer-paper': openedMixin(theme),
    }),
    ...(!open && {
      ...closedMixin(theme),
      '& .MuiDrawer-paper': closedMixin(theme),
    }),
  }),
)

export default function Sidebar() {
  const [open, setOpen] = useAtom(sidebarAtom)
  const location = useLocation()
  const navigate = useNavigate()
  const { isAdmin, user } = useAuthentication()

  const onClick = (e: React.MouseEvent<HTMLLIElement, MouseEvent>, to: string) => {
    e.stopPropagation()
    if (isMobile) {
      setOpen(false)
    }
    navigate(to)
  }


  return (
    <Drawer variant="permanent" anchor="left" open={open} onClose={() => setOpen(false)}>
      <SidebarHeader>
        <IconButton onClick={() => setOpen(false)}>
          <ChevronLeftIcon />
        </IconButton>
      </SidebarHeader>
      <Divider />
      <List>
        {publicNavItems.map(({ path, exact, Icon, title }) => (
          <ListItem key={path} onClick={(e) => onClick(e, path)}>
            <ListItemIcon>
              <Icon color={isNavActive(path, exact, location.pathname) ? 'primary' : 'inherit'} />
            </ListItemIcon>
            <ListItemText
              primary={title}
              primaryTypographyProps={{
                color: isNavActive(path, exact, location.pathname) ? 'primary' : 'inherit',
              }}
            />
          </ListItem>
        ))}
        {user && (
          <div>
            {authenticatedNavItems.map(({ path, exact, Icon, title }) => (
              <ListItem key={path} onClick={(e) => onClick(e, path)}>
                <ListItemIcon>
                  <Icon
                    color={isNavActive(path, exact, location.pathname) ? 'primary' : 'inherit'}
                  />
                </ListItemIcon>
                <ListItemText
                  primary={title}
                  primaryTypographyProps={{
                    color: isNavActive(path, exact, location.pathname) ? 'primary' : 'inherit',
                  }}
                />
              </ListItem>
            ))}
          </div>
        )}
        {isAdmin && (
          <div>
            <Divider />
            {adminNavItems.map(({ path, exact, Icon, title }) => (
              <ListItem key={path} onClick={(e) => onClick(e, path)}>
                <ListItemIcon>
                  <Icon
                    color={isNavActive(path, exact, location.pathname) ? 'primary' : 'inherit'}
                  />
                </ListItemIcon>
                <ListItemText
                  primary={title}
                  primaryTypographyProps={{
                    color: isNavActive(path, exact, location.pathname) ? 'primary' : 'inherit',
                  }}
                />
              </ListItem>
            ))}
          </div>
        )}
      </List>
    </Drawer>
  )
}
