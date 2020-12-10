def find_diffs(adapters: list) -> tuple:
    diffs = {}
    sorted_adapters = adapters.copy()
    sorted_adapters.append(0)
    sorted_adapters.sort()
    sorted_adapters.append(sorted_adapters[-1] + 3)
    for i in range(1, len(sorted_adapters)):
        diff = sorted_adapters[i] - sorted_adapters[i - 1]
        if diff in diffs:
            diffs[diff] += 1
        else:
            diffs[diff] = 1
    return diffs


if __name__ == '__main__':
    with open('input.txt') as data:
        adapters = [int(adapter) for adapter in data.readlines()]
        diffs = find_diffs(adapters)
        print(diffs[1] * diffs[3])
