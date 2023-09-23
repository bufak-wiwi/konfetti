import { useEffect, useMemo } from 'react'
import { useMediaQuery } from '@mui/material'
import { createTheme } from '@mui/material'
import { blue, pink } from '@mui/material/colors'
import { useDarkMode } from '../store/useDarkMode'

export function useCustomTheme() {
  const { darkMode, initDarkMode } = useDarkMode()
  const prefersDarkMode = useMediaQuery('(prefers-color-scheme: dark)')

  useEffect(() => {
    initDarkMode(prefersDarkMode)
  }, [initDarkMode, prefersDarkMode])

  const theme = useMemo(
    () =>
      createTheme({
        palette: {
          mode: darkMode ? 'dark' : 'light',
          primary: {
            main: blue[700],
          },
          secondary: pink,
        },
      }),
    [darkMode],
  )

  return theme
}
