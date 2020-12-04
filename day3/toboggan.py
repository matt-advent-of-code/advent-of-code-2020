import numpy

TREE = '#'


def calculate(route: str, slopes: list) -> int:
    trees = [count_trees(route, slope) for slope in slopes]
    return numpy.prod(trees)


def count_trees(route: str, slope: tuple) -> int:
    parsed_route = parse(route)
    x = 0
    y = 0
    tree_count = 0
    while y < len(parsed_route):
        if parsed_route[y][x] == TREE:
            tree_count += 1
        x += slope[0]
        if x >= len(parsed_route[y]):
            x = x - len(parsed_route[y])
        y += slope[1]

    return tree_count


def parse(route: str) -> list:
    return [list(x) for x in route.splitlines()]


if __name__ == '__main__':
    with open('input.txt') as data:
        slopes = [(1,1), (3,1), (5,1), (7,1), (1,2)]
        print(calculate(data.read(), slopes))
