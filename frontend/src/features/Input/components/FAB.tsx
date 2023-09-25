import AddIcon from '@mui/icons-material/Add'
import EditIcon from '@mui/icons-material/Edit'
import { Fab, Tooltip, Zoom } from '@mui/material'

interface Props {
  type: 'ADD' | 'EDIT'
  onClick: () => void
  show: boolean
  title?: string
}

export function FAB(props: Props) {
  const { type, onClick, show, title } = props

  return (
    <Zoom in={show}>
      <Tooltip
        title={title ? title : type === 'ADD' ? 'Hinzufügen' : 'Bearbeiten'}
        placement="left"
      >
        <Fab
          color="primary"
          onClick={() => onClick()}
          sx={{ position: 'fixed', bottom: 70, right: (theme) => theme.spacing(2) }}
        >
          {type === 'ADD' ? <AddIcon /> : <EditIcon />}
        </Fab>
      </Tooltip>
    </Zoom>
  )
}
