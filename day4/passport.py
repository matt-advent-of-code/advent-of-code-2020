import re

REQUIRED_FIELDS = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']


def parse(data: str) -> list:
    return [parse_passport(passport) for passport in data.split("\n\n")]


def parse_passport(data: str) -> dict:
    passport = {}
    fields = data.strip("\n").replace("\n", " ").replace(" ", ":").split(":")
    for i in range(0, len(fields), 2):
        passport[fields[i]] = fields[i + 1]
    return passport


def is_valid(passport: dict) -> bool:
    return has_required_fields(passport) and has_valid_fields(passport)


def has_required_fields(passport: dict) -> bool:
    return all([field in passport for field in REQUIRED_FIELDS])


def has_valid_fields(passport: dict) -> bool:
    for field in passport:
        validator = get_validator_for(field)
        if not validator.is_valid(passport[field]):
            return False
    return True


class Validator:
    def is_valid(self, field: str) -> bool:
        return True


class BirthYearValidator(Validator):
    def is_valid(self, birth_year: str) -> bool:
        return 1920 <= int(birth_year) <= 2002


class HeightValidator(Validator):
    def is_valid(self, height: str) -> bool:
        if height.endswith('in'):
            return 59 <= int(height[:-2]) <= 76
        elif height.endswith('cm'):
            return 150 <= int(height[:-2]) <= 193
        else:
            return False


class HairColorValidator(Validator):
    def is_valid(self, hair_color: dict) -> bool:
        return re.match("#([0-9]|[a-f]){6}$", hair_color)


class EyeColorValidator(Validator):
    VALID_COLORS = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

    def is_valid(self, eye_color: dict) -> bool:
        return eye_color in self.VALID_COLORS


class PidValidator(Validator):
    def is_valid(self, pid: str) -> bool:
        return re.match("[0-9]{9}$", pid)


class IssueYearValidator(Validator):
    def is_valid(self, issue_year: dict) -> bool:
        return 2010 <= int(issue_year) <= 2020


class ExpirationYearValidator(Validator):
    def is_valid(self, expiration_year: dict) -> bool:
        return 2020 <= int(expiration_year) <= 2030


def get_validator_for(field: str) -> Validator:
    if field == 'byr':
        return BirthYearValidator()
    if field == 'iyr':
        return IssueYearValidator()
    if field == 'eyr':
        return ExpirationYearValidator()
    if field == 'hgt':
        return HeightValidator()
    if field == 'hcl':
        return HairColorValidator()
    if field == 'ecl':
        return EyeColorValidator()
    if field == 'pid':
        return PidValidator()
    if field == 'cid':
        return Validator()
    else:
        raise Exception


if __name__ == '__main__':
    valid_passports = 0
    with open('input.txt') as data:
        passports = parse(data.read())
        for passport in passports:
            if is_valid(passport):
                valid_passports += 1
    print(valid_passports)
