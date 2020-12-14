import unittest

from day14 import bitmask


class MyTestCase(unittest.TestCase):



    def test_write_to_floating(self):
        bitmask.mask = '000000000000000000000000000000X1001X'
        bitmask.put(42, 100)

        self.assertEqual(100, bitmask.get(26))
        self.assertEqual(100, bitmask.get(27))
        self.assertEqual(100, bitmask.get(58))
        self.assertEqual(100, bitmask.get(59))

    def test_write_to_floating2(self):
        bitmask.mask = '00000000000000000000000000000000X0XX'
        bitmask.put(26, 1)

        self.assertEqual(1, bitmask.get(16))
        self.assertEqual(1, bitmask.get(17))
        self.assertEqual(1, bitmask.get(18))
        self.assertEqual(1, bitmask.get(19))
        self.assertEqual(1, bitmask.get(24))
        self.assertEqual(1, bitmask.get(25))
        self.assertEqual(1, bitmask.get(26))
        self.assertEqual(1, bitmask.get(27))


    def test_initialization(self):
        input = """mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1"""
        bitmask.initialize(input)
        sum_of_memory = sum(bitmask.mem.values())
        self.assertEqual(208, sum_of_memory)


if __name__ == '__main__':
    unittest.main()
