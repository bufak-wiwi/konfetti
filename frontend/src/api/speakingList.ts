import { conferenceIdAtom } from '@/utils/atoms'
import { useMutation, useQuery, useQueryClient } from '@tanstack/react-query'
import { useAtomValue } from 'jotai'
import { api } from '.'
import { SpeakingEntry } from '@/utils/types'
import { useNotifications } from '@/features/Feedback'

export const useSpeakingList = () => {
    const conferenceId = useAtomValue(conferenceIdAtom)

    return useQuery(
        ['speakinglist', conferenceId],
        async () => {
            if (!conferenceId) return { data: [] as SpeakingEntry[] }
            return api.get<SpeakingEntry[]>(`/conference/${conferenceId}/speakinglist/`)
        },
        { select: (result) => result.data, staleTime: 5 * 1000 }
    )
}

export const useRaiseHand = () => {
    const conferenceId = useAtomValue(conferenceIdAtom)
    const client = useQueryClient()
    const addNotification = useNotifications((state) => state.addNotification)

    return useMutation(
        (reportType: number) => api.get(`/conference/${conferenceId}/speakinglist/raiseHand/${reportType}`),
        {
            onSuccess: () => {
                client.invalidateQueries(['speakinglist', conferenceId])
                addNotification({ message: 'Redebeitrag hinzugefügt', options: { variant: 'success' } })
            },
            onError: () =>
                addNotification({
                    message: 'Redebeitrag konnte nicht hinzugefügt werden',
                    options: { variant: 'error' },
                }),
        }
    )
}

export const useLowerHand = () => {
    const conferenceId = useAtomValue(conferenceIdAtom)
    const client = useQueryClient()
    const addNotification = useNotifications((state) => state.addNotification)

    return useMutation(
        (reportId: number) => api.get(`/conference/${conferenceId}/speakinglist/lowerHand/${reportId}`),
        {
            onSuccess: () => {
                client.invalidateQueries(['speakinglist', conferenceId])
                addNotification({ message: 'Redebeitrag entfernt', options: { variant: 'success' } })
            },
            onError: () =>
                addNotification({
                    message: 'Redebeitrag konnte nicht entfernt werden',
                    options: { variant: 'error' },
                }),
        }
    )
}

export const useLowerHandAdmin = () => {
    const conferenceId = useAtomValue(conferenceIdAtom)
    const client = useQueryClient()
    const addNotification = useNotifications((state) => state.addNotification)

    return useMutation(() => api.get(`/conference/${conferenceId}/speakinglist/lowerHand/admin`), {
        onSuccess: () => {
            client.invalidateQueries(['speakinglist', conferenceId])
            addNotification({ message: 'Alle Redebeiträge entfernt', options: { variant: 'success' } })
        },
        onError: () =>
            addNotification({
                message: 'Fehler beim entfernen der Redebeiträge',
                options: { variant: 'error' },
            }),
    })
}
