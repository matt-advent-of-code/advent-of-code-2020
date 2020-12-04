import unittest

from day3 import toboggan


class MyTestCase(unittest.TestCase):
    route = """..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#
"""

    def test_something(self):
        trees = toboggan.count_trees(self.route, (3,1))
        self.assertEqual(7, trees)

    def test_count_trees_for_all_slopes(self):
        trees = toboggan.calculate(self.route, [(1,1), (3,1), (5,1), (7,1), (1,2)])
        self.assertEqual(336, trees)


if __name__ == '__main__':
    unittest.main()
