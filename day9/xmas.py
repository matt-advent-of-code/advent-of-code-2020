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

def find_contiguous_numbers(data: list, invalid_number: int) -> list:
    sub_data = data[:data.index(invalid_number)]
    for i, element in enumerate(sub_data):
        contiguous_numbers = [element]
        for j in range(i+1, len(sub_data)):
            contiguous_numbers.append(sub_data[j])
            if sum(contiguous_numbers) == invalid_number:
                return contiguous_numbers


if __name__ == '__main__':
    with open('input.txt') as data:
        numbers = [int(num) for num in data.readlines()]
        invalid_num = first_invalid(numbers.copy(), 25)
        contiguous_numbers = find_contiguous_numbers(numbers, invalid_num)
        print(min(contiguous_numbers) + max(contiguous_numbers))
