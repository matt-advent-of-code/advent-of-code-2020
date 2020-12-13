import unittest

from day13 import bus


class MyTestCase(unittest.TestCase):
    def test_earliest_bus(self):
        arival_time = 939
        buses = ['7','13','x','x','59','x','31','19']
        expected_bus = {'59': 944}
        best_bus = bus.calculate_earliest_departure(arival_time, buses)
        self.assertEqual(expected_bus, best_bus)
        self.assertEqual(295, bus.solve(best_bus, arival_time))


if __name__ == '__main__':
    unittest.main()
