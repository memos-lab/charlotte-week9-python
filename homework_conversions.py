
# --- Q9 ---
well_id = "WELL-01"
pressure_psi = 2500.0
temperature_f = 140.0
sensor_active = True

pressure_kpa = pressure_psi * 6.89476
temperature_c = (temperature_f - 32) * 5 / 9

print(f"Well: {well_id}")
print(f"Pressure: {pressure_kpa:.1f} kPa")
print(f"Temperature: {temperature_c:.1f} °C")
print(f"Sensor active: {sensor_active}")

# --- Q10 ---
pressure_psi = 3000.0
temperature_f = 32.0

pressure_kpa = pressure_psi * 6.89476
temperature_c = (temperature_f - 32) * 5 / 9

print(f"Well: {well_id}")
print(f"Pressure: {pressure_kpa:.1f} kPa")
print(f"Temperature: {temperature_c:.1f} °C")
print(f"Sensor active: {sensor_active}")
print("Prediction was: 20684.3 kPa and 0.0 C - matches Python")
print("Rounding: Python calculated 20684.28 then rounded to 20684.3 for display")

# --- Q11 ---
print("--- Q11 ---")
raw_pressure = "3150"
print(f"Raw pressure type: {type(raw_pressure)}")
print("This line would fail if we run it:")
print("# print(raw_pressure * 6.89476)  # TypeError - cannot multiply str by float")

# Fix with float()
pressure_psi_2 = float(raw_pressure)
print(f"After float(): {pressure_psi_2}")
print(f"Converted raw_pressure: {pressure_psi_2 * 6.89476:.1f} kPa")