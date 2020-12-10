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


if __name__ == '__main__':
    unittest.main()
