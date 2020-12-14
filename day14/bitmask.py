import re
global mask
mask = ''
mem = {}


def put(key, value: int):
    binary_value = '{0:036b}'.format(value)
    masked_value = apply_mask(binary_value)
    value = int(masked_value, 2)
    mem[key] = value


def get(key) -> int:
    return mem[key]


def apply_mask(value: str) -> str:
    return "".join([mask_index(e,i) for i, e in enumerate(list(value))])


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
            results = re.search('mem\[(.*)\] = (.*)', instruction)
            key = results.group(1)
            value = results.group(2)
            put(key, int(value))

if __name__ == '__main__':
    with open('input.txt') as data:
        initialize(data.read())
        print(sum(mem.values()))