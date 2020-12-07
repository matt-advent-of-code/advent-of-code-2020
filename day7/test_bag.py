import unittest

from day7 import bag


class MyTestCase(unittest.TestCase):
    def test_parse(self):
        text = """light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags."""

        expected_bags = {
            'light red': [{'bright white': 1}, {'muted yellow': 2}],
            'dark orange': [{'bright white': 3}, {'muted yellow': 4}],
            'bright white': [{'shiny gold': 1}],
            'muted yellow': [{'shiny gold': 2}, {'faded blue': 9}],
            'shiny gold': [{'dark olive': 1}, {'vibrant plum': 2}],
            'dark olive': [{'faded blue': 3}, {'dotted black': 4}],
            'vibrant plum': [{'faded blue': 5}, {'dotted black': 6}],
            'faded blue': [],
            'dotted black': []
        }

        bags = bag.parse(text)
        self.assertEqual(expected_bags, bags)

    def test_contains_bag(self):
        bag_to_check = 'bright white'
        bags = {
            'light red': ['bright white', 'muted yellow'],
            'dark orange': ['bright white', 'muted yellow'],
            'bright white': ['shiny gold'],
            'muted yellow': ['shiny gold', 'faded blue'],
            'shiny gold': ['dark olive', 'vibrant plum'],
            'dark olive': ['faded blue', 'dotted black'],
            'vibrant plum': ['faded blue', 'dotted black'],
            'faded blue': [],
            'dotted black': []
        }
        self.assertTrue(bag.contains(bag_to_check, 'shiny gold', bags))

    def test_contains_bag_multi_inside(self):
        bag_to_check = 'muted yellow'
        bags = {
            'light red': ['bright white', 'muted yellow'],
            'dark orange': ['bright white', 'muted yellow'],
            'bright white': ['shiny gold'],
            'muted yellow': ['shiny gold', 'faded blue'],
            'shiny gold': ['dark olive', 'vibrant plum'],
            'dark olive': ['faded blue', 'dotted black'],
            'vibrant plum': ['faded blue', 'dotted black'],
            'faded blue': [],
            'dotted black': []
        }
        self.assertTrue(bag.contains(bag_to_check, 'shiny gold', bags))


    def test_contains_bag_one_away(self):
        bag_to_check = 'dark orange'
        bags = {
            'light red': ['bright white', 'muted yellow'],
            'dark orange': ['bright white', 'muted yellow'],
            'bright white': ['shiny gold'],
            'muted yellow': ['shiny gold', 'faded blue'],
            'shiny gold': ['dark olive', 'vibrant plum'],
            'dark olive': ['faded blue', 'dotted black'],
            'vibrant plum': ['faded blue', 'dotted black'],
            'faded blue': [],
            'dotted black': []
        }
        self.assertTrue(bag.contains(bag_to_check, 'shiny gold', bags))


    def test_contains_bag_one_away2(self):
        bag_to_check = 'light red'
        bags = {
            'light red': ['bright white', 'muted yellow'],
            'dark orange': ['bright white', 'muted yellow'],
            'bright white': ['shiny gold'],
            'muted yellow': ['shiny gold', 'faded blue'],
            'shiny gold': ['dark olive', 'vibrant plum'],
            'dark olive': ['faded blue', 'dotted black'],
            'vibrant plum': ['faded blue', 'dotted black'],
            'faded blue': [],
            'dotted black': []
        }
        self.assertTrue(bag.contains(bag_to_check, 'shiny gold', bags))


    def test_does_not_contains_bag_empty(self):
        bag_to_check = 'faded blue'
        bags = {
            'light red': ['bright white', 'muted yellow'],
            'dark orange': ['bright white', 'muted yellow'],
            'bright white': ['shiny gold'],
            'muted yellow': ['shiny gold', 'faded blue'],
            'shiny gold': ['dark olive', 'vibrant plum'],
            'dark olive': ['faded blue', 'dotted black'],
            'vibrant plum': ['faded blue', 'dotted black'],
            'faded blue': [],
            'dotted black': []
        }
        self.assertFalse(bag.contains(bag_to_check, 'shiny gold', bags))

    def test_does_not_contains_bag(self):
        bag_to_check = 'dark olive'
        bags = {
            'light red': ['bright white', 'muted yellow'],
            'dark orange': ['bright white', 'muted yellow'],
            'bright white': ['shiny gold'],
            'muted yellow': ['shiny gold', 'faded blue'],
            'shiny gold': ['dark olive', 'vibrant plum'],
            'dark olive': ['faded blue', 'dotted black'],
            'vibrant plum': ['faded blue', 'dotted black'],
            'faded blue': [],
            'dotted black': []
        }
        self.assertFalse(bag.contains(bag_to_check, 'shiny gold', bags))


    def test_does_not_contains_bag_same(self):
        bag_to_check = 'shiny gold'
        bags = {
            'light red': ['bright white', 'muted yellow'],
            'dark orange': ['bright white', 'muted yellow'],
            'bright white': ['shiny gold'],
            'muted yellow': ['shiny gold', 'faded blue'],
            'shiny gold': ['dark olive', 'vibrant plum'],
            'dark olive': ['faded blue', 'dotted black'],
            'vibrant plum': ['faded blue', 'dotted black'],
            'faded blue': [],
            'dotted black': []
        }
        self.assertFalse(bag.contains(bag_to_check, 'shiny gold', bags))


    def test_count_bags(self):
        bag_to_count = 'faded blue'
        bags = {
            'light red': [{'bright white': 1}, {'muted yellow': 2}],
            'dark orange': [{'bright white': 3}, {'muted yellow': 4}],
            'bright white': [{'shiny gold': 1}],
            'muted yellow': [{'shiny gold': 2}, {'faded blue': 9}],
            'shiny gold': [{'dark olive': 1}, {'vibrant plum': 2}],
            'dark olive': [{'faded blue': 3}, {'dotted black': 4}],
            'vibrant plum': [{'faded blue': 5}, {'dotted black': 6}],
            'faded blue': [],
            'dotted black': []
        }
        expected = 0
        count = bag.count(bag_to_count, bags)
        self.assertEqual(expected, count)

    def test_count_bags_plum(self):
        bag_to_count = 'vibrant plum'
        bags = {
            'light red': [{'bright white': 1}, {'muted yellow': 2}],
            'dark orange': [{'bright white': 3}, {'muted yellow': 4}],
            'bright white': [{'shiny gold': 1}],
            'muted yellow': [{'shiny gold': 2}, {'faded blue': 9}],
            'shiny gold': [{'dark olive': 1}, {'vibrant plum': 2}],
            'dark olive': [{'faded blue': 3}, {'dotted black': 4}],
            'vibrant plum': [{'faded blue': 5}, {'dotted black': 6}],
            'faded blue': [],
            'dotted black': []
        }
        expected = 11
        count = bag.count(bag_to_count, bags)
        self.assertEqual(expected, count)


    def test_count_dark_olive(self):
        bag_to_count = 'dark olive'
        bags = {
            'light red': [{'bright white': 1}, {'muted yellow': 2}],
            'dark orange': [{'bright white': 3}, {'muted yellow': 4}],
            'bright white': [{'shiny gold': 1}],
            'muted yellow': [{'shiny gold': 2}, {'faded blue': 9}],
            'shiny gold': [{'dark olive': 1}, {'vibrant plum': 2}],
            'dark olive': [{'faded blue': 3}, {'dotted black': 4}],
            'vibrant plum': [{'faded blue': 5}, {'dotted black': 6}],
            'faded blue': [],
            'dotted black': []
        }
        expected = 7
        count = bag.count(bag_to_count, bags)
        self.assertEqual(expected, count)


    def test_count_shiny_gold(self):
        bag_to_count = 'shiny gold'
        bags = {
            'light red': [{'bright white': 1}, {'muted yellow': 2}],
            'dark orange': [{'bright white': 3}, {'muted yellow': 4}],
            'bright white': [{'shiny gold': 1}],
            'muted yellow': [{'shiny gold': 2}, {'faded blue': 9}],
            'shiny gold': [{'dark olive': 1}, {'vibrant plum': 2}],
            'dark olive': [{'faded blue': 3}, {'dotted black': 4}],
            'vibrant plum': [{'faded blue': 5}, {'dotted black': 6}],
            'faded blue': [],
            'dotted black': []
        }
        expected = 32
        count = bag.count(bag_to_count, bags)
        self.assertEqual(expected, count)


if __name__ == '__main__':
    unittest.main()
