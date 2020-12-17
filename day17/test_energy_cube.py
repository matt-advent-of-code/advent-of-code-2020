import unittest
import numpy

from day17 import energy_cube


class MyTestCase(unittest.TestCase):
    def test_something(self):
        starting_state = """.#.
..#
###"""
        energy_cube.init_state(starting_state)
        energy_cube.cycle()
        print(energy_cube.cubes)
        self.assertEqual(29, energy_cube.get_active())


    def test_six_cycles(self):
            starting_state = """.#.
..#
###"""
            energy_cube.init_state(starting_state)
            energy_cube.cycle()
            energy_cube.cycle()
            energy_cube.cycle()
            energy_cube.cycle()
            energy_cube.cycle()
            energy_cube.cycle()
            self.assertEqual(848, energy_cube.get_active())


if __name__ == '__main__':
    unittest.main()
