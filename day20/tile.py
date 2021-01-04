import re
import numpy
import math


class Tile:
    def __init__(self):
        id = None
        content = [[]]

    def __eq__(self, other):
        return self.id == other.id and self.content == other.content


def rotate(original: list) -> list:
    return [list(r) for r in zip(*original[::-1])]


def remove_border(tile_with_border: list) -> list:
    return [row[1:-1] for row in tile_with_border[1:-1]]


def is_top_match(tile1: list, tile2: list) -> bool:
    if len(tile1[0]) == len(tile2[-1]):
        for i in range(len(tile1)):
            if tile1[0][i] != tile2[-1][i]:
                return False
        return True
    return False


def is_bottom_match(tile1: list, tile2: list) -> bool:
    if len(tile1[-1]) == len(tile2[0]):
        for i in range(len(tile1)):
            if tile1[-1][i] != tile2[0][i]:
                return False
        return True
    return False


def is_left_match(tile1: list, tile2: list) -> bool:
    if len(tile1) == len(tile2):
        for i in range(len(tile1)):
            if tile1[i][0] != tile2[i][-1]:
                return False
        return True
    return False


def is_right_match(tile1: list, tile2: list) -> bool:
    if len(tile1) == len(tile2):
        for i in range(len(tile1)):
            if tile1[i][-1] != tile2[i][0]:
                return False
        return True
    return False


def match_with_flip_and_rotate(tile1: Tile, tile2: Tile, match_function) -> bool:
    content = tile2.content
    for _ in range(4):
        if match_function(tile1.content, content):
            tile2.content = content
            return True
        content = numpy.flipud(content)
        if match_function(tile1.content, content):
            tile2.content = content
            return True
        content = numpy.flipud(content)
        content = numpy.fliplr(content)
        if match_function(tile1.content, content):
            tile2.content = content
            return True
        content = numpy.fliplr(content)
        content = rotate(content)
    return False


def right_match(tile1: Tile, tile2: Tile) -> bool:
    return match_with_flip_and_rotate(tile1, tile2, is_right_match)


def top_match(tile1: Tile, tile2: Tile) -> bool:
    return match_with_flip_and_rotate(tile1, tile2, is_top_match)


def bottom_match(tile1: Tile, tile2: Tile) -> bool:
    return match_with_flip_and_rotate(tile1, tile2, is_bottom_match)


def left_match(tile1: Tile, tile2: Tile) -> bool:
    return match_with_flip_and_rotate(tile1, tile2, is_left_match)


def is_match(tile1: Tile, tile2: Tile) -> bool:
    return left_match(tile1, tile2) or right_match(tile1, tile2) or top_match(tile1, tile2) or bottom_match(tile1,
                                                                                                            tile2)


def parse(input: str) -> list:
    parsed = []
    for tile in input.split('\n\n'):
        lines = tile.split('\n')
        id = int(re.findall(r'\d+', lines[0])[0])
        content = [list(row) for row in lines[1:]]
        tile = Tile()
        tile.id = id
        tile.content = content
        parsed.append(tile)

    return parsed


def is_tile_in_list(tile: Tile, tiles: list) -> bool:
    for tile_to_check in tiles:
        if tile.id == tile_to_check.id:
            return True
    return False


def find_corners(tiles: list) -> list:
    corners = []
    for tile in tiles:
        matches = 0
        for tile_to_check in tiles:
            if tile.id != tile_to_check.id:
                if is_match(tile, tile_to_check):
                    matches += 1
        if matches == 2:
            corners.append(tile)
    assert len(corners) == 4
    return corners


def find_side_tiles(tiles: list) -> list:
    sides = []
    for tile in tiles:
        matches = 0
        for tile_to_check in tiles:
            if tile.id != tile_to_check.id:
                if is_match(tile, tile_to_check):
                    matches += 1
        if matches == 3:
            sides.append(tile)

    return sides


def set_left_corner(corner: Tile, sides: list):
    while not is_left_corner_set(corner, sides):
        corner.content = rotate(corner.content)


def is_left_corner_set(corner: Tile, sides: list):
    for side in sides:
        if top_match(corner, side) or left_match(corner, side):
            return False
    return True


def recontruct(input: str) -> list:
    print('starting parse')
    tiles = parse(input)
    print('parsed')
    side_length = int(math.sqrt(len(tiles)))
    corner_tiles = find_corners(tiles)
    print('corners found')
    side_tiles = find_side_tiles(tiles)
    print('sides found')

    print('setting left corner')
    set_left_corner(corner_tiles[0], side_tiles)
    print('left corner has been set')
    tiles = [tile for tile in tiles if tile not in corner_tiles and tile not in side_tiles]
    reconstructed_tiles = [
        [corner_tiles[0]]
    ]
    corner_tiles.remove(corner_tiles[0])
    for i in range(1, side_length - 1):
        tile_to_match = reconstructed_tiles[0][i - 1]
        for tile in side_tiles:
            if right_match(tile_to_match, tile):
                reconstructed_tiles[0].append(tile)
                side_tiles.remove(tile)

    for corner_tile in corner_tiles:
        if right_match(reconstructed_tiles[0][-1], corner_tile):
            reconstructed_tiles[0].append(corner_tile)
            corner_tiles.remove(corner_tile)

    for i in range(1, side_length - 1):
        for side_tile in side_tiles:
            if bottom_match(reconstructed_tiles[i - 1][0], side_tile):
                reconstructed_tiles.append([side_tile])
                side_tiles.remove(side_tile)

        for j in range(1, side_length - 1):
            tile_to_left = reconstructed_tiles[i][j - 1]
            tile_above = reconstructed_tiles[i - 1][j]
            for tile in tiles:
                if right_match(tile_to_left, tile) and bottom_match(tile_above, tile):
                    reconstructed_tiles[i].append(tile)
                    tiles.remove(tile)

        tile_to_left = reconstructed_tiles[-1][-1]
        tile_above = reconstructed_tiles[-2][-1]
        for side_tile in side_tiles:
            if right_match(tile_to_left, side_tile) and bottom_match(tile_above, side_tile):
                reconstructed_tiles[i].append(side_tile)
                side_tiles.remove(side_tile)

    tile_above = reconstructed_tiles[-1][0]
    for corner_tile in corner_tiles:
        if bottom_match(tile_above, corner_tile):
            reconstructed_tiles.append([corner_tile])
            corner_tiles.remove(corner_tile)

    for i in range(1, side_length - 1):
        for side_tile in side_tiles:
            tile_to_match = reconstructed_tiles[-1][i - 1]
            if right_match(tile_to_match, side_tile):
                reconstructed_tiles[-1].append(side_tile)
                side_tiles.remove(side_tile)

    tile_to_left = reconstructed_tiles[-1][-1]
    tile_above = reconstructed_tiles[-2][-1]
    for corner_tile in corner_tiles:
        if right_match(tile_to_left, corner_tile) and bottom_match(tile_above, corner_tile):
            reconstructed_tiles[-1].append(corner_tile)
            corner_tiles.remove(corner_tile)

    assert len(tiles) == 0
    assert len(corner_tiles) == 0
    assert len(side_tiles) == 0

    for i in range(len(reconstructed_tiles)):
        for j in range(len(reconstructed_tiles[i])):
            reconstructed_tiles[i][j] = remove_border(reconstructed_tiles[i][j].content)


    rows = []
    for row in reconstructed_tiles:
        rows.append(
            numpy.concatenate(row, axis=1).tolist()
        )
    return numpy.concatenate(rows, axis=0).tolist()

def count_sea_monsters(tiles: list) -> int:
    sea_monster_count = 0
    while sea_monster_count == 0:
        for i in range(len(tiles) - 2):
            for j in range(len(tiles[i]) - 18):
                if is_sea_monster(i, j, tiles):
                    sea_monster_count += 1
        if sea_monster_count > 0:
            return sea_monster_count
        tiles = numpy.fliplr(tiles)
        for i in range(len(tiles) - 2):
            for j in range(len(tiles[i]) - 18):
                if is_sea_monster(i, j, tiles):
                    sea_monster_count += 1
        if sea_monster_count > 0:
            return sea_monster_count
        tiles = numpy.fliplr(tiles)
        tiles = numpy.flipud(tiles)
        for i in range(len(tiles) - 2):
            for j in range(len(tiles[i]) - 18):
                if is_sea_monster(i, j, tiles):
                    sea_monster_count += 1
        tiles = numpy.flipud(tiles)
        tiles = rotate(tiles)
        print('rotated')

    return sea_monster_count

def is_sea_monster(i: int, j: int, tiles: list) -> bool:
    """
                      #
    #    ##    ##    ###
     #  #  #  #  #  #
    """
    return tiles[i][j + 18] == '#'\
           and tiles[i + 1][j] == '#' and tiles[i + 1][j + 5] == '#' and tiles[i + 1][j + 6] == '#' and tiles[i + 1][j + 11] == '#' and tiles[i + 1][j + 12] == '#' and tiles[i + 1][j + 17] == '#' and tiles[i + 1][j + 18] == '#' and tiles[i + 1][j + 19] == '#'\
           and tiles[i + 2][j + 1] == '#' and tiles[i + 2][j + 4] == '#' and tiles[i + 2][j + 7] == '#' and tiles[i + 2][j + 10] == '#' and tiles[i + 2][j + 13] == '#' and tiles[i + 2][j + 16] == '#'


def calc_roughness(input: str) -> int:
    print('starting recontruct')
    tiles = recontruct(input)
    print('completed reconstruct')
    sea_monsters = count_sea_monsters(tiles)

    return sum(row.count('#') for row in tiles) - (sea_monsters * 15)




if __name__ == '__main__':
    with open('input.txt') as data:
        print(calc_roughness(data.read()))