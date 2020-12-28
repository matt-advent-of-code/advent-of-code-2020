def crack_loop_size(public_key: int, subject_number: int) -> int:
    loop_size = 0
    value = 1
    while value != public_key:
        value = handshake(value, subject_number)
        loop_size += 1

    return loop_size


def handshake(value: int, subject_number: int) -> int:
    value *= subject_number
    return value % 20201227


def crack_encryption_key(card_public_key: int, door_public_key: int, subject_number: int) -> int:
    card_loop_size = crack_loop_size(card_public_key, subject_number)
    encryption_key = 1
    for _ in range(card_loop_size):
        encryption_key = handshake(encryption_key, door_public_key)

    return encryption_key


if __name__ == '__main__':
    card_public_key = 11404017
    door_public_key = 13768789
    subject_number = 7

    print(crack_encryption_key(card_public_key, door_public_key, subject_number))
