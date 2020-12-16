import unittest

from day16 import ticket


class MyTestCase(unittest.TestCase):
    def test_parse(self):
        input = """departure location: 27-180 or 187-953
departure station: 47-527 or 545-958

your ticket:
97,61,53,101,131,163,79,103,67,127,71,109,89,107,83,73,113,59,137,139

nearby tickets:
93,566,873,796,908,899,408,393,621,571,546,549,494,631,940,491,561,108,395,258
609,949,551,408,648,723,627,428,905,665,248,557,630,169,494,583,680,658,677,385"""
        expected_tickets = {
            "fields": {
                "departure location": ["27-180", "187-953"],
                "departure station": ["47-527", "545-958"]
            },
            "ticket": [97, 61, 53, 101, 131, 163, 79, 103, 67, 127, 71, 109, 89, 107, 83, 73, 113, 59, 137, 139],
            "nearby_tickets": [
                [93, 566, 873, 796, 908, 899, 408, 393, 621, 571, 546, 549, 494, 631, 940, 491, 561, 108, 395, 258],
                [609, 949, 551, 408, 648, 723, 627, 428, 905, 665, 248, 557, 630, 169, 494, 583, 680, 658, 677, 385]
            ]
        }
        tickets = ticket.parse(input)
        self.assertEqual(expected_tickets, tickets)

    def test_find_invalid_fields_all_valid(self):
        fields = {
            'class': ['1-3', '5-7'],
            'row': ['6-11', '33-44'],
            'seat': ['13-40', '45-50']
        }
        train_ticket = [7, 3, 47]
        self.assertEqual([], ticket.find_invalid_fields(train_ticket, fields))

    def test_find_invalid_fields_invalid(self):
        fields = {
            'class': ['1-3', '5-7'],
            'row': ['6-11', '33-44'],
            'seat': ['13-40', '45-50']
        }
        train_ticket = [40,4,50]
        self.assertEqual([4], ticket.find_invalid_fields(train_ticket, fields))


    def test_find_invalid_fields_invalid_2(self):
        fields = {
            'class': ['1-3', '5-7'],
            'row': ['6-11', '33-44'],
            'seat': ['13-40', '45-50']
        }
        train_ticket = [55,2,20]
        self.assertEqual([55], ticket.find_invalid_fields(train_ticket, fields))


    def test_find_invalid_fields_invalid_3(self):
        fields = {
            'class': ['1-3', '5-7'],
            'row': ['6-11', '33-44'],
            'seat': ['13-40', '45-50']
        }
        train_ticket = [38,6,12]
        self.assertEqual([12], ticket.find_invalid_fields(train_ticket, fields))


    def test_find_error_rate(self):
        input = """class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12"""
        expected_error_rate = 71
        error_rate = ticket.calculate_error_rate(input)
        self.assertEqual(expected_error_rate, error_rate)


if __name__ == '__main__':
    unittest.main()
