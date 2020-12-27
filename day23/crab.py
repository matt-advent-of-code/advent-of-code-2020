def play(input: str, rounds: int) -> str:
    cups = list(input)
    for _ in range(rounds):
        cups_copy = cups.copy()
        picked_up_cups = [
            cups_copy.pop(1),
            cups_copy.pop(1),
            cups_copy.pop(1)
        ]

        d = destination_cup_index(cups[0], cups_copy)
        cups_copy[d+1:d+1] = picked_up_cups
        current_cup = cups_copy.pop(0)
        cups_copy.append(current_cup)
        cups = cups_copy

    i = cups.index('1')
    return ''.join(cups[i + 1:] + cups[:i])


def destination_cup_index(current_cup: int, cups: list) -> int:
    for i in range(int(current_cup) - 1, 0, -1):
        if str(i) in cups:
            return cups.index(str(i))
    highest_cup = max([int(cup) for cup in cups])
    return cups.index(str(highest_cup))


if __name__ == '__main__':
    print(play('467528193', 100))