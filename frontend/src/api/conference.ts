import { sleep } from '@/utils/functions'
import { useQuery } from '@tanstack/react-query'

export const useConferenceList = () => {
    return useQuery(
        ['conference'],
        async () => {
            // TODO: implement real function
            await sleep(500)
            return {
                data: [
                    { id: 1, name: 'Konferenz 1' },
                    { id: 2, name: 'Konferenz 2' },
                ] as const,
            }
        },
        {
            select: (result) => result.data,
        }
    )
}
