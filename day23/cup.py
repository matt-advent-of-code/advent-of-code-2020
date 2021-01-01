class Cup:
    def __init__(self, number: int, next=None, previous=None):
        self.number = number
        self.next = next
        self.previous = previous


def play(input: str, rounds: int) -> str:
    cups_list = [Cup(int(cup)) for cup in (list(input))]
    max_cup = max([cup.number for cup in cups_list])
    for i in range(max_cup + 1, 1000000 + 1):
        cups_list.append(Cup(i))

    for i in range(len(cups_list) - 1):
        cups_list[i].next = cups_list[i + 1]
        cups_list[i].previous = cups_list[i - 1]
    cups_list[-1].next = cups_list[0]
    cups_list[-1].previous = cups_list[-2]

    cups = {cup.number: cup for cup in cups_list}
    head = cups_list[0]

    max_cup = max([cup for cup in list(cups.keys())])

    for _ in range(rounds):
        picked_up_cups = pop_next_three_cups(head)

        destination = destination_cup(head, cups, [picked_up_cups.number, picked_up_cups.next.number,
                                                   picked_up_cups.next.next.number], max_cup)
        insert_cup(destination, picked_up_cups)
        head = head.next

    return cups[1].next.number, cups[1].next.next.number


def pop_next_three_cups(cup: Cup) -> Cup:
    cup_to_remove = cup.next

    next_in_line = cup_to_remove.next.next.next
    cup.next = next_in_line
    next_in_line.previous = cup

    cup_to_remove.previous = None
    cup_to_remove.next.next.next = None

    return cup_to_remove


def destination_cup(head: Cup, cups: dict, picked_up_cups: list, max_cup: int) -> int:
    for i in range(head.number - 1, 0, -1):
        if i in cups and i not in picked_up_cups:
            return cups[i]

    for i in range(max_cup, 0, -1):
        if i in cups and i not in picked_up_cups:
            return cups[i]


def insert_cup(destination: Cup, cup_to_insert: Cup):
    next = destination.next
    destination.next = cup_to_insert
    cup_to_insert.previous = destination

    next.previous = cup_to_insert.next.next
    cup_to_insert.next.next.next = next


def get_order(cups: dict) -> str:
    head = cups[1]
    order = ''
    while head.next != cups[1]:
        order += str(head.next.number)
        head = head.next

    return order


def parse(input: str) -> dict:
    cups_list = [Cup(int(cup)) for cup in list(input)]
    for i in range(len(cups_list) - 1):
        cups_list[i].next = cups_list[i + 1]
        cups_list[i].previous = cups_list[i - 1]
    cups_list[-1].next = cups_list[0]
    cups_list[-1].previous = cups_list[-2]

    return {cup.number: cup for cup in cups_list}
    head = cups_list[0]

if __name__ == '__main__':
    cups = play('467528193', 10000000)
    print(cups[0] * cups[1])
