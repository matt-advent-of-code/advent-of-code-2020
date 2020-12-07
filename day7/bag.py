import re


def parse(data: str) -> dict:
    bags = {}
    for bag_text in data.splitlines():
        name = re.match("(.*) bags contain", bag_text).group(1)
        inner_bags = re.findall("(\d+ .*?) bag", bag_text)
        bags[name] = [{inner_bag[inner_bag.find(" "):].strip(): int(inner_bag[:inner_bag.find(" ")])} for inner_bag in
                      inner_bags]
    return bags


def contains(bag_to_check: str, bag_to_check_for: str, bags_to_check: dict) -> bool:
    if bag_to_check_for in bags_to_check[bag_to_check]:
        return True
    else:
        return True in [contains(bag, bag_to_check_for, bags_to_check) for bag in bags_to_check[bag_to_check]]


def count(bag: str, bags: dict) -> int:
    if not bags[bag]:
        return 0
    bag_count = 0
    for b in bags[bag]:
        key = list(b.keys())[0]
        value = b[key]
        inner_bags = count(key, bags)
        bag_count += inner_bags * value + value
    return bag_count


if __name__ == '__main__':
    with open('input.txt') as data:
        bags = parse(data.read())
        bag_to_count = 'shiny gold'
        print(count(bag_to_count, bags))
