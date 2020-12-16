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


if __name__ == '__main__':
    with open('input.txt') as data:
        print(calculate_error_rate(data.read()))