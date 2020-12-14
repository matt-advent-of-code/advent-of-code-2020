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

    def test_earliest_subsequent_timestamp(self):
        buses = ['7', '13', 'x', 'x', '59', 'x', '31', '19']
        expected_timestamp = 1068781
        timestamp = bus.earliest_subsequent_timestamp(buses)
        self.assertEqual(expected_timestamp, timestamp)

    def test_earliest_subsequent_timestamp_example2(self):
        buses = ['17','x','13','19']
        expected_timestamp = 3417
        timestamp = bus.earliest_subsequent_timestamp(buses)
        self.assertEqual(expected_timestamp, timestamp)

    def test_earliest_subsequent_timestamp_example3(self):
        buses = ['67','7','59','61']
        expected_timestamp = 754018
        timestamp = bus.earliest_subsequent_timestamp(buses)
        self.assertEqual(expected_timestamp, timestamp)

    def test_earliest_subsequent_timestamp_example4(self):
        buses = ['67','x','7','59','61']
        expected_timestamp = 779210
        timestamp = bus.earliest_subsequent_timestamp(buses)
        self.assertEqual(expected_timestamp, timestamp)

    def test_earliest_subsequent_timestamp_example5(self):
        buses = ['67','7','x','59','61']
        expected_timestamp = 1261476
        timestamp = bus.earliest_subsequent_timestamp(buses)
        self.assertEqual(expected_timestamp, timestamp)

    def test_earliest_subsequent_timestamp_example6(self):
        buses = ['1789','37','47','1889']
        expected_timestamp = 1202161486
        timestamp = bus.earliest_subsequent_timestamp(buses)
        self.assertEqual(expected_timestamp, timestamp)

    def test_test(self):
        buses = ['67','7','x','59']
        timestamp = bus.earliest_subsequent_timestamp(buses)
        print(timestamp)


if __name__ == '__main__':
    unittest.main()
