global numbers
numbers = []

order = {}


def seed(starting_numbers: list):
    global numbers
    numbers = starting_numbers
    for i in range(len(starting_numbers) - 1):
        order[starting_numbers[i]] = i + 1


def next() -> int:
    if numbers[-1] in order:
        number = len(numbers) - order[numbers[-1]]
    else:
        number = 0
    order[numbers[-1]] = len(numbers)
    numbers.append(number)
    return number


def play_game(iterations: int):
    for i in range(iterations - len(numbers)):
        next()


if __name__ == '__main__':
    with open('input.txt') as data:
        starting_numbers = [int(line) for line in data.read().split(',')]
        seed(starting_numbers)
        play_game(2020)
        print(numbers[-1])
