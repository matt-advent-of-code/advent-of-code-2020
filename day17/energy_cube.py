import numpy
import copy

global cubes
cubes = {}


def init_state(starting_state: str):
    global cubes
    for i, row in enumerate(starting_state.split('\n')):
        for j, column in enumerate(list(row)):
            cubes[i, j, 0] = convert_cube(column)



def cycle():
    global cubes
    cubes_copy = copy.deepcopy(cubes)
    for cube in cubes_copy:
        for neighbor in get_neighbors(*cube):
            cubes[neighbor[0]] = neighbor[1]

    cubes_copy = copy.deepcopy(cubes)
    for cube_index in cubes:
        cube = cubes_copy[cube_index]
        neighbors = get_neighbor_values(*cube_index)
        n = list(get_neighbors(*cube_index))



        if cube == 1 and sum(neighbors) != 2 and sum(neighbors) != 3:
            cubes_copy[cube_index] = 0

        if cube == 0 and sum(neighbors) == 3:
            cubes_copy[cube_index] = 1

    cubes = cubes_copy


def get_neighbors(x: int, y: int, z: int):
    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            for k in range(z - 1, z + 2):
                if (x,y,z) != (i,j,k):
                    yield (i, j, k), get_neighbor(i, j, k)


def get_neighbor_values(x: int, y: int, z: int):
    neighbors = []
    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            for k in range(z - 1, z + 2):
                if (i,j,k) != (x,y,z):
                    neighbors.append(get_neighbor(i, j, k))

    return neighbors


def get_neighbor(x: int, y: int, z: int) -> int:
    try:
        return cubes[x, y, z]
    except Exception:
        return 0


def convert_cube(cube: str) -> int:
    if cube == '#':
        return 1
    else:
        return 0


def get_active() -> int:
    global cubes
    return sum(list(cubes.values()))
    return sum

if __name__ == '__main__':
    with open('input.txt') as data:
        init_state(data.read())
        cycle()
        cycle()
        cycle()
        cycle()
        cycle()
        cycle()
        print(get_active())
