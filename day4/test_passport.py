import unittest

from day4 import passport


class MyTestCase(unittest.TestCase):
    data = """ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in
"""

    def test_parse(self):
        passports = passport.parse(self.data)
        print(passports)
        self.assertEqual(4, len(passports))
        self.assertTrue(isinstance(passports[0], dict))

    def test_is_valid(self):
        valid_passport = {'ecl': 'gry', 'pid': '860033327', 'eyr': '2020', 'hcl': 'fffffd',
                    'byr': '1937', 'iyr': '2017', 'cid': '147', 'hgt': '183cm'}
        self.assertTrue(passport.is_valid(valid_passport))

    def test_is_invalid_missing_one(self):
        valid_passport = {'iyr': '2013', 'ecl': 'amb', 'cid': '350', 'eyr': '2023', 'pid': '028048884',
                          'hcl': 'cfa07d', 'byr': '1929'}
        self.assertFalse(passport.is_valid(valid_passport))

    def test_is_valid_missing_cid(self):
        valid_passport = {'hcl': 'ae17e1', 'iyr': '2013', 'eyr': '2024', 'ecl': 'brn', 'pid': '760753108',
                          'byr': '1931', 'hgt': '179cm'}
        self.assertTrue(passport.is_valid(valid_passport))

    def test_is_invalid_missing_cid_and_required(self):
        valid_passport = {'hcl': 'cfa07d', 'eyr': '2025', 'pid': '166559648', 'iyr': '2011', 'ecl': 'brn', 'hgt': '59in'}
        self.assertFalse(passport.is_valid(valid_passport))


if __name__ == '__main__':
    unittest.main()
