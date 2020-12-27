import re


def seed(layout: str) -> set:
    black_tiles = set()
    for tile in layout.split('\n'):
        start = (0, 0)
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
            black_tiles.add(location)

    return black_tiles


def flip(black_tiles: set, days: int) -> int:
    for _ in range(days):
        flip_one_day(black_tiles)

    return len(black_tiles)


def flip_one_day(black_tiles: set):
    black_tiles_copy = black_tiles.copy()
    for black_tile in black_tiles_copy:
        neighbors = get_neighbors(black_tile)
        black_neighbors = 0
        for neighbor in neighbors:
            if neighbor in black_tiles_copy:
                black_neighbors += 1
        if black_neighbors == 0 or black_neighbors > 2:
            black_tiles.remove(black_tile)

    for black_tile in black_tiles_copy:
        neighbors = get_neighbors(black_tile)
        for neighbor in neighbors:
            if neighbor not in black_tiles_copy:
                while_tile = neighbor
                white_tile_neighbors = get_neighbors(while_tile)
                black_neighbors = 0
                for white_tile_neighbor in white_tile_neighbors:
                    if white_tile_neighbor in black_tiles_copy:
                        black_neighbors += 1
                if black_neighbors == 2:
                    black_tiles.add(while_tile)


def get_neighbors(tile: tuple) -> list:
    return [
        (tile[0], tile[1] - 1),
        (tile[0] - 1, tile[1]),
        (tile[0] - 1, tile[1] + 1),
        (tile[0], tile[1] + 1),
        (tile[0] + 1, tile[1]),
        (tile[0] + 1, tile[1] - 1)
    ]


if __name__ == '__main__':
    with open('input.txt') as data:
        black_tiles = seed(data.read())
        print(flip(black_tiles, 100))
