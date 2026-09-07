import axios from 'axios'
import type { RankingResponse, VillageRanking, VillageSolarResponse, VillagesResponse } from '../types/api'

export const api = axios.create({ baseURL: import.meta.env.VITE_API_BASE_URL || '/api' })
export const solarShaktiApi = {
  getVillages: async () => (await api.get<VillagesResponse>('/villages')).data,
  getVillage: async (villageId: string) => (await api.get<VillageRanking>(`/villages/${villageId}`)).data,
  getRanking: async () => (await api.get<RankingResponse>('/ranking')).data,
  getVillageSolar: async (villageId: string) => (await api.get<VillageSolarResponse>(`/villages/${villageId}/solar`)).data,
}
