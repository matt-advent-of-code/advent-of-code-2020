import unittest

from day25 import card


class MyTestCase(unittest.TestCase):
    def test_crack_card_loop_size(self):
        card_public_key = 5764801
        subject_number = 7

        expected_loop_size = 8
        loop_size = card.crack_loop_size(card_public_key, subject_number)

        self.assertEqual(expected_loop_size, loop_size)

    def test_crack_door_loop_size(self):
        door_public_key = 17807724
        subject_number = 7

        expected_loop_size = 11
        loop_size = card.crack_loop_size(door_public_key, subject_number)

        self.assertEqual(expected_loop_size, loop_size)

    def test_crack_encryption_key(self):
        card_public_key = 5764801
        door_public_key = 17807724
        subject_number = 7

        expected_encryption_key = 14897079

        encryption_key = card.crack_encryption_key(card_public_key, door_public_key, subject_number)

        self.assertEqual(expected_encryption_key, encryption_key)




if __name__ == '__main__':
    unittest.main()
