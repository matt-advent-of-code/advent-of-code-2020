import unittest

from day5 import boarding


class MyTestCase(unittest.TestCase):
    def test_range_front_zero(self):
        section = 'F'
        seat_range = (0, 127)
        expected_new_range = (0, 63)
        new_seat_range = boarding.calculate_row_range(section, seat_range)
        self.assertEqual(expected_new_range, new_seat_range)

    def test_range_back_zero(self):
        section = 'B'
        seat_range = (0, 63)
        expected_new_range = (32, 63)
        new_seat_range = boarding.calculate_row_range(section, seat_range)
        self.assertEqual(expected_new_range, new_seat_range)

    def test_range_front_greater_than_zero(self):
        section = 'F'
        seat_range = (32, 63)
        expected_new_range = (32, 47)
        new_seat_range = boarding.calculate_row_range(section, seat_range)
        self.assertEqual(expected_new_range, new_seat_range)

    def test_range_back_greater_than_zero(self):
        section = 'B'
        seat_range = (32, 47)
        expected_new_range = (40, 47)
        new_seat_range = boarding.calculate_row_range(section, seat_range)
        self.assertEqual(expected_new_range, new_seat_range)

    def test_range_back_greater_than_zero_2(self):
        section = 'B'
        seat_range = (40, 47)
        expected_new_range = (44, 47)
        new_seat_range = boarding.calculate_row_range(section, seat_range)
        self.assertEqual(expected_new_range, new_seat_range)

    def test_range_front_greater_than_zero(self):
        section = 'F'
        seat_range = (44, 45)
        expected_new_range = (44, 44)
        new_seat_range = boarding.calculate_row_range(section, seat_range)
        self.assertEqual(expected_new_range, new_seat_range)

    def test_column_range_right_zero(self):
        section = 'R'
        seat_range = (0, 7)
        expected_new_range = (4, 7)
        new_seat_range = boarding.calculate_column_range(section, seat_range)
        self.assertEqual(expected_new_range, new_seat_range)

    def test_column_range_right_zero(self):
        section = 'R'
        seat_range = (0, 7)
        expected_new_range = (4, 7)
        new_seat_range = boarding.calculate_column_range(section, seat_range)
        self.assertEqual(expected_new_range, new_seat_range)

    def test_column_range_left_zero(self):
        section = 'L'
        seat_range = (4, 7)
        expected_new_range = (4, 5)
        new_seat_range = boarding.calculate_column_range(section, seat_range)
        self.assertEqual(expected_new_range, new_seat_range)

    def test_column_range_right_non_zero(self):
        section = 'R'
        seat_range = (4, 5)
        expected_new_range = (5, 5)
        new_seat_range = boarding.calculate_column_range(section, seat_range)
        self.assertEqual(expected_new_range, new_seat_range)

    def test_calculate_row(self):
        boarding_pass_rows = 'BFFFBBF'
        expected_row = 70
        row = boarding.calculate_row(boarding_pass_rows, (0, 127))
        self.assertEqual(expected_row, row)

    def test_calculate_column(self):
        boarding_pass_column = 'RRR'
        expected_row = 7
        row = boarding.calculate_column(boarding_pass_column, (0, 7))
        self.assertEqual(expected_row, row)

    def test_calculate_seat_id(self):
        boarding_pass = 'BFFFBBFRRR'
        expected_seat_id = 567
        seat_id = boarding.calculate_seat_id(boarding_pass)
        self.assertEqual(expected_seat_id, seat_id)

    def test_calculate_seat_id2(self):
        boarding_pass = 'FFFBBBFRRR'
        expected_seat_id = 119
        seat_id = boarding.calculate_seat_id(boarding_pass)
        self.assertEqual(expected_seat_id, seat_id)

    def test_calculate_seat_id3(self):
        boarding_pass = 'BBFFBBFRLL'
        expected_seat_id = 820
        seat_id = boarding.calculate_seat_id(boarding_pass)
        self.assertEqual(expected_seat_id, seat_id)


if __name__ == '__main__':
    unittest.main()
