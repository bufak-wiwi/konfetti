import { useEffect, useState } from 'react'

function getOrientation() {
  return window.innerHeight > window.innerWidth
}

export default function useWindow() {
  const [isPortrait, setIsPortrait] = useState(getOrientation())
  const [width, setWidth] = useState(window.innerWidth)

  useEffect(() => {
    function handleResize() {
      setWidth(window.innerWidth)
      setIsPortrait(getOrientation())
    }

    window.addEventListener('resize', handleResize)

    return () => window.removeEventListener('resize', handleResize)
  }, [])

  return { isPortrait, width }
}
