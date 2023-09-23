import welcome from '@/utils/welcome'

// These are the two main chunks that are used to render the core structure of the app
// Importing them with Promise.all (by using HTTP/2 multiplexing) we can load them in parallel
// and achieve the best possible performance
Promise.all([import('@/Root'), import('@/App')]).then(([{ default: render }, { default: App }]) => {
  render(App)
})

// welcome message for users in the console
welcome()

// ts(1208)
export {}
