export interface VillageRanking { village_id: string; village_name: string; grid_distance_km: number; annual_generation_mwh: number; payback_years: number; roi_percent: number; solar_score: number; financial_score: number; grid_score: number; demand_score: number; infrastructure_score: number; investment_score: number; rank: number }
export interface RankingResponse { count: number; ranking: VillageRanking[] }
export interface VillagesResponse { count: number; villages: VillageRanking[] }
export interface MonthlySolarRecord { village_id: string; village_name: string; month: number; solar_irradiance: number; avg_temperature: number; days_observed: number }
export interface VillageSolarResponse { village_id: string; data: MonthlySolarRecord[] }
export interface GeoJsonVillageProperties { id: string; name: string; district: string; population: number; grid_distance_km: number; investment_score: number; annual_generation_mwh: number; roi_percent: number; payback_years: number; rank: number }
export interface VillageGeoJson { type: 'FeatureCollection'; features: Array<{ type: 'Feature'; geometry: { type: 'Point'; coordinates: [number, number] }; properties: GeoJsonVillageProperties }> }
