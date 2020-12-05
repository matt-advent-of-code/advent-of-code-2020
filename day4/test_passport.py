import unittest

from day4 import passport
from day4.passport import BirthYearValidator, HeightValidator, HairColorValidator, EyeColorValidator, PidValidator, \
    IssueYearValidator, ExpirationYearValidator


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

    def test_is_invalid_missing_one(self):
        valid_passport = {'iyr': '2013', 'ecl': 'amb', 'cid': '350', 'eyr': '2023', 'pid': '028048884',
                          'hcl': 'cfa07d', 'byr': '1929'}
        self.assertFalse(passport.is_valid(valid_passport))

    def test_is_invalid_missing_cid_and_required(self):
        valid_passport = {'hcl': 'cfa07d', 'eyr': '2025', 'pid': '166559648', 'iyr': '2011', 'ecl': 'brn',
                          'hgt': '59in'}
        self.assertFalse(passport.is_valid(valid_passport))

    def test_birth_year_is_valid(self):
        birth_year = '2002'
        validator = BirthYearValidator()
        self.assertTrue(validator.is_valid(birth_year))

    def test_birth_year_is_invalid(self):
        birth_year = '2003'
        validator = BirthYearValidator()
        self.assertFalse(validator.is_valid(birth_year))

    def test_height_in_is_valid(self):
        height = '60in'
        validator = HeightValidator()
        self.assertTrue(validator.is_valid(height))

    def test_height_cm_is_valid(self):
        height = '190cm'
        validator = HeightValidator()
        self.assertTrue(validator.is_valid(height))

    def test_height_in_is_invalid(self):
        height = '190in'
        validator = HeightValidator()
        self.assertFalse(validator.is_valid(height))

    def test_height_no_mess_is_invalid(self):
        height = '190'
        validator = HeightValidator()
        self.assertFalse(validator.is_valid(height))

    def test_hair_color_valid(self):
        hair_color = '#123abc'
        validator = HairColorValidator()
        self.assertTrue(validator.is_valid(hair_color))

    def test_hair_color_invalid(self):
        hair_color = '#123abz'
        validator = HairColorValidator()
        self.assertFalse(validator.is_valid(hair_color))

    def test_hair_color_invalid_missing_hash(self):
        hair_color = '123abc'
        validator = HairColorValidator()
        self.assertFalse(validator.is_valid(hair_color))

    def test_eye_color_is_valid(self):
        eye_color = 'brn'
        validator = EyeColorValidator()
        self.assertTrue(validator.is_valid(eye_color))

    def test_eye_color_is_invalid(self):
        eye_color = 'wat'
        validator = EyeColorValidator()
        self.assertFalse(validator.is_valid(eye_color))

    def test_pid_is_valid(self):
        pid = '000000001'
        validator = PidValidator()
        self.assertTrue(validator.is_valid(pid))

    def test_pid_is_invalid(self):
        pid = '0123456789'
        validator = PidValidator()
        self.assertFalse(validator.is_valid(pid))

    def test_issue_year_is_valid(self):
        issue_year = '2011'
        validator = IssueYearValidator()
        self.assertTrue(validator.is_valid(issue_year))

    def test_issue_year_is_invalid(self):
        issue_year = '2021'
        validator = IssueYearValidator()
        self.assertFalse(validator.is_valid(issue_year))

    def test_expiration_year_is_valid(self):
        issue_year = '2020'
        validator = ExpirationYearValidator()
        self.assertTrue(validator.is_valid(issue_year))

    def test_expiration__year_is_invalid(self):
        issue_year = '2050'
        validator = ExpirationYearValidator()
        self.assertFalse(validator.is_valid(issue_year))

    def test_invalid_passports(self):
        invalid_passports = """eyr:1972 cid:100
hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

iyr:2019
hcl:#602927 eyr:1967 hgt:170cm
ecl:grn pid:012533040 byr:1946

hcl:dab227 iyr:2012
ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

hgt:59cm ecl:zzz
eyr:2038 hcl:74454a iyr:2023
pid:3556412378 byr:2007"""

        passports = passport.parse(invalid_passports)
        self.assertFalse(all([passport.is_valid(p) for p in passports]))

    def test_valid_passports(self):
        invalid_passports = """pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f

eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022

iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719"""

        passports = passport.parse(invalid_passports)
        self.assertTrue(all([passport.is_valid(p) for p in passports]))


if __name__ == '__main__':
    unittest.main()
