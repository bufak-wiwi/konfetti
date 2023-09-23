import { atom } from 'jotai'
import { atomWithStorage } from 'jotai/utils'

export const sidebarAtom = atom(false)

export const confettiAtom = atomWithStorage<boolean | undefined>('confetti', !!localStorage.getItem('confetti'))
