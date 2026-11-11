# Week 9 Class 3 - Control Flow + Functions
# Synthetic multi-well pressure surveillance

READINGS = [
    {"well_id": "WELL-07", "pressure_psi": 3180.0, "status": "active"},
    {"well_id": "WELL-07", "pressure_psi": 3180.0, "status": "active"},
    {"well_id": "WELL-08", "pressure_psi": 2795.0, "status": "active"},
    {"well_id": "WELL-08", "pressure_psi": 2795.0, "status": "active"},
    {"well_id": "WELL-10", "pressure_psi": 3495.0, "status": "active"},
    {"well_id": "WELL-10", "pressure_psi": 3500.0, "status": "active"},
    {"well_id": "WELL-03", "pressure_psi": 2600.0, "status": "inactive"},
    {"well_id": "WELL-04", "pressure_psi": -1.0, "status": "active"},
    {"well_id": "WELL-05", "pressure_psi": None, "status": "active"},
    {"well_id": "WELL-06", "pressure_psi": 3100.0, "status": "inactive"},
]

# --- A. Decisions ---
def classify_pressure(pressure_psi):
    if pressure_psi is None or pressure_psi < 0:
        return "invalid"
    if pressure_psi >= 3500:
        return "high"
    if pressure_psi >= 2500:
        return "normal"
    return "low"

# --- C. Functions ---
def psi_to_kpa(pressure_psi):
    if pressure_psi is None or pressure_psi < 0:
        return None
    return pressure_psi * 6.8947572932

# --- A Check: Boundary values ---
print("Boundary checks:")
for value in [None, -1, 0, 2499, 2500, 3499, 3500]:
    print(f"  {value} -> {classify_pressure(value)}")
print()

# --- B. Loops: Print ALL 10 rows, including inactive ---
print("Activity B - All readings:")
for reading in READINGS:
    well = reading["well_id"]
    pressure = reading["pressure_psi"]
    label = classify_pressure(pressure)
    print(f"  {well} | {pressure} psi | {label}")
print()

# --- C. Conversion demo ---
print("Activity C - Conversion:")
result = psi_to_kpa(3150)
print(f"  3150 psi = {result:.2f} kPa")
print()

# --- D. Filter and Summarize ---
print("Activity D - Filter and Summarize (active + valid only):")
totals = {}
counts = {}
valid = 0
skipped = 0

for reading in READINGS:
    # Skip inactive
    if reading["status"] != "active":
        skipped += 1
        continue
    # Skip invalid pressure
    if reading["pressure_psi"] is None or reading["pressure_psi"] < 0:
        skipped += 1
        continue

    well = reading["well_id"]
    pressure = reading["pressure_psi"]

    if well not in totals:
        totals[well] = 0.0
        counts[well] = 0
    totals[well] += pressure
    counts[well] += 1
    valid += 1

print(f"  Valid: {valid}")
print(f"  Skipped: {skipped}")
for well in totals:
    average = totals[well] / counts[well]
    print(f"  {well} average: {average:.2f} psi")