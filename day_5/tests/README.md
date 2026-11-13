# Week 9 Class 5 — Drilling Telemetry Capstone

## Summary
This program reads raw drilling telemetry, cleans it, converts units, and separates good records from bad ones.

It converts:
- Pressure: psi -> kPa (1 psi = 6.8948 kPa)
- Temperature: F -> C

It only accepts records with status ACTIVE or IDLE. It rejects bad pressure, bad units, negative pressure, wrong field count, and bad status.

## How to run
python src/telemetry_capstone.py data/drilling_telemetry_capstone.txt outputs

## How to test
python -m unittest tests.test_telemetry_capstone -v

## Results
- Done: 13 cleaned, 7 rejected, 5 wells
- outputs/cleaned_telemetry.csv
- outputs/rejected_records.csv
- outputs/well_summary.csv

## Known limitations
- Only supports psi/kPa for pressure and F/C for temperature.
- Does not handle missing data file gracefully beyond a basic error.