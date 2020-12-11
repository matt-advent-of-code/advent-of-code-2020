import unittest

from day10 import adapter


class MyTestCase(unittest.TestCase):
    def test_adapter(self):
        adapters = [16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4]
        expected_diff = {1: 7, 3: 5}
        diff = adapter.find_diffs(adapters)
        self.assertEqual(expected_diff, diff)

    def test_larger_adapter(self):
        adapters = [28, 33, 18, 42, 31, 14, 46, 20, 48, 47, 24, 23, 49, 45, 19, 38, 39, 11, 1, 32, 25, 35, 8, 17,
                    7, 9, 4, 2, 34, 10, 3]
        expected_diff = {1: 22, 3: 10}
        diff = adapter.find_diffs(adapters)
        self.assertEqual(expected_diff, diff)

    def test_number_possible_arangements(self):
        adapters = [16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4]
        expected_number_of_arangements = 8
        number_of_aranagements = adapter.find_arrangements(adapters)
        self.assertEqual(expected_number_of_arangements, number_of_aranagements)


    def test_number_possible_arangements2(self):
        adapters = [28, 33, 18, 42, 31, 14, 46, 20, 48, 47, 24, 23, 49, 45, 19, 38, 39, 11, 1, 32, 25, 35, 8, 17,
                    7, 9, 4, 2, 34, 10, 3]
        expected_number_of_arangements = 19208
        number_of_aranagements = adapter.find_arrangements(adapters)
        self.assertEqual(expected_number_of_arangements, number_of_aranagements)


    def test_number_possible_find_arrangements_1_entry(self):
        adapters = [1]
        expected_number_of_arrangements = 1
        number_of_arrangements = adapter.find_arrangements(adapters)
        self.assertEqual(expected_number_of_arrangements, number_of_arrangements)

    def test_number_possible_find_arrangements_2_entries(self):
        adapters = [1, 3]
        expected_number_of_arrangements = 2
        number_of_arrangements = adapter.find_arrangements(adapters)
        self.assertEqual(expected_number_of_arrangements, number_of_arrangements)

if __name__ == '__main__':
    unittest.main()
