import React from 'react'
import CancelIcon from '@mui/icons-material/Cancel'
import EditIcon from '@mui/icons-material/Edit'
import SaveIcon from '@mui/icons-material/Save'
import { LoadingButton } from '@mui/lab'
import { Button, Chip, Grid, Toolbar, Tooltip, Typography } from '@mui/material'
import { isMobile } from '@/utils/functions'

type Props = {
    title: string
    editing?: boolean
    hideCancel?: boolean
    onEditCancel?: () => void
    onEdit?: () => void | undefined
    invalid?: boolean
    onSave?: () => void
    CustomActions?: React.ReactNode
    TitleButton?: React.ReactNode
    hideTitleButton?: boolean
    archived?: boolean
    loading?: boolean
}

export default function DetailsToolbar(props: Props) {
    const {
        title,
        editing,
        hideCancel,
        onEditCancel = () => console.error("onEditCancel isn't defined"),
        onEdit,
        invalid,
        onSave = () => console.error("onSave isn't defined"),
        CustomActions,
        TitleButton,
        hideTitleButton,
        archived,
        loading,
    } = props

    const Title = () => (
        <div style={{ flexGrow: 1, display: 'flex' }}>
            <Typography variant="h6">
                {title + ' '}
                {archived && <Chip label="archiviert" variant="outlined" />}
            </Typography>
            {!hideTitleButton && TitleButton !== undefined && TitleButton}
        </div>
    )

    const CancelButton = () => (
        <Tooltip title="Bearbeitung abbrechen">
            <span>
                <Button
                    variant="outlined"
                    color="primary"
                    onClick={() => onEditCancel()}
                    startIcon={<CancelIcon />}
                    style={{ marginRight: 8 }}
                    fullWidth={isMobile}
                >
                    {' '}
                    Abbrechen
                </Button>
            </span>
        </Tooltip>
    )

    const SaveButton = () => (
        <Tooltip title="Änderungen speichern">
            <span>
                <LoadingButton
                    variant="contained"
                    color="primary"
                    disabled={invalid}
                    loading={loading}
                    onClick={() => onSave()}
                    startIcon={<SaveIcon />}
                    fullWidth={isMobile}
                >
                    {' '}
                    Speichern
                </LoadingButton>
            </span>
        </Tooltip>
    )

    const EditButton = () => (
        <Button onClick={() => onEdit && onEdit()} color="primary" variant="contained" startIcon={<EditIcon />}>
            {' '}
            Bearbeiten{' '}
        </Button>
    )

    if (isMobile) {
        return (
            <Toolbar style={{ justifyContent: 'space-between', marginBottom: 16 }}>
                <Grid container spacing={2}>
                    <Grid item xs={12}>
                        <Title />
                    </Grid>
                    {CustomActions && (
                        <Grid item xs={12} sm={12}>
                            {CustomActions}
                        </Grid>
                    )}
                    {editing && (
                        <React.Fragment>
                            {!hideCancel && (
                                <Grid item xs={6}>
                                    <CancelButton />
                                </Grid>
                            )}
                            <Grid item xs={6}>
                                <SaveButton />
                            </Grid>
                        </React.Fragment>
                    )}
                    {!editing && onEdit && <EditButton />}
                </Grid>
            </Toolbar>
        )
    }

    return (
        <Toolbar style={{ justifyContent: 'space-between' }}>
            <Title />
            {CustomActions}
            {editing && (
                <React.Fragment>
                    {!hideCancel && <CancelButton />}
                    <SaveButton />
                </React.Fragment>
            )}
            {!editing && onEdit && <EditButton />}
        </Toolbar>
    )
}
