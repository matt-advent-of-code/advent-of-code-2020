def find_diffs(adapters: list) -> tuple:
    diffs = {}
    for i in range(1, len(adapters)):
        diff = adapters[i] - adapters[i - 1]
        if diff in diffs:
            diffs[diff] += 1
        else:
            diffs[diff] = 1
    return diffs


def find_arrangements(adapters: list) -> int:
    sorted_adapters = adapters.copy()
    sorted_adapters.append(0)
    sorted_adapters.sort()
    sorted_adapters.append(sorted_adapters[-1] + 3)
    return __find_arrangements(sorted_adapters, 1)


def __find_arrangements(adapters: list, start: int) -> int:
    sorted_adapters = adapters.copy()
    sorted_adapters.sort()
    number_of_arrangements = 0
    diffs = find_diffs(adapters)
    if max(list(diffs.keys())) <= 3:
        for i in range(start, len(adapters) - 1):
            adapters_copy = sorted_adapters.copy()
            adapters_copy.pop(i)
            number_of_arrangements += __find_arrangements(adapters_copy, i)
        return 1 + number_of_arrangements
    else:
        return 0


if __name__ == '__main__':
    with open('input.txt') as data:
        adapters = [int(adapter) for adapter in data.readlines()]
        print(find_arrangements(adapters))
