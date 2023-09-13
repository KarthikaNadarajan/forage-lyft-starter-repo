import unittest
from datetime import date

from battery import SpindlerBattery

class TestSpindlerBattery(unittest.TestCase):
    def test_needs_service_true(self):
        current_date=date(2023, 9, 12)
        last_service_date=date(2021, 9, 10)
        battery = SpindlerBattery(current_date, last_service_date)
        self.assertTrue(battery.needs_service_battery())

    def test_needs_service_false(self):
        current_date=date(2023, 9, 12)
        last_service_date=date(2021, 9, 14)
        battery = SpindlerBattery(current_date, last_service_date)
        self.assertFalse(battery.needs_service_battery())

