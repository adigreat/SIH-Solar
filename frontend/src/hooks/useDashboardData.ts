import { useQuery } from '@tanstack/react-query'
import { solarShaktiApi } from '../services/api'
import type { VillageGeoJson } from '../types/api'

async function getVillageGeoJson(): Promise<VillageGeoJson> { const response = await fetch('/data/villages.geojson'); if (!response.ok) throw new Error('Map data is unavailable.'); return response.json() as Promise<VillageGeoJson> }
export function useDashboardData() { const ranking = useQuery({ queryKey: ['ranking'], queryFn: solarShaktiApi.getRanking }); const mapData = useQuery({ queryKey: ['village-map'], queryFn: getVillageGeoJson, staleTime: Infinity }); return { ranking, mapData } }
