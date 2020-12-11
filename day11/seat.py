import copy


def parse(data: str) -> list:
    for row in data.splitlines():
        print(row)

    return [list(row) for row in data.splitlines()]


def next_round(seats: list) -> list:
    seats_copy = copy.deepcopy(seats)
    for i in range(len(seats)):
        for j in range(len(seats[i])):
            rule = get_rule(seats[i][j])
            new_state = rule.apply(seats, i, j)
            seats_copy[i][j] = new_state

    return seats_copy


def to_string(seats: list) -> str:
    seat_string = ''
    for row in seats:
        for i in row:
            seat_string += i
        seat_string += '\n'

    return seat_string[:-1]


class SeatRule:
    def apply(self, seats: list, i: int, j: int) -> str:
        return '.'


class EmptySeatRule(SeatRule):
    def apply(self, seats: list, i: int, j: int) -> str:
        visible_seats = find_visible_seats(seats, i, j)
        if not '#' in visible_seats:
            return '#'
        else:
            return 'L'


class FilledSeatRule(SeatRule):
    def apply(self, seats: list, i: int, j: int) -> str:
        visible_seats = find_visible_seats(seats, i, j)
        if visible_seats.count('#') >= 5:
            return 'L'
        else:
            return '#'


def get_rule(item: str) -> SeatRule:
    if item == 'L':
        return EmptySeatRule()
    elif item == '#':
        return FilledSeatRule()
    else:
        return SeatRule()


def get_adjacent_seats(seats: list, i: int, j: int) -> list:
    adjacent_seats = []
    if (i - 1) >= 0:
        if (j - 1) >= 0:
            adjacent_seats.append(seats[i - 1][j - 1])
        adjacent_seats.append(seats[i - 1][j])
        if (j + 1) < len(seats[i - 1]):
            adjacent_seats.append(seats[i - 1][j + 1])

    if (j - 1) >= 0:
        adjacent_seats.append(seats[i][j - 1])
    if (j + 1) < len(seats[i]):
        adjacent_seats.append(seats[i][j + 1])

    if (i + 1) < len(seats):
        if (j - 1) >= 0:
            adjacent_seats.append(seats[i + 1][j - 1])
        adjacent_seats.append(seats[i + 1][j])

        if (j + 1) < len(seats[i + 1]):
            adjacent_seats.append(seats[i + 1][j + 1])

    return adjacent_seats


def find_visible_seats(seats: list, i: int, j: int) -> list:
    return [
        find_upper_left_seat(seats, i, j),
        find_left_seat(seats, i, j),
        find_lower_left_seat(seats, i, j),
        find_lower_seat(seats, i, j),
        find_lower_right_seat(seats, i, j),
        find_right_seat(seats, i, j),
        find_upper_right_seat(seats, i, j),
        find_upper_seat(seats, i, j)
    ]


def find_upper_left_seat(seats: list, i: int, j: int) -> str:

    if i == 0 or j == 0:
        return '.'
    i = i - 1
    j = j - 1
    while i > 0 and j > 0:
        if seats[i][j] == '#' or seats[i][j] == 'L':
            return seats[i][j]
        i = i - 1
        j = j - 1
    return seats[i][j]


def find_left_seat(seats: list, i: int, j: int) -> str:
    if j == 0:
        return '.'
    j = j - 1
    while j > 0:
        if seats[i][j] == '#' or seats[i][j] == 'L':
            return seats[i][j]
        j = j - 1
    return seats[i][j]


def find_lower_left_seat(seats: list, i: int, j: int) -> str:
    if i == (len(seats) - 1) or j == 0:
        return '.'
    j = j - 1
    i = i + 1
    while i < (len(seats) - 1) and j > 0:
        if seats[i][j] == '#' or seats[i][j] == 'L':
            return seats[i][j]
        j = j - 1
        i = i + 1
    return seats[i][j]


def find_lower_seat(seats: list, i: int, j: int) -> str:
    if i == (len(seats) - 1):
        return '.'
    i = i + 1

    while i < (len(seats) - 1):
        if seats[i][j] == '#' or seats[i][j] == 'L':
            return seats[i][j]
        i = i + 1
    return seats[i][j]


def find_lower_right_seat(seats: list, i: int, j: int) -> str:
    if i == (len(seats) - 1) or j == (len(seats[i]) - 1):
        return '.'
    j = j + 1
    i = i + 1

    while i < (len(seats) - 1) and j < (len(seats[i]) - 1):
        if seats[i][j] == '#' or seats[i][j] == 'L':
            return seats[i][j]
        j = j + 1
        i = i + 1
    return seats[i][j]


def find_right_seat(seats: list, i: int, j: int) -> str:
    if j == (len(seats[i]) - 1):
        return '.'
    j = j + 1

    while j < (len(seats[i]) - 1):
        if seats[i][j] == '#' or seats[i][j] == 'L':
            return seats[i][j]
        j = j + 1
    return seats[i][j]


def find_upper_right_seat(seats: list, i: int, j: int) -> str:
    if i == 0 or j == (len(seats[i]) - 1):
        return '.'
    j = j + 1
    i = i - 1

    while i > 0 and j < (len(seats[i]) - 1):
        if seats[i][j] == '#' or seats[i][j] == 'L':
            return seats[i][j]
        j = j + 1
        i = i - 1
    return seats[i][j]


def find_upper_seat(seats: list, i: int, j: int) -> str:
    if i == 0:
        return '.'
    i = i - 1
    while i > 0:
        if seats[i][j] == '#' or seats[i][j] == 'L':
            return seats[i][j]
        i = i - 1
    return seats[i][j]


def run(data: str) -> list:
    seats = parse(data)
    rounds = 1
    new_seats = next_round(seats)
    print(to_string(new_seats))
    print('\n')
    while new_seats != seats:
        seats = new_seats
        new_seats = next_round(seats)
        print(to_string(new_seats))
        print('\n')

    return new_seats


if __name__ == '__main__':
    with open('input.txt') as data:
        seats = run(data.read())
        count = 0
        for i in seats:
            for j in i:
                if j == '#':
                    count += 1
        print(count)
