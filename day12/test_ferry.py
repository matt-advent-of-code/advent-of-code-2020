import unittest

from day12.ferry import Ship


class MyTestCase(unittest.TestCase):
    def test_ferry(self):
        ship = Ship((0, 0), 'E')
        self.assertEqual((0, 0), ship.coordinates)

    def test_move_north(self):
        ship = Ship((0, 0), 'E')
        ship.move('N3')
        self.assertEqual((0, 3), ship.coordinates)

    def test_move_south(self):
        ship = Ship((0, 0), 'E')
        ship.move('S3')
        self.assertEqual((0, -3), ship.coordinates)

    def test_move_east(self):
        ship = Ship((0, 0), 'E')
        ship.move('E3')
        self.assertEqual((3, 0), ship.coordinates)

    def test_move_west(self):
        ship = Ship((0, 0), 'E')
        ship.move('W3')
        self.assertEqual((-3, 0), ship.coordinates)

    def test_move_forward(self):
        ship = Ship((0, 0), 'E')
        ship.move('F10')
        self.assertEqual((10, 0), ship.coordinates)

    def test_right_90(self):
        ship = Ship((0, 0), 'E')
        ship.move('R90')
        self.assertEqual('S', ship.direction)

    def test_right_180(self):
        ship = Ship((0, 0), 'E')
        ship.move('R180')
        self.assertEqual('W', ship.direction)

    def test_right_270(self):
        ship = Ship((0, 0), 'E')
        ship.move('R270')
        self.assertEqual('N', ship.direction)

    def test_right_450(self):
        ship = Ship((0, 0), 'E')
        ship.move('R450')
        self.assertEqual('S', ship.direction)

    def test_left_90(self):
        ship = Ship((0, 0), 'E')
        ship.move('L90')
        self.assertEqual('N', ship.direction)

    def test_left_90_north(self):
        ship = Ship((0, 0), 'N')
        ship.move('L90')
        self.assertEqual('W', ship.direction)

    def test_left_180(self):
        ship = Ship((0, 0), 'E')
        ship.move('L180')
        self.assertEqual('W', ship.direction)

    def test_left_270(self):
        ship = Ship((0, 0), 'E')
        ship.move('L270')
        self.assertEqual('S', ship.direction)

    def test_left_450(self):
        ship = Ship((0, 0), 'E')
        ship.move('L450')
        self.assertEqual('N', ship.direction)

    def test_move(self):
        ship = Ship((0, 0), 'E')
        ship.move('F10')
        ship.move('N3')
        ship.move('F7')
        ship.move('R90')
        ship.move('F11')

        self.assertEqual((17, -8), ship.coordinates)


if __name__ == '__main__':
    unittest.main()
