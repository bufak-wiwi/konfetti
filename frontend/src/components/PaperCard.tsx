import React from 'react'
import { Paper, Stack } from '@mui/material'
import { isMobile } from '@/utils/functions'
import DetailsToolbar from './DetailsToolbar'

type Props = {
  title?: string
  editing?: boolean
  hideCancel?: boolean
  onEditCancel?: () => void
  onEdit?: () => void
  invalid?: boolean
  onSave?: () => void
  children?: React.ReactNode
  CustomActions?: React.ReactNode
  TitleButton?: React.ReactNode
  hideTitleButton?: boolean
  archived?: boolean
  loading?: boolean
}

export default function PaperCard(props: Props) {
  const {
    title,
    editing,
    hideCancel,
    onEditCancel = () => console.error("onEditCancel isn't defined"),
    onEdit,
    invalid,
    onSave = () => console.error("onSave isn't defined"),
    children,
    CustomActions,
    TitleButton,
    hideTitleButton,
    archived,
    loading,
  } = props

  return (
    <Paper elevation={3} sx={{ mt: 0, mb: 16, mx: isMobile ? -2 : 0, px: 0 }}>
      {title && (
        <DetailsToolbar
          title={title}
          editing={editing}
          invalid={invalid}
          hideCancel={hideCancel}
          onEditCancel={onEditCancel}
          onEdit={onEdit}
          onSave={onSave}
          loading={loading}
          CustomActions={CustomActions}
          TitleButton={TitleButton}
          hideTitleButton={hideTitleButton}
          archived={archived}
        />
      )}
      <Stack spacing={2} style={{ padding: 16 }}>
        {children && children}
      </Stack>
    </Paper>
  )
}
