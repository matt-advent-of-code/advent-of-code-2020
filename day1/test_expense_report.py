import unittest

from day1 import expense_report


class MyTestCase(unittest.TestCase):
    def test_something(self):
        expenses = [1721, 979, 366, 299, 675, 1456]
        expected = 514579
        answer = expense_report.calculate(expenses, 2020)
        self.assertEqual(expected, answer)




if __name__ == '__main__':
    unittest.main()
