# SolarShakti — Frontend Project Context

## 1. Project

SolarShakti is a government decision-support platform for planning,
prioritizing, optimizing, and monitoring rural solar investments in India.

The platform helps answer:

1. WHERE should solar infrastructure be deployed?
2. HOW MUCH should be invested?
3. IS the deployed project performing as expected?

The product is designed primarily for government and infrastructure
decision-makers.

---

## 2. Core Product Flow

Data
→ Solar & Financial Analysis
→ Village Scoring
→ Village Ranking
→ Investment Optimization
→ Government Decision

Future lifecycle:

Deployment
→ Actual Generation Data
→ Expected vs Actual
→ Performance Monitoring
→ Underperformance Detection

---

## 3. Current Repository

The repository currently contains:

backend/
data/

The frontend will be added as:

frontend/

Do not modify existing backend functionality unless explicitly required.

---

## 4. Frontend Technology

Use:

- React
- TypeScript
- Vite
- Tailwind CSS
- shadcn/ui
- React Router
- TanStack Query
- Axios
- Recharts
- Leaflet / React Leaflet
- Lucide React

Do not introduce additional UI frameworks unless explicitly requested.

Avoid mixing multiple component libraries.

---

## 5. Planned Frontend Pages

### Authentication

- Login

### Main Application

- Dashboard
- Village Intelligence
- Priority Ranking
- Investment Optimizer
- Monitoring

Possible future pages/features:

- Detailed Solar Analysis
- Detailed Financial Analysis
- Project Details

---

## 6. Current Backend API

The current FastAPI backend provides:

GET /

Basic API status.

GET /health

Returns backend/data health information.

GET /villages

Returns all villages from the processed investment
ranking dataset.

GET /villages/{village_id}

Returns information for one village.

GET /villages/{village_id}/solar

Returns monthly solar data for one village.

GET /ranking

Returns villages ordered by investment score.

GET /investment-plan?budget={budget}

Runs the current investment optimizer using the supplied budget.

---

## 7. Current Backend Data Available

Village/ranking results currently include information such as:

- village_id
- village_name
- grid_distance_km
- annual_generation_mwh
- payback_years
- roi_percent
- solar_score
- financial_score
- grid_score
- demand_score
- infrastructure_score
- investment_score
- rank

The exact available fields should always be checked against
the current backend response before being used in the frontend.

Do not invent fields.

---

## 8. Current Analytical Pipeline

The current backend processes villages through:

### Solar Engine

Calculates annual solar generation.

### Financial Engine

Calculates:

- CAPEX
- annual cash flow
- payback period
- ROI
- lifetime generation

### Site Ranking

Creates:

- solar score
- financial score
- grid score
- demand score
- infrastructure score
- investment score
- rank

### Budget Optimizer

Given a government budget, selects villages for investment
and returns:

- selected villages
- total investment
- remaining budget
- expected annual generation

---

## 9. Important Current Limitation

The current ranking implementation uses placeholder values
for demand_score and infrastructure_score.

Do not present these as sophisticated real-world AI predictions.

The backend may be enhanced later.

---

## 10. Future ML Integration

A teammate is developing ML models/ensemble models that are expected
to enhance three major analytical areas:

1. Solar generation
2. Financial analysis
3. Investment scoring

The planned ensemble may use:

- Linear Regression
- Random Forest
- XGBoost
- A meta/weighting model

The frontend must be designed so these future predictions can be
added without requiring a complete frontend rewrite.

Do not expose model implementation details unless they are useful
to the government user.

The user should primarily see:

- prediction/result
- confidence where available
- explanation/reasoning
- relevant supporting metrics

---

## 11. Frontend Responsibility

The frontend is responsible for:

- displaying backend results
- visualizing data
- maps
- charts
- filtering
- navigation
- user interaction
- sending user inputs to the backend
- presenting investment recommendations clearly

The frontend should NOT independently calculate:

- solar generation
- ROI
- payback
- investment scores
- budget optimization

These calculations belong to the backend/analytical layer.

---

## 12. Design Philosophy

The interface should feel:

- professional
- government-grade
- modern
- data-driven
- clean
- renewable-energy focused

Avoid:

- excessive futuristic effects
- generic green environmental designs
- unnecessary animations
- excessive gradients
- cluttered dashboards

The design should communicate:

Government + Technology + Renewable Energy.

---

## 13. Login Design

The login page has been manually designed by the project team.

Visual concept:

- SolarShakti branding
- India map as a major visual element
- login panel
- clean professional layout
- subtle solar/energy visual language

The login design should establish the visual language
for the rest of the application.

---

## 14. Dashboard Philosophy

The dashboard should answer the government's first questions quickly:

- What is the current solar investment opportunity?
- Which villages have the highest priority?
- Where are they located?
- What is the potential generation?
- What investment opportunities exist?
- What needs attention?

Important information should be visualized rather than presented
as large blocks of text.

---

## 15. Map

The application will use an interactive India/village map.

The map should eventually support:

- village locations
- priority visualization
- village selection
- village details
- filtering
- navigation to village intelligence

Leaflet / React Leaflet should be used.

---

## 16. Village Intelligence

A village detail screen should eventually show information such as:

- village identity
- location
- investment priority
- solar potential
- expected generation
- financial metrics
- ROI
- payback
- grid information
- supporting score components
- charts

Future ML predictions can be incorporated here.

---

## 17. Priority Ranking

The ranking screen should allow decision-makers to:

- see highest-priority villages
- sort/filter villages
- compare villages
- inspect the reason behind a score
- open village details

The ranking should be visual and easy to scan.

---

## 18. Investment Optimizer

The government user should be able to enter a budget.

Example:

₹50 Crore

The frontend sends the budget to the backend.

The result should show:

- selected villages
- total investment
- remaining budget
- expected annual generation
- selected village rankings
- investment distribution
- map visualization

---

## 19. Monitoring

The long-term product should support:

Expected Generation
vs
Actual Generation

and identify underperforming projects.

This may initially be implemented as a prototype UI
and enhanced when corresponding backend functionality becomes available.

Do not invent monitoring APIs that do not currently exist.

---

## 20. Vibe Coding Rules

When generating code:

1. Read this file before making major changes.
2. Do not invent backend API fields.
3. Do not invent backend endpoints.
4. Do not duplicate backend business logic in React.
5. Keep API calls separate from UI components.
6. Keep components reusable.
7. Use TypeScript types for backend data.
8. Keep mock/demo data separate from real API data.
9. Clearly label temporary mock data.
10. Do not rewrite working backend code to solve frontend problems.
11. Do not install unnecessary dependencies.
12. Maintain the existing visual language across pages.
13. Prefer simple, maintainable solutions over unnecessary complexity.
14. Do not make architectural changes without explaining why.