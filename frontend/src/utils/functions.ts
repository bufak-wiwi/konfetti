import isMobileDevice from 'is-mobile'

export function sleep(ms: number) {
    return new Promise((res) => setTimeout(res, ms))
}

export const isMobile = isMobileDevice()
