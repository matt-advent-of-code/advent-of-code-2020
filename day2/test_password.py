import unittest

from day2 import password


class MyTestCase(unittest.TestCase):
    def test_valid_password(self):
        policy_character = 'a'
        user_password = 'abcde'
        first = 1
        second = 3
        self.assertTrue(password.is_valid(user_password, policy_character, first, second))

    def test_invalid_password(self):
        policy_character = 'b'
        user_password = 'cdefg'
        first = 1
        second = 3
        self.assertFalse(password.is_valid(user_password, policy_character, first, second))

    def test_valid_same_char(self):
        policy_character = 'c'
        user_password = 'ccccccccc'
        first = 2
        second = 9
        self.assertFalse(password.is_valid(user_password, policy_character, first, second))

    def test_valid_policy(self):
        policy = '1-3 a: abcde'
        self.assertTrue(password.is_valid_policy(policy))


if __name__ == '__main__':
    unittest.main()
