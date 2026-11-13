import csv
import sys
from pathlib import Path
from collections import defaultdict

PSI_TO_KPA = 6.8947572932

def psi_to_kpa(psi):
    return psi * PSI_TO_KPA

def f_to_c(f):
    return (f - 32) * 5 / 9

def convert_pressure(value, unit):
    if unit == "psi":
        return psi_to_kpa(value)
    if unit == "kPa":
        return value
    raise ValueError(f"Unsupported pressure unit: {unit}")

def convert_temperature(value, unit):
    if unit == "F":
        return f_to_c(value)
    if unit == "C":
        return value
    raise ValueError(f"Unsupported temperature unit: {unit}")

def parse_record(line):
    parts = [p.strip() for p in line.split("|")]
    if len(parts) != 7:
        raise ValueError(f"Expected 7 fields, got {len(parts)}")
    timestamp, well_id, p_val, p_unit, t_val, t_unit, status = parts
    if not timestamp:
        raise ValueError("Missing timestamp")
    if not well_id:
        raise ValueError("Missing well_id")
    try:
        pressure = float(p_val)
    except ValueError:
        raise ValueError("Non-numeric pressure")
    if pressure < 0:
        raise ValueError("Negative pressure")
    if p_unit not in ("psi", "kPa"):
        raise ValueError(f"Unsupported pressure unit: {p_unit}")
    try:
        temp = float(t_val)
    except ValueError:
        raise ValueError("Non-numeric temperature")
    if t_unit not in ("F", "C"):
        raise ValueError(f"Unsupported temperature unit: {t_unit}")
    if status not in ("ACTIVE", "INACTIVE"):
        raise ValueError(f"Invalid status: {status}")
    pressure_kpa = convert_pressure(pressure, p_unit)
    temp_c = convert_temperature(temp, t_unit)
    return {
        "timestamp": timestamp,
        "well_id": well_id,
        "pressure_kpa": f"{pressure_kpa:.2f}",
        "temperature_c": f"{temp_c:.2f}",
        "status": status,
        "_pressure_float": pressure_kpa,
    }

def main():
    if len(sys.argv) != 3:
        print("Usage: python src/telemetry_capstone.py <input_file> <output_dir>")
        sys.exit(1)
    input_path = Path(sys.argv[1])
    out_dir = Path(sys.argv[2])
    out_dir.mkdir(parents=True, exist_ok=True)

    cleaned = []
    rejected = []
    totals = defaultdict(list)

    lines = input_path.read_text(encoding="utf-8").splitlines()
    for line_number, raw in enumerate(lines, start=1):
        if raw.strip() == "":
            continue
        try:
            rec = parse_record(raw)
        except ValueError as e:
            rejected.append({"line_number": line_number, "reason": str(e), "raw_record": raw})
            continue
        cleaned.append(rec)
        if rec["status"] == "ACTIVE":
            totals[rec["well_id"]].append(rec["_pressure_float"])

    with open(out_dir / "cleaned_telemetry.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["timestamp", "well_id", "pressure_kpa", "temperature_c", "status"])
        for r in cleaned:
            w.writerow([r["timestamp"], r["well_id"], r["pressure_kpa"], r["temperature_c"], r["status"]])

    with open(out_dir / "rejected_records.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["line_number", "reason", "raw_record"])
        for r in rejected:
            w.writerow([r["line_number"], r["reason"], r["raw_record"]])

    with open(out_dir / "well_summary.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["well_id", "active_readings", "avg_pressure_kpa"])
        for well_id in sorted(totals):
            vals = totals[well_id]
            avg = sum(vals) / len(vals)
            w.writerow([well_id, len(vals), f"{avg:.2f}"])

    print(f"Done: {len(cleaned)} cleaned, {len(rejected)} rejected, {len(totals)} wells")

if __name__ == "__main__":
    main()