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
    row = calculate_row(boarding_pass[:7], (0, 127))
    column = calculate_column(boarding_pass[7:], (0, 7))
    return row * 8 + column


def __calculate_seat_range(section: str, seat_range: tuple, front_identifier: str) -> tuple:
    if section == front_identifier:
        return seat_range[0], seat_range[1] - (int((seat_range[1] - seat_range[0]) / 2) + 1)
    else:
        return seat_range[1] - int((seat_range[1] - seat_range[0]) / 2), seat_range[1]


if __name__ == '__main__':
    max_seat_id = 0
    with open('input.txt') as data:
        for boarding_pass in data.readlines():
            seat_id = calculate_seat_id(boarding_pass)
            if seat_id > max_seat_id:
                max_seat_id = seat_id
    print(max_seat_id)
