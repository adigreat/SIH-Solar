export interface GeographicOption { id: string; name: string }
export interface DashboardState extends GeographicOption { districts: GeographicOption[] }

// The current ranking and GeoJSON datasets contain Maharashtra villages only.
export const dashboardStates: DashboardState[] = [{ id: 'maharashtra', name: 'Maharashtra', districts: [{ id: 'nashik', name: 'Nashik' }] }]
