import { useConferenceList } from '@/api'
import { conferenceIdAtom } from '@/utils/atoms'
import { Conference } from '@/utils/types'
import { useAtom } from 'jotai'
import { useEffect, useState } from 'react'

/**
 * Get the currently selected conference
 */
export const useCurrentConference = () => {
    const { data: conferenceList, isLoading, isError } = useConferenceList()
    const [conferenceId, setConferenceId] = useAtom(conferenceIdAtom)
    const [conference, setConference] = useState<undefined | Pick<Conference, 'name' | 'id'>>()

    // update conferenceId once the conference list is loaded
    useEffect(() => {
        const current = conferenceList?.find((x) => x.id === conferenceId)
        if (!current) {
            setConferenceId(conferenceList?.at(-1)?.id)
        }
    }, [conferenceList, setConferenceId])

    // set conference when the selected conferenceId changes
    useEffect(() => {
        const selected = conferenceList?.find((x) => x.id === conferenceId)
        setConference(selected as any)
    }, [conferenceId, conferenceList, setConference])

    return { conference, isLoading, isError }
}
