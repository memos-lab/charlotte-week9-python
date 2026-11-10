# Maimuna Umar Makaniki - Week 9 Class 2 Lab
# Organizing multi-well telemetry with Python collections
# Only print, no Pandas, no CSV parser

# Data - 8 observations, 6 wells
# We use a list of dictionaries so repeated wells are NOT lost
readings = [
    {"well_id": "WELL-05", "field": "north", "pressure_psi": 3150.0, "sensor_active": True},
    {"well_id": "WELL-06", "field": "south", "pressure_psi": 2780.0, "sensor_active": True},
    {"well_id": "WELL-07", "field": "north", "pressure_psi": 3325.0, "sensor_active": True},
    {"well_id": "WELL-07", "field": "north", "pressure_psi": 3180.0, "sensor_active": False},
    {"well_id": "WELL-08", "field": "east", "pressure_psi": 2850.0, "sensor_active": True},
    {"well_id": "WELL-08", "field": "east", "pressure_psi": 2950.0, "sensor_active": False},
    {"well_id": "WELL-09", "field": "south", "pressure_psi": 2700.0, "sensor_active": True},
    {"well_id": "WELL-10", "field": "east", "pressure_psi": 2755.0, "sensor_active": True},
]

# Tuple for units - it should never change, so we use tuple not list
measurement_units = ("psi", "m")

print("Week 9 Class 2 Lab - Multi-Well Telemetry")
print()

# --- Activity A: List exploration ---
print("Activity A - List exploration")
print("Number of observations:", len(readings))
print("First well:", readings[0]["well_id"])
print("Last well:", readings[-1]["well_id"])
first_three = readings[0:3]
print("First three readings:", first_three)
print("Length of first three:", len(first_three))
print("A list retains repeated observations because each position keeps its own dictionary, even if well_id repeats.")
print()

# --- Activity B: Tuples and dictionaries ---
print("Activity B - Tuples and dictionaries")
print("Measurement unit 1:", measurement_units[0])
print("Measurement unit 2:", measurement_units[1])
print("Keys of first reading:", list(readings[0].keys()))
print("First pressure:", readings[0]["pressure_psi"])
print("First field:", readings[0]["field"])
print("Depth with .get():", readings[0].get("depth_m", "not supplied"))
print("We cannot use well_id as the only key in one dictionary, because WELL-07 would overwrite itself and we would lose one reading.")
print()

# --- Activity C: Sets and membership ---
print("Activity C - Sets and membership")
well_ids = []
fields = []
for obs in readings:
    well_ids.append(obs["well_id"])
    fields.append(obs["field"])

unique_wells = set(well_ids)
print("Unique well IDs:", sorted(unique_wells))
print("Number of distinct wells:", len(unique_wells))
print("Sorted distinct fields:", sorted(set(fields)))
print("Is WELL-12 in unique wells?", "WELL-12" in unique_wells)
print()

# --- Activity D: Summaries ---
print("Activity D - Summaries")
pressures = []
for obs in readings:
    pressures.append(obs["pressure_psi"])

total_pressure = sum(pressures)
mean_pressure = total_pressure / len(pressures)
print("Sum of pressure (psi):", total_pressure, "psi")
print("Mean pressure (psi):", mean_pressure, "psi")

inactive_count = 0
for obs in readings:
    if obs["sensor_active"] == False:
        inactive_count = inactive_count + 1
print("Inactive sensor observations:", inactive_count)

# Counts per well - WELL-07 and WELL-08 must be 2
counts_per_well = {}
for obs in readings:
    well = obs["well_id"]
    if well in counts_per_well:
        counts_per_well[well] = counts_per_well[well] + 1
    else:
        counts_per_well[well] = 1
print("Observations per well:", counts_per_well)

# Stretch: second WELL-07 pressure
well07_pressures = []
for obs in readings:
    if obs["well_id"] == "WELL-07":
        well07_pressures.append(obs["pressure_psi"])
print("Second WELL-07 pressure (psi):", well07_pressures[1], "psi")