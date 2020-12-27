import unittest

from day21 import food


class MyTestCase(unittest.TestCase):
    def test_something(self):
        input = """mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
trh fvjkl sbzzf mxmxvkd (contains dairy)
sqjhc fvjkl (contains soy)
sqjhc mxmxvkd sbzzf (contains fish)"""
        expected_allergy_free_ingredients = ['kfcds', 'nhms', 'trh', 'sbzzf', 'sbzzf']
        allergy_free_ingredients = food.find_allergy_free_ingredients(input)
        self.assertEqual(expected_allergy_free_ingredients, allergy_free_ingredients)


if __name__ == '__main__':
    unittest.main()
