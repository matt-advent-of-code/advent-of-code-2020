import re


def parse(data: str) -> dict:
    bags = {}
    for bag_text in data.splitlines():
        name = re.match("(.*) bags contain", bag_text).group(1)
        inner_bags = re.findall("\d+(.*?) bag", bag_text)
        bags[name] = [inner_bag.strip() for inner_bag in inner_bags]
    return bags


def contains(bag_to_check: str, bag_to_check_for: str, bags_to_check: dict) -> bool:
    if bag_to_check_for in bags_to_check[bag_to_check]:
        return True
    else:
        return True in [contains(bag, bag_to_check_for, bags_to_check) for bag in bags_to_check[bag_to_check]]


if __name__ == '__main__':
    bag_count = 0
    with open('input.txt') as data:
        bags = parse(data.read())
        bag_to_check_for = 'shiny gold'
        for bag in bags:
            if contains(bag, bag_to_check_for, bags):
                bag_count += 1

    print(bag_count)
