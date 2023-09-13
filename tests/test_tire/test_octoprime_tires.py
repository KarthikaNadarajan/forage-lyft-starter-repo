import unittest

from tires import OctoprimeTires


class TestOctoprimeTires(unittest.TestCase):
    def test_needs_service_true(self):
        tire_wear = [1, 0.3, 1, 0.7]
        tires = OctoprimeTires(tire_wear)
        self.assertTrue(tires.needs_service_tires())

    def test_needs_service_false(self):
        tire_wear = [0.5, 0.5, 0.5, 0.5]
        tires = OctoprimeTires(tire_wear)
        self.assertFalse(tires.needs_service_tires())