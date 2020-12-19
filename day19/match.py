def matches(rules: str, message: str, rule: int) -> bool:
    rules = parse(rules)
    rule_to_match = rules[rule]
    message_list = list(message)
    matches = does_match(rules, rule_to_match, message_list)
    return matches and len(message_list) == 0


def does_match(rules: dict, rule: list, message: list) -> bool:
    if len(rule) == 1 and rule[0].isalpha():
        to_check = message.pop(0)
        return rule[0] == to_check
    if len(rule) == 1:
        matches = [does_match(rules, rules[int(r)], message) for r in rule[0].split(' ')]
        return False not in matches
    else:
        for path in rule:
            message_copy = message.copy()
            matches = [does_match(rules, rules[int(r)], message_copy) for r in path.split(' ')]
            if False not in matches:
                message.clear()
                message.extend(message_copy)
                return True
        return False


def parse(rules: str) -> dict:
    parsed_rules = {}
    for rule in rules.split('\n'):
        key = int(rule.split(':')[0])
        values = [value.strip() for value in rule.replace('"', '').split(':')[1].strip().split('|')]
        parsed_rules[key] = values
    return parsed_rules


if __name__ == '__main__':
    with open('input.txt') as data:
        data_split = data.read().split('\n\n')
        rules = data_split[0]
        total = 0
        for message in data_split[1].split('\n'):
            if matches(rules, message, 0):
                total += 1
        print(total)
