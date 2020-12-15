import re

global mask
mask = ''
mem = {}


def put(key, value: int):
    binary_value = '{0:036b}'.format(key)
    keys = apply_mask(binary_value)
    for key in keys:
        key = int(key, 2)
        mem[key] = value


def get(key) -> int:
    return mem[key]


def apply_mask(value: str) -> list:
    keys = ['']
    for i, character in enumerate(list(mask)):
        if character == 'X':
            new_keys = []
            for key in keys:
                new_keys.append(key + '0')
                new_keys.append(key + '1')
            keys = new_keys

        if character == '1':
            keys = [key + '1' for key in keys]
        if character == '0':
            keys = [key + value[i] for key in keys]

    return keys


def mask_index(character: str, index: int) -> str:
    if list(mask)[index] == 'X':
        return character
    else:
        return list(mask)[index]


def initialize(input: str):
    for instruction in input.splitlines():
        if instruction.startswith('mask'):
            global mask
            mask = instruction.split('=')[1].strip()
        else:
            results = re.search(r'mem\[(.*)\] = (.*)', instruction)
            key = results.group(1)
            value = results.group(2)
            put(int(key), int(value))


if __name__ == '__main__':
    with open('input.txt') as data:
        initialize(data.read())
        print(sum(mem.values()))
