import os
import sys
import unittest

SRC_DIR = os.path.dirname(__file__)
if SRC_DIR not in sys.path:
    sys.path.insert(0, SRC_DIR)

from aircraft import Aircraft
from sensor import Sensor


class TestAircraftSystem(unittest.TestCase):

    def test_aircraft_exists(self):
        plane = Aircraft("Prueba", 1200, wing_area=15, velocity=80, cl=0.7)
        self.assertEqual(plane.name, "Prueba")
        self.assertGreater(plane.weight, 0)
        self.assertEqual(plane.wing_area, 15)
        self.assertTrue(hasattr(plane, "calculate_lift"))

    def test_sensors_work(self):
        plane = Aircraft("PruebaSensor", 800)
        temp_sensor = Sensor("Temperatura", 25.0)
        pressure_sensor = Sensor("Presion", 1.02)
        plane.add_sensor(temp_sensor)
        plane.add_sensor(pressure_sensor)

        self.assertEqual(len(plane.sensors), 2)
        self.assertEqual(plane.sensors[0].read(), 25.0)
        self.assertEqual(plane.sensors[1].read(), 1.02)

    def test_calculation_returns_result(self):
        plane = Aircraft("Calculo", 1000, wing_area=10, velocity=50, cl=1.2, air_density=1.225)
        lift = plane.calculate_lift()
        self.assertIsInstance(lift, float)
        self.assertGreater(lift, 0.0)


if __name__ == "__main__":
    unittest.main()
