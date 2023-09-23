import { useMutation, useQuery, useQueryClient } from '@tanstack/react-query'
import { User } from '@/utils/types'
import { api } from './api'
import { DEFAULT_USER } from '@/utils/demo'

export const useUserList = () => {
  return useQuery(['user'], () => api.get<User[]>('/user'), {
    select: (result) => result.data,
  })
}

export const useUser = (id?: string) => {
  return useQuery(
    ['user', id],
    () => {
      if (id) {
        return { data: DEFAULT_USER}
        return api.get<User>(`/user/${id}`)
      }
    },
    {
      select: (result) => result?.data,
    },
  )
}

export const useUpdateUser = (id?: string) => {
  const client = useQueryClient()
  return useMutation(
    (user: Pick<User, 'email' | 'firstName' | 'lastName'>) => api.put(`/user/${id}`, user),
    {
      onSuccess: () => client.invalidateQueries(['user', id]),
    },
  )
}
