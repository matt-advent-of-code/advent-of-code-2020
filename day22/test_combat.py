import unittest

from day22 import combat


class MyTestCase(unittest.TestCase):
    def test_combat(self):

        player1 = [9, 2, 6, 3, 1]
        player2 = [5, 8, 4, 7, 10]

        expected_winning_score = 291
        winning_score = combat.play(player1, player2)


        self.assertEqual(expected_winning_score, winning_score[1])


    def test_infinite_game(self):
        player1 = [43, 19]
        player2 = [2, 29, 14]
        combat.play(player1, player2)


if __name__ == '__main__':
    unittest.main()
