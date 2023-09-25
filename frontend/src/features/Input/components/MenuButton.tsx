import React, { ReactElement, useState } from 'react'
import MoreIcon from '@mui/icons-material/MoreVert'
import { IconButton, IconProps, ListItemIcon, ListItemText, Menu, MenuItem } from '@mui/material'

interface MenuOption {
  label: string
  onClick: () => void
  icon?: ReactElement<IconProps>
  disabled?: boolean
}

interface Props {
  disabled?: boolean
  options: MenuOption[]
}

export function MenuButton({ disabled, options }: Props) {
  const [anchorEl, setAnchorEl] = useState<null | HTMLElement>(null)
  const open = Boolean(anchorEl)
  const handleClick = (event: React.MouseEvent<HTMLElement>) => {
    setAnchorEl(event.currentTarget)
  }
  const handleClose = (onClick?: () => void) => {
    setAnchorEl(null)
    onClick && onClick()
  }

  const hasIcons = React.useMemo(() => options.some((x) => x.icon), [options])

  return (
    <React.Fragment>
      <IconButton disabled={disabled} onClick={handleClick}>
        <MoreIcon />
      </IconButton>
      <Menu anchorEl={anchorEl} open={open} onClose={() => handleClose()}>
        {options.map(({ label, icon, onClick, disabled: disabled_item }) => (
          <MenuItem key={label} onClick={() => handleClose(onClick)} disabled={disabled_item}>
            {hasIcons && <ListItemIcon>{icon}</ListItemIcon>}
            <ListItemText>{label}</ListItemText>
          </MenuItem>
        ))}
      </Menu>
    </React.Fragment>
  )
}
