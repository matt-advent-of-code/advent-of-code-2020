def parse(input: str) -> dict:
    data = input.split("\n\n")
    fields_data = parse_field_data(data[0])
    ticket_data = parse_ticket(data[1])
    nearby_ticket_data = parse_nearby_ticket_data(data[2])
    return {'fields': fields_data, 'ticket': ticket_data, 'nearby_tickets': nearby_ticket_data}


def parse_field_data(data: str) -> dict:
    field_data = {}
    for field in data.split('\n'):
        key = field.split(":")[0]
        value = field.split(":")[1].strip().split(" or ")
        field_data[key] = value
    return field_data


def parse_ticket(data: str) -> list:
    return [int(field) for field in data.split(':')[1].strip().split(',')]


def parse_nearby_ticket_data(data: str) -> list:
    return [[int(field) for field in ticket.split(',')] for ticket in data.split(':')[1].strip().split('\n')]


def find_invalid_fields(ticket: list, fields: dict) -> list:
    valid_fields = []
    for ticket_field in ticket:
        for field in fields:
            for value_range in fields[field]:
                lower = int(value_range.split('-')[0])
                upper = int(value_range.split('-')[1])
                if ticket_field in range(lower, upper + 1):
                    valid_fields.append(ticket_field)
    return list(filter(lambda field: field not in valid_fields, ticket))


def calculate_error_rate(input: str) -> int:
    error_rate = 0
    data = parse(input)
    invalid_fields = [find_invalid_fields(ticket, data['fields']) for ticket in data['nearby_tickets']]
    for ticket_fields in invalid_fields:
        for field in ticket_fields:
            error_rate += field
    return error_rate


def translate(input: str) -> dict:
    data = parse(input)
    possible_fields = {}
    for key in data['fields']:
        possible_fields[key] = list(range(len(data['ticket'])))

    nearby_tickets = filter_invalid_tickets(data['nearby_tickets'], data['fields'])
    for ticket in nearby_tickets:
        for i, ticket_field in enumerate(ticket):
            for field in data['fields']:
                if not is_valid_for_field(ticket_field, data['fields'][field]):
                    if i in possible_fields[field]:
                        possible_fields[field].remove(i)
                        remove_determined_fields(possible_fields)

    remove_determined_fields(possible_fields)
    return {field: data['ticket'][possible_fields[field][0]] for field in possible_fields}


def remove_determined_fields(possible_fields: dict):
    for field in possible_fields:
        if len(possible_fields[field]) == 1:
            for field_to_check in possible_fields:
                if field != field_to_check:
                    if possible_fields[field][0] in possible_fields[field_to_check]:
                        possible_fields[field_to_check].remove(possible_fields[field][0])
                        remove_determined_fields(possible_fields)


def is_valid_for_field(field_value: int, value_ranges: list) -> bool:
    return True in [is_range_valid_for_field(field_value, value_range) for value_range in value_ranges]


def is_range_valid_for_field(field_value: int, value_range: str):
    lower = int(value_range.split('-')[0])
    upper = int(value_range.split('-')[1])
    return field_value in range(lower, upper + 1)


def filter_invalid_tickets(nearby_tickets: list, fields: dict):
    return list(filter(lambda ticket: len(find_invalid_fields(ticket, fields)) == 0, nearby_tickets))


if __name__ == '__main__':
    with open('input.txt') as data:
        ticket = translate(data.read())
        print(ticket['departure location'] * ticket['departure station'] * ticket['departure platform']
              * ticket['departure track'] * ticket['departure date'] * ticket['departure time'])
