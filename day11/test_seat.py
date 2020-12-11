import unittest

from day11 import seat


class MyTestCase(unittest.TestCase):
    def test_parse(self):
        input = """L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL"""
        seats = seat.parse(input)
        self.assertEqual(10, len(seats))
        self.assertEqual(10, len(seats[0]))

    def test_all_floor(self):
        seats = [['.', '.'], ['.'], ['.']]
        expected = seats
        seats = seat.next_round(seats)
        self.assertEqual(expected, seats)

    def test_empty_seats(self):
        input = """L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL"""
        expected = """#.##.##.##
#######.##
#.#.#..#..
####.##.##
#.##.##.##
#.#####.##
..#.#.....
##########
#.######.#
#.#####.##"""

        seats = seat.parse(input)
        seats = seat.next_round(seats)
        self.assertEqual(expected, seat.to_string(seats))

    def test_all_full_seats(self):
        input = """#.##.##.##
#######.##
#.#.#..#..
####.##.##
#.##.##.##
#.#####.##
..#.#.....
##########
#.######.#
#.#####.##"""
        expected = """#.LL.LL.L#
#LLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLL#
#.LLLLLL.L
#.LLLLL.L#"""

        seats = seat.parse(input)
        seats = seat.next_round(seats)
        self.assertEqual(expected, seat.to_string(seats))


    def test_run_simulation(self):
        input = '''L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL'''

        seats = seat.run(input)
        count = 0
        for i in seats:
            for j in i:
                if j == '#':
                    count += 1
        self.assertEqual(26, count)


    def test_find_visible_seats(self):
        input = """#.##.##.##
#######.##
#.#.#..#..
####.##.##
#.##.##.##
#.#####.##
..#.#.....
##########
#.######.#
#.#####.##"""

        seats = seat.parse(input)

        visible_seats = seat.find_visible_seats(seats, 3, 9)
        expected_visible_seats = ['#', '#', '#', '#', '.', '.', '.', '#']
        print(visible_seats)
        self.assertEqual(expected_visible_seats, visible_seats)


if __name__ == '__main__':
    unittest.main()
