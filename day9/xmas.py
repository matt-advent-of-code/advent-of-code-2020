def is_valid(value: int, preamble: list) -> bool:
    for i in range(len(preamble)):
        for j in preamble[:i] + preamble[i + 1:]:
            if preamble[i] + j == value:
                return True
    return False


def first_invalid(data: list, preamble_size: int) -> int:
    preamble = []
    for i in range(preamble_size):
        preamble.append(data.pop(0))
    value = data[0]
    if not is_valid(value, preamble):
        return value
    else:
        preamble.pop(0)
        return first_invalid(preamble + data, preamble_size)


if __name__ == '__main__':
    with open('input.txt') as data:
        numbers = [int(num) for num in data.readlines()]
        print(first_invalid(numbers, 25))
