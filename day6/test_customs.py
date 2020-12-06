import unittest

from day6 import customs


class MyTestCase(unittest.TestCase):
    def test_number_one_person(self):
        group_answers = ['abc']
        self.assertEqual(3, customs.number_of_yes(group_answers))

    def test_3_people_no_duplicates(self):
        group_answers = ['a', 'b', 'c']
        self.assertEqual(0, customs.number_of_yes(group_answers))

    def test_duplicates(self):
        group_answers = ['ab', 'ac']
        self.assertEqual(1, customs.number_of_yes(group_answers))

    def test_all_same_question(self):
        group_answers = ['a', 'a', 'a', 'a']
        self.assertEqual(1, customs.number_of_yes(group_answers))

    def test_one_question(self):
        group_answers = ['b']
        self.assertEqual(1, customs.number_of_yes(group_answers))

    def test_parse(self):
        answers = """abc

a
b
c

ab
ac

a
a
a
a

b"""
        expected_answers = [['abc'], ['a', 'b', 'c'], ['ab', 'ac'], ['a', 'a', 'a', 'a'], ['b']]
        self.assertEqual(expected_answers, customs.parse(answers))

if __name__ == '__main__':
    unittest.main()
