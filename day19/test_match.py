import unittest

from day19 import match


class MyTestCase(unittest.TestCase):
    def test_single(self):
        rules = """0: 1 2
1: "a"
2: 1 3 | 3 1
3: "b"""
        message = 'a'
        self.assertTrue(match.matches(rules, message, 1))


    def test_or(self):
        rules = """0: 1 2
1: "a"
2: 1 3 | 3 1
3: "b"""
        message = 'aab'
        self.assertTrue(match.matches(rules, message, 0))

    def test_or_2(self):
        rules = """0: 1 2
1: "a"
2: 1 3 | 3 1
3: "b"""
        message = 'aba'
        self.assertTrue(match.matches(rules, message, 0))

    def test_no_match(self):
        rules = """0: 1 2
1: "a"
2: 1 3 | 3 1
3: "b"""
        message = 'aaa'
        self.assertFalse(match.matches(rules, message, 0))

    def test_no_match_length(self):
        rules = """0: 1 2
1: "a"
2: 1 3 | 3 1
3: "b"""
        message = 'abaa'
        self.assertFalse(match.matches(rules, message, 0))


    def test_sample(self):
        rules = """0: 4 1 5
1: 2 3 | 3 2
2: 4 4 | 5 5
3: 4 5 | 5 4
4: "a"
5: "b"""

        self.assertTrue(match.matches(rules, 'ababbb', 0))
        self.assertTrue(match.matches(rules, 'abbbab', 0))

        self.assertFalse(match.matches(rules, 'bababa', 0))
        self.assertFalse(match.matches(rules, 'aaabbb', 0))
        self.assertFalse(match.matches(rules, 'aaaabbb', 0))





if __name__ == '__main__':
    unittest.main()
