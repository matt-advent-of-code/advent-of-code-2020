import unittest

from day23 import cup

class MyTestCase(unittest.TestCase):
    def test_10_000_000(self):
        input = '389125467'
        expected = (934001, 159792)
        cups = cup.play(input, 10000000)
        self.assertEqual(expected, cups)


if __name__ == '__main__':
    unittest.main()
