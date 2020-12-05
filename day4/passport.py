import re

REQUIRED_FIELDS = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']


def parse(data: str) -> list:
    return [parse_passport(passport) for passport in data.split("\n\n")]


def parse_passport(data: str) -> dict:
    passport = {}
    fields = re.findall(r"[\w']+", data)
    for i in range(0, len(fields), 2):
        passport[fields[i]] = fields[i + 1]
    return passport


def is_valid(passport: dict) -> bool:
    return all([field in passport for field in REQUIRED_FIELDS])


if __name__ == '__main__':
    valid_passports = 0
    with open('input.txt') as data:
        passports = parse(data.read())
        for passport in passports:
            if is_valid(passport):
                valid_passports += 1
    print(valid_passports)
