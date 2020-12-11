import copy


def parse(data: str) -> list:
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
        adjacent_seats = get_adjacent_seats(seats, i, j)
        if not '#' in adjacent_seats:
            return '#'
        else:
            return 'L'


class FilledSeatRule(SeatRule):
    def apply(self, seats: list, i: int, j: int) -> str:
        adjacent_seats = get_adjacent_seats(seats, i, j)
        if adjacent_seats.count('#') >= 4:
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