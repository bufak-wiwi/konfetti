import type { SnackbarProps } from 'notistack'

export interface SnackbarType {
    options: SnackbarProps
    maxSnack: number
}

export type ConferenceStatus = 'applied' | 'attendee' | 'organizer' | 'none'

/**
 * Api key for custom applications (e.g. third party apps).
 * Using this key in the `x-api-key` header will allow the user to access all endpoints as he would be logged in.
 */
export type ApiKey = {
    id: number
    userId: number
    apiKey: string
    note: string
    createdOn: string
    validUntil: string
}

export const Priorities = [1, 2, 3, 4, 5, 6, 7] as const
export type Priority = (typeof Priorities)[number]

export type ApplicationType = {
    id: number
    name: string
}

export type ApplicationCode = {
    id: number
    conferenceId: number
    councilId: number
    priority: Priority
    code: string
    isUsed: boolean
    applicationTypeId: number
}

type JSONField = { [key: string]: string | number | boolean }

export type Conference = {
    id: number
    name: string
    startDate: string
    endDate: string
    arrivedCouncils: number
    conferenceApplicationPhase: JSONField
    workshopApplicationPhase: JSONField
    workshopSuggestionPhase: JSONField
    /**
     * link to the participation agreement
     */
    participationAgreement: string
    texts: JSONField
    dropdowns: JSONField
}

export type User = {
    id: number
    email: string
    firstname: string
    lastname: string
    councilId: number
    birthday: string
    status: 'blocked' | 'confirmed' | 'pending'
    isAdmin: boolean
    isRat: boolean
    conferences: {
        [id: number]: ConferenceStatus
    }
}

export interface LocationState {
    from: {
        pathname: string
    }
}

export type SpeakingEntry = {
    name: string
    surname: string
    council: string
    reportType: number
    reportTime: string
    reportApplicantInfo: string
}
