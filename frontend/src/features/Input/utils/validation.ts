export const isValidEmail = (mail: string) => {
    const re =
        /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
    return re.test(mail?.toLowerCase())
}

/**
 * Check whether the password is between 8 and 32 characters long
 */
export const isValidPassword = (password: string) => {
    return password.length <= 32 // TODO: && password.length >= 8
}
