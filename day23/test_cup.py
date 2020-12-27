import unittest

from day23 import crab


class MyTestCase(unittest.TestCase):
    def test_10_rounds(self):
        input = '389125467'
        expected_order = '92658374'
        order = crab.play(input, 10)
        self.assertEqual(expected_order, order)

    def test_100_rounds(self):
        input = '389125467'
        expected_order = '67384529'
        order = crab.play(input, 100)
        self.assertEqual(expected_order, order)


if __name__ == '__main__':
    unittest.main()
