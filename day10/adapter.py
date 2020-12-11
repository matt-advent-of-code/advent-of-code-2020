import networkx as nx


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

    paths = {0: 1}
    for i in range(1, len(sorted_adapters)):
        j = i - 1
        number_of_paths = 0
        while j >= 0 and sorted_adapters[i] - sorted_adapters[j] <= 3:
            number_of_paths += paths[sorted_adapters[j]]
            j = j - 1
        paths[sorted_adapters[i]] = number_of_paths

    return paths[sorted_adapters[-1]]


if __name__ == '__main__':
    with open('input.txt') as data:
        adapters = [int(adapter) for adapter in data.readlines()]
        print(find_arrangements(adapters))
