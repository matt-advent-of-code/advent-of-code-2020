TREE = '#'


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
        print(count_trees(data.read(), (3, 1)))
