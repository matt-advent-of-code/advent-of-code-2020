import unittest

from day9 import xmas


class MyTestCase(unittest.TestCase):
    def test_is_valid(self):
        preamble = [x for x in range(1, 26)]
        value = 26
        self.assertTrue(xmas.is_valid(value, preamble))

    def test_is_valid_49(self):
        preamble = [x for x in range(1, 26)]
        value = 49
        self.assertTrue(xmas.is_valid(value, preamble))

    def test_is_invalid(self):
        preamble = [x for x in range(1, 26)]
        value = 100
        self.assertFalse(xmas.is_valid(value, preamble))

    def test_is_invalid_50(self):
        preamble = [x for x in range(1, 26)]
        value = 50
        self.assertFalse(xmas.is_valid(value, preamble))

    def test_find_first_invalid(self):
        data = [35, 20, 15, 25, 47, 40, 62, 55, 65, 95, 102, 117, 150, 182, 127, 219, 299, 277, 309, 576]
        preamble_size = 5
        expected_number = 127
        invalid_number = xmas.first_invalid(data, preamble_size)
        self.assertEqual(expected_number, invalid_number)

    def test_find_contiguous_numbers(self):
        data = [35, 20, 15, 25, 47, 40, 62, 55, 65, 95, 102, 117, 150, 182, 127, 219, 299, 277, 309, 576]
        invalid_number = 127
        expected_contiguous_numbers = [15,25,47,40]

        contiguous_numbers = xmas.find_contiguous_numbers(data, invalid_number)
        self.assertEqual(expected_contiguous_numbers, contiguous_numbers)


if __name__ == '__main__':
    unittest.main()
