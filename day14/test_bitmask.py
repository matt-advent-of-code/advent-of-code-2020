import unittest

from day14 import bitmask


class MyTestCase(unittest.TestCase):
    def test_mask_change(self):
        bitmask.mask = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X'
        bitmask.put(8, 11)
        result = bitmask.get(8)
        self.assertEqual(73, result)

    def test_no_mask_change(self):
        bitmask.mask = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X'
        bitmask.put(7, 101)
        result = bitmask.get(7)
        self.assertEqual(101, result)

    def test_no_mask_zero(self):
        bitmask.mask = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X'
        bitmask.put(8, 0)
        result = bitmask.get(8)
        self.assertEqual(64, result)


    def test_initialization(self):
        input = """mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0"""
        bitmask.initialize(input)
        sum_of_memory = sum(bitmask.mem.values())
        self.assertEqual(165, sum_of_memory)


if __name__ == '__main__':
    unittest.main()
