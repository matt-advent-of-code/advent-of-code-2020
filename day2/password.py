import re


def is_valid(password: str, policy_character, first: int, second: int) -> bool:
    return (password[first-1] == policy_character) != (password[second-1] == policy_character)


def is_valid_policy(password_policy: str) -> bool:
    policy_attributes = password_policy.split()
    first = int(policy_attributes[0].split("-")[0])
    second = int(policy_attributes[0].split("-")[1])
    policy_character = policy_attributes[1].replace(":", "")
    password = policy_attributes[2]
    return is_valid(password, policy_character, first, second)


if __name__ == '__main__':
    valid_passwords_count = 0
    with open('input.txt') as data:
        for policy in data.read().splitlines():
            if is_valid_policy(policy):
                valid_passwords_count += 1
    print(valid_passwords_count)
