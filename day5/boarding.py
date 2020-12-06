FRONT = 'F'
LEFT = 'L'


def calculate_row_range(section: str, seat_range: tuple) -> tuple:
    return __calculate_seat_range(section, seat_range, FRONT)


def calculate_column_range(section: str, seat_range: tuple) -> tuple:
    return __calculate_seat_range(section, seat_range, LEFT)


def calculate_row(boarding_pass_sections: str, seat_range) -> int:
    for section in boarding_pass_sections:
        seat_range = calculate_row_range(section, seat_range)
    assert seat_range[0] == seat_range[1]
    return seat_range[0]


def calculate_column(boarding_pass_sections: str, seat_range) -> int:
    for section in boarding_pass_sections:
        seat_range = calculate_column_range(section, seat_range)
    assert seat_range[0] == seat_range[1]
    return seat_range[0]


def calculate_seat_id(boarding_pass: str) -> int:
    row, column = calculate_seat(boarding_pass)
    return row * 8 + column


def calculate_seat(boarding_pass: str) -> tuple:
    row = calculate_row(boarding_pass[:7], (0, 127))
    column = calculate_column(boarding_pass[7:], (0, 7))
    return row, column


def __calculate_seat_range(section: str, seat_range: tuple, front_identifier: str) -> tuple:
    if section == front_identifier:
        return seat_range[0], seat_range[1] - (int((seat_range[1] - seat_range[0]) / 2) + 1)
    else:
        return seat_range[1] - int((seat_range[1] - seat_range[0]) / 2), seat_range[1]


if __name__ == '__main__':
    with open('input.txt') as data:
        boarding_passes = data.readlines()
        seat_ids = [calculate_seat_id(boarding_pass) for boarding_pass in boarding_passes]
        possible_seat_ids = []
        for row in range(1,126):
            for column in range(0,7):
                possible_seat_ids.append(row * 8 + column)

        for seat in possible_seat_ids:
            if seat + 1 in seat_ids and seat -1 in seat_ids and seat not in seat_ids:
                print(seat)
