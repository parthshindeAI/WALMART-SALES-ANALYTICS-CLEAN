# Walmart Sales — EDA & Storytelling Dashboard

**Problem:** Analyze Walmart sales data to derive business KPIs and create a Power BI dashboard that helps operations & merchandising teams reduce stockouts & improve promotions.

## 🎥 Project Demo
Watch a 2-minute walkthrough explaining the business insights and dashboard:
👉 [Demo Video](https://www.loom.com/share/d09b1238e08341cc880c25976cccedab)

**Data source:** (Kaggle / local CSV) — include exact file names and license.

**Approach:** EDA → KPI design → SQL-backed analysis → Dashboard (Power BI) → automation: narrative generation via LLM.

**Structure:**
- `notebooks/` : exploratory notebooks
- `src/` : reusable scripts (data loading, cleaning)
- `sql/` : queries used to create metrics
- `dashboard/` : Power BI pbix & screenshots
- `docs/` : architecture & diagrams

**How to run (dev):**
1. `python -m venv venv && source venv/bin/activate`
2. `pip install -r requirements.txt`
3. Run notebooks in `notebooks/`

**Deliverables:**
- Cleaned dataset sample (not full raw)
- EDA notebook
- SQL queries file
- Power BI report screenshot + pbix
- README & short Loom demo

