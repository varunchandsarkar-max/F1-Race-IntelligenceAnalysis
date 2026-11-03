import argparse
from src.ingest import download_all
from src.cleaning import clean_data
from src.analysis import run_analysis
from src.visualizations import make_charts

parser = argparse.ArgumentParser(description="F1 Race Intelligence Analysis pipeline")
parser.add_argument("--download", action="store_true", help="Download source data")
parser.add_argument("--analyze", action="store_true", help="Clean, analyze and chart existing data")
parser.add_argument("--all", action="store_true", help="Download and analyze")
args = parser.parse_args()

if args.download or args.all:
    download_all()
if args.analyze or args.all:
    clean_data()
    run_analysis()
    make_charts()
if not (args.download or args.analyze or args.all):
    parser.print_help()
