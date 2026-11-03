# Formula 1 Race Intelligence Analysis

A reproducible data analytics project for exploring Formula 1 race history, driver and constructor performance, circuits, podiums, retirements and (where licensed/source data is available) tyre strategies.

## Project scope

- Default historical window: **2009–2025** (17 seasons; change it in `config.py`).
- Main source: [Jolpica-F1 API](https://api.jolpi.ca/ergast/f1/), an open-source, Ergast-compatible Formula 1 data API.
- Optional tyre compound source: [FastF1](https://docs.fastf1.dev/), which can expose lap-level tyre data for supported modern seasons.
- Output: cleaned CSV files suitable for Tableau, analysis summaries, charts and a project report.

> **Data honesty:** the Ergast-compatible race-results API does not provide tyre compound for every race entry. The project does not invent compounds. The tyre module is optional and uses FastF1 session data when available. Pit stops are not the same thing as tyre compounds. The API's pit-stop endpoint has historical coverage limitations.

## Quick start (Windows)

1. Install Python 3.10 or newer.
2. Extract this repository.
3. Open Command Prompt in the project folder.
4. Create and activate a virtual environment:

```bash
py -m venv .venv
.venv\Scripts\activate
```

5. Install packages:

```bash
pip install -r requirements.txt
```

6. Download race data:

```bash
python run_pipeline.py --download
```

7. Run analysis:

```bash
python run_pipeline.py --analyze
```

8. Or run both:

```bash
python run_pipeline.py --all
```

The first download can take several minutes because it requests paginated season data. Respect the API's published terms and rate limits; do not run repeated downloads unnecessarily.

## Folder guide

```text
data/
  raw/                 # API response tables
  processed/           # Tableau-ready cleaned CSVs
  external/            # Optional FastF1 tyre-lap data
notebooks/              # Guided analysis notebook
src/
  ingest.py             # Jolpica API downloader
  cleaning.py           # Data preparation and joins
  analysis.py           # Metrics and summary tables
  visualizations.py     # Static charts
  tyre_analysis.py      # Optional FastF1 tyre extraction
tableau/
  dashboard_blueprint.md
  calculated_fields.md
reports/
  project_report.md
  project_report.pdf
```

## Data tables produced

- `races.csv`: one row per Grand Prix.
- `results.csv`: one row per driver per Grand Prix.
- `drivers.csv`, `constructors.csv`, `circuits.csv`, `status.csv`.
- `pit_stops.csv`: pit-stop records where the API provides them.
- `race_results_enriched.csv`: joined analysis table.
- `driver_summary.csv`, `constructor_summary.csv`, `country_summary.csv`, `circuit_summary.csv`, `dnf_summary.csv`, `podium_summary.csv`.
- `season_constructor_points.csv`: points grouped by season and constructor.
- `tyre_laps.csv`: optional FastF1 data, only if extraction succeeds.

## Important metric definitions

- **Podium:** classified finishing position 1, 2 or 3.
- **Win:** classified finishing position 1.
- **DNF / retirement:** this project uses the source status text and flags a result as `is_dnf` when it is not classified as a finish. This is a practical analysis flag, not a complete FIA technical failure taxonomy.
- **Finish rate:** classified finishers divided by all race starts.
- **Points:** official race-result points as reported by the source. Cross-era comparisons require caution because F1 points systems changed.
- **Driver nationality:** nationality field in the driver register; it is not necessarily the driver's birthplace or current residence.
- **Tyre compound:** only analyzed when the optional lap-level data contains a compound field.

## Tableau workflow

1. Open Tableau Public or Tableau Desktop.
2. Connect to `data/processed/race_results_enriched.csv`.
3. Use `raceId` to relate it to `races.csv` if you want separate logical tables.
4. Build the four dashboards using `tableau/dashboard_blueprint.md`.
5. Save the workbook as `tableau/F1_Race_Intelligence.twbx`.
6. Add screenshots to `tableau/screenshots/` and update the report with actual findings.

## Limitations

- The API is community maintained and may have rate limits or temporary outages.
- Historical data coverage differs by endpoint. Pit stops and lap-level tyre compounds are not complete across all seasons.
- DNF categories are source status descriptions, not always clean engineering root causes.
- Points totals from different eras are not directly comparable without normalization.
- This project is descriptive analytics, not a race outcome prediction system.

## Attribution

Data source: Jolpica-F1 / Ergast-compatible API. Cite the API and review its terms before redistribution: https://github.com/jolpica/jolpica-f1

Optional tyre data: FastF1 documentation: https://docs.fastf1.dev/

This repository is an educational analytics project and is not affiliated with Formula 1, FIA or any racing team.
