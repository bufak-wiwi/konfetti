import { create } from 'zustand'

import { devtools, persist } from 'zustand/middleware'
import { User } from '@/utils/types'

interface AuthStore {
    user: User | null
    isAdmin: boolean
    setUser: (user: User | null) => void
}

export const useAuthenticationStore = create<AuthStore>()(
    devtools(
        persist(
            (set) => ({
                user: null,
                isAdmin: false,
                setUser: (user) => set({ user, isAdmin: user?.isAdmin || false }),
            }),
            {
                name: 'auth-storage',
            }
        )
    )
)
