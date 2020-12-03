import unittest

from day2 import password


class MyTestCase(unittest.TestCase):
    def test_valid_password(self):
        policy_character = 'a'
        user_password = 'abcde'
        min = 1
        max = 3
        self.assertTrue(password.is_valid(user_password, policy_character, min, max))

    def test_invalid_password(self):
        policy_character = 'b'
        user_password = 'cdefg'
        min = 1
        max = 3
        self.assertFalse(password.is_valid(user_password, policy_character, min, max))

    def test_valid_same_char(self):
        policy_character = 'c'
        user_password = 'ccccccccc'
        min = 2
        max = 9
        self.assertTrue(password.is_valid(user_password, policy_character, min, max))

    def test_valid_policy(self):
        policy = '1-3 a: abcde'
        self.assertTrue(password.is_valid_policy(policy))


if __name__ == '__main__':
    unittest.main()
