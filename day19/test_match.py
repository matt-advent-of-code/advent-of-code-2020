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
        rules = """0: 8
8: 42 | 42 8
31: 14 17 | 1 13
42: 9 14 | 10 1
14: "a"
9: "b"
10: "a"
1: "a"
5: "b"""

        self.assertTrue(match.matches(rules, 'a', 0))



    def test_small_loop(self):
        rules = """0: 1 2
        1: "a"
        2: 1 2 4 | 3
        3: "b\"
        4: 2 1"""
        self.assertTrue(match.matches(rules, 'aabba', 0))

    def test_loop(self):
        rules = """42: 9 14 | 10 1
9: 14 27 | 1 26
10: 23 14 | 28 1
1: "a"
11: 42 31 | 42 11 31
5: 1 14 | 15 1
19: 14 1 | 14 14
12: 24 14 | 19 1
16: 15 1 | 14 14
31: 14 17 | 1 13
6: 14 14 | 1 14
2: 1 24 | 14 4
0: 8 11
13: 14 3 | 1 12
15: 1 | 14
17: 14 2 | 1 7
23: 25 1 | 22 14
28: 16 1
4: 1 1
20: 14 14 | 1 15
3: 5 14 | 16 1
27: 1 6 | 14 18
14: "b"
21: 14 1 | 1 14
25: 1 1 | 1 14
22: 14 14
8: 42 | 42 8
26: 14 22 | 1 20
18: 15 15
7: 14 5 | 1 21
24: 14 1"""
        self.assertTrue(match.matches(rules, 'bbabbbbaabaabba', 0))
        self.assertTrue(match.matches(rules, 'babbbbaabbbbbabbbbbbaabaaabaaa', 0))
        self.assertTrue(match.matches(rules, 'aaabbbbbbaaaabaababaabababbabaaabbababababaaa', 0))
#        self.assertTrue(match.matches(rules, 'bbbbbbbaaaabbbbaaabbabaaa', 0))
#        self.assertTrue(match.matches(rules, 'bbbababbbbaaaaaaaabbababaaababaabab', 0))
        self.assertTrue(match.matches(rules, 'ababaaaaaabaaab', 0))
        self.assertTrue(match.matches(rules, 'ababaaaaabbbaba', 0))
        self.assertTrue(match.matches(rules, 'baabbaaaabbaaaababbaababb', 0))
#        self.assertTrue(match.matches(rules, 'abbbbabbbbaaaababbbbbbaaaababb', 0))
#        self.assertTrue(match.matches(rules, 'aaaaabbaabaaaaababaa', 0))
        self.assertTrue(match.matches(rules, 'aaaabbaabbaaaaaaabbbabbbaaabbaabaaa', 0))
#        self.assertTrue(match.matches(rules, 'aabbbbbaabbbaaaaaabbbbbababaaaaabbaaabba', 0))





if __name__ == '__main__':
    unittest.main()
