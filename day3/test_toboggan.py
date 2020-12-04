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


if __name__ == '__main__':
    unittest.main()
