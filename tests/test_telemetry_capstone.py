import unittest
from src.telemetry_capstone import convert_pressure, convert_temperature, parse_record

class TestTelemetry(unittest.TestCase):
    def test_psi_to_kpa(self):
        self.assertAlmostEqual(convert_pressure(100, "psi"), 689.48, places=2)

    def test_kpa_passthrough(self):
        self.assertEqual(convert_pressure(100, "kPa"), 100)

    def test_f_to_c(self):
        self.assertAlmostEqual(convert_temperature(212, "F"), 100.0, places=2)

    def test_c_passthrough(self):
        self.assertEqual(convert_temperature(25, "C"), 25)

    def test_valid_record(self):
        rec = parse_record("2025-01-01T08:00:00 | WELL-101 | 100 | psi | 212 | F | ACTIVE")
        self.assertEqual(rec["well_id"], "WELL-101")
        self.assertEqual(rec["pressure_kpa"], "689.48")
        self.assertEqual(rec["temperature_c"], "100.00")

    def test_rejects_bad_pressure(self):
        with self.assertRaises(ValueError):
            parse_record("2025-01-01T08:00:00 | WELL-101 | bad | psi | 212 | F | ACTIVE")

    def test_rejects_negative_pressure(self):
        with self.assertRaises(ValueError):
            parse_record("2025-01-01T08:00:00 | WELL-101 | -10 | psi | 212 | F | ACTIVE")

    def test_rejects_bad_unit(self):
        with self.assertRaises(ValueError):
            parse_record("2025-01-01T08:00:00 | WELL-101 | 100 | bar | 212 | F | ACTIVE")

if __name__ == "__main__":
    unittest.main()