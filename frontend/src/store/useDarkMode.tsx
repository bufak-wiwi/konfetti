import { create } from 'zustand'
import { persist } from 'zustand/middleware'

interface StoreState {
    darkMode: boolean | null
    initDarkMode: (darkMode: boolean) => void
    toggleDarkMode: () => void
}

export const useDarkMode = create<StoreState>()(
    persist(
        (set) => ({
            darkMode: null,
            initDarkMode: (darkMode) =>
                set((state) => ({ darkMode: state.darkMode === null ? darkMode : state.darkMode })),
            toggleDarkMode: () => set((state) => ({ darkMode: !state.darkMode })),
        }),
        {
            name: 'darkMode',
            partialize: (state) => ({ darkMode: state.darkMode }),
        }
    )
)
