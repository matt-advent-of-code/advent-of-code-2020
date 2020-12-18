import unittest

from day18 import new_math


class MyTestCase(unittest.TestCase):
    def test_simple_add(self):
        expression = '3 + 2'
        expected_answer = 5
        answer = new_math.calculate(expression)
        self.assertEqual(expected_answer, answer)

    def test_multiple_add(self):
        expression = '3 + 2 + 5'
        expected_answer = 10
        answer = new_math.calculate(expression)
        self.assertEqual(expected_answer, answer)

    def test_multiply(self):
        expression = '3 + 2 + 5'
        expected_answer = 10
        answer = new_math.calculate(expression)
        self.assertEqual(expected_answer, answer)

    def test_order(self):
        expression = '1 + 2 * 3 + 4 * 5 + 6'
        expected_answer = 71
        answer = new_math.calculate(expression)
        self.assertEqual(expected_answer, answer)

    def test_parentheses(self):
        expression = '(1 + 1)'
        expected_answer = 2
        answer = new_math.calculate(expression)
        self.assertEqual(expected_answer, answer)

    def test_complex_parentheses(self):
        expression = '1 + (2 * 3) + (4 * (5 + 6))'
        expected_answer = 51
        answer = new_math.calculate(expression)
        self.assertEqual(expected_answer, answer)


    def test_example_1(self):
        expression = '2 * 3 + (4 * 5)'
        expected_answer = 26
        answer = new_math.calculate(expression)
        self.assertEqual(expected_answer, answer)

    def test_example_2(self):
        expression = '5 + (8 * 3 + 9 + 3 * 4 * 3)'
        expected_answer = 437
        answer = new_math.calculate(expression)
        self.assertEqual(expected_answer, answer)

    def test_example_3(self):
        expression = '5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))'
        expected_answer = 12240
        answer = new_math.calculate(expression)
        self.assertEqual(expected_answer, answer)

    def test_example_4(self):
        expression = '((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2'
        expected_answer = 13632
        answer = new_math.calculate(expression)
        self.assertEqual(expected_answer, answer)


    def test_example_4_simp(self):
        expression = '((1 + 1) * (1 + 1) + 6)'
        expected_answer = 10
        answer = new_math.calculate(expression)
        self.assertEqual(expected_answer, answer)



if __name__ == '__main__':
    unittest.main()
