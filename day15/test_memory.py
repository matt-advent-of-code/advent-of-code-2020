import unittest

from day15 import memory


class MyTestCase(unittest.TestCase):
    def test_first_spoken(self):
        starting_numbers = [0, 3, 6]
        expected_number = 0
        memory.seed(starting_numbers)
        number = memory.next()
        self.assertEqual(expected_number, number)

    def test_repeat_number(self):
        starting_numbers = [0, 3, 6, 0]
        expected_number = 3
        memory.seed(starting_numbers)
        number = memory.next()
        self.assertEqual(expected_number, number)

    def test_repeat_number_2(self):
        starting_numbers = [0, 3, 6, 0, 3]
        expected_number = 3
        memory.seed(starting_numbers)
        number = memory.next()
        self.assertEqual(expected_number, number)

    def test_repeat_number_3(self):
        starting_numbers = [0, 3, 6, 0, 3, 3]
        expected_number = 1
        memory.seed(starting_numbers)
        number = memory.next()
        self.assertEqual(expected_number, number)

    def test_repeat_number_4(self):
        starting_numbers = [0, 3, 6, 0, 3, 3, 1]
        expected_number = 0
        memory.seed(starting_numbers)
        number = memory.next()
        self.assertEqual(expected_number, number)

    def test_repeat_number_5(self):
        starting_numbers = [0, 3, 6, 0, 3, 3, 1, 0]
        expected_number = 4
        memory.seed(starting_numbers)
        number = memory.next()
        self.assertEqual(expected_number, number)

    def test_repeat_number_6(self):
        starting_numbers = [0, 3, 6, 0, 3, 3, 1, 0, 4]
        expected_number = 0
        memory.seed(starting_numbers)
        number = memory.next()
        self.assertEqual(expected_number, number)

    def test_play_game(self):
        starting_numbers = [0, 3, 6]
        memory.seed(starting_numbers)
        memory.play_game(2020)
        expected_number = 436
        self.assertEqual(expected_number, memory.numbers[-1])

    def test_play_game2(self):
        starting_numbers = [1, 3, 2]
        memory.seed(starting_numbers)
        memory.play_game(2020)
        expected_number = 1
        self.assertEqual(expected_number, memory.numbers[-1])

    def test_play_game3(self):
        starting_numbers = [2, 1, 3]
        memory.seed(starting_numbers)
        memory.play_game(2020)
        expected_number = 10
        self.assertEqual(expected_number, memory.numbers[-1])

    def test_play_game4(self):
        starting_numbers = [1, 2, 3]
        memory.seed(starting_numbers)
        memory.play_game(2020)
        expected_number = 27
        self.assertEqual(expected_number, memory.numbers[-1])

    def test_play_game5(self):
        starting_numbers = [2, 3, 1]
        memory.seed(starting_numbers)
        memory.play_game(2020)
        expected_number = 78
        self.assertEqual(expected_number, memory.numbers[-1])

    def test_play_game6(self):
        starting_numbers = [3, 2, 1]
        memory.seed(starting_numbers)
        memory.play_game(2020)
        expected_number = 438
        self.assertEqual(expected_number, memory.numbers[-1])

    def test_play_game7(self):
        starting_numbers = [3, 1, 2]
        memory.seed(starting_numbers)
        memory.play_game(2020)
        expected_number = 1836
        self.assertEqual(expected_number, memory.numbers[-1])


if __name__ == '__main__':
    unittest.main()
