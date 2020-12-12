import unittest

from day12.ferry import Ship


class MyTestCase(unittest.TestCase):
    def test_ferry(self):
        ship = Ship((0, 0), (10, 1))
        self.assertEqual((0, 0), ship.coordinates)
        self.assertEqual((10, 1), ship.waypoint)

    def test_move_north(self):
        ship = Ship((0, 0), (10, 1))
        ship.move('N3')
        self.assertEqual((0, 0), ship.coordinates)
        self.assertEqual((10, 4), ship.waypoint)

    def test_move_south(self):
        ship = Ship((0, 0), (10, 1))
        ship.move('S3')
        self.assertEqual((0, 0), ship.coordinates)
        self.assertEqual((10, -2), ship.waypoint)

    def test_move_east(self):
        ship = Ship((0, 0), (10, 1))
        ship.move('E3')
        self.assertEqual((0, 0), ship.coordinates)
        self.assertEqual((13, 1), ship.waypoint)

    def test_move_west(self):
        ship = Ship((0, 0), (10, 1))
        ship.move('W3')
        self.assertEqual((0, 0), ship.coordinates)
        self.assertEqual((7, 1), ship.waypoint)

    def test_move_forward(self):
        ship = Ship((0, 0), (10, 1))
        ship.move('F10')
        self.assertEqual((100, 10), ship.coordinates)
        self.assertEqual((110, 11), ship.waypoint)

    def test_move_negative(self):
        ship = Ship((0, 0), (-10, -1))
        ship.move('F10')
        self.assertEqual((-100, -10), ship.coordinates)
        self.assertEqual((-110, -11), ship.waypoint)

    def test_right_90(self):
        ship = Ship((170, 38), (180, 42))
        ship.move('R90')
        self.assertEqual((174, 28), ship.waypoint)

    def test_right_180(self):
        ship = Ship((0, 0), (1, 0))
        ship.move('R180')
        self.assertEqual((-1, 0), ship.waypoint)

    def test_right_270(self):
        ship = Ship((0, 0), (1, 0))
        ship.move('R270')
        self.assertEqual((0, 1), ship.waypoint)

    def test_right_450(self):
        ship = Ship((0, 0), (1, 0))
        ship.move('R450')
        self.assertEqual((0, -1), ship.waypoint)

    def test_left_90(self):
        ship = Ship((0, 0), (1, 0))
        ship.move('L90')
        self.assertEqual((0, 1), ship.waypoint)

    def test_left_180(self):
        ship = Ship((0, 0), (1, 0))
        ship.move('L180')
        self.assertEqual((-1, 0), ship.waypoint)

    def test_left_270(self):
        ship = Ship((0, 0), (1, 0))
        ship.move('L270')
        self.assertEqual((0, -1), ship.waypoint)

    def test_left_450(self):
        ship = Ship((0, 0), (1, 0))
        ship.move('L450')
        self.assertEqual((0, 1), ship.waypoint)

    def test_move(self):
        ship = Ship((0, 0), (10, 1))
        ship.move('F10')
        ship.move('N3')
        ship.move('F7')
        ship.move('R90')
        ship.move('F11')

        self.assertEqual((214, -72), ship.coordinates)


if __name__ == '__main__':
    unittest.main()
