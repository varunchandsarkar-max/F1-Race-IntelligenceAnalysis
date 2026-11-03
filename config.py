"""Project settings. Edit years here to change the analysis window."""
START_YEAR = 2009
END_YEAR = 2025
API_BASE = "https://api.jolpi.ca/ergast/f1"
REQUEST_TIMEOUT = 30
PAGE_LIMIT = 100
REQUEST_PAUSE_SECONDS = 0.25

from pathlib import Path
ROOT = Path(__file__).resolve().parent
RAW_DIR = ROOT / "data" / "raw"
PROCESSED_DIR = ROOT / "data" / "processed"
EXTERNAL_DIR = ROOT / "data" / "external"
CHART_DIR = ROOT / "visualizations"
