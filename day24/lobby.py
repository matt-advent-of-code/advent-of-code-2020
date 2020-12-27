import re
def flip(layout: str) -> int:
    black_tiles = []
    for tile in layout.split('\n'):
        start = (0,0)
        location = start
        moves = re.findall(r'(e|se|sw|w|nw|ne)', tile)
        for move in moves:
            if move == 'e':
                location = location[0], location[1] - 1
            elif move == 'se':
                location = location[0] - 1, location[1]
            elif move == 'sw':
                location = location[0] - 1, location[1] + 1
            elif move == 'w':
                location = location[0], location[1] + 1
            elif move == 'nw':
                location = location[0] + 1, location[1]
            elif move == 'ne':
                location = location[0] + 1, location[1] - 1
            else:
                raise Exception

        if location in black_tiles:
            black_tiles.remove(location)
        else:
            black_tiles.append(location)

    return len(black_tiles)


if __name__ == '__main__':
    with open('input.txt') as data:
        print(flip(data.read()))
