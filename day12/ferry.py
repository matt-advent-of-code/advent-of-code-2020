class Action:
    def act(self, action: str, ship):
        pass


class NorthAction(Action):
    def act(self, action: str, ship):
        ship.coordinates = (ship.coordinates[0], ship.coordinates[1] + int(action[1:]))


class SouthAction(Action):
    def act(self, action: str, ship):
        ship.coordinates = (ship.coordinates[0], ship.coordinates[1] - int(action[1:]))


class EastAction(Action):
    def act(self, action: str, ship):
        ship.coordinates = (ship.coordinates[0] + int(action[1:]), ship.coordinates[1])


class WestAction(Action):
    def act(self, action: str, ship):
        ship.coordinates = (ship.coordinates[0] - int(action[1:]), ship.coordinates[1])


class TurnRightAction(Action):
    def act(self, action: str, ship):
        direction = Ship.directions[ship.direction]
        degree = int(action[1:])
        degree = simplify_degree(degree)
        new_direction = simplify_degree(direction + degree)
        for key, value in Ship.directions.items():
            if value == new_direction:
                ship.direction = key


def simplify_degree(degree: int):
    return degree - (360 * int(degree / 360))


class TurnLeftAction(TurnRightAction):
    def act(self, action: str, ship):
        degree = simplify_degree(int(action[1:]))
        action = 'R' + str((360 - degree))
        super(TurnLeftAction, self).act(action, ship)


class ForwardDirection(Action):
    def act(self, action: str, ship):
        action = ship.direction + action[1:]
        Ship.get_action(action).act(action, ship)


class Ship:
    directions = {
        'E': 0,
        'S': 90,
        'W': 180,
        'N': 270
    }

    def __init__(self, coordinates: tuple, direction: str):
        self.coordinates = coordinates
        self.direction = direction

    def move(self, action: str):
        Ship.get_action(action).act(action, self)

    @staticmethod
    def get_action(action: str) -> Action:
        if action[0] == 'N':
            return NorthAction()
        elif action[0] == 'S':
            return SouthAction()
        elif action[0] == 'E':
            return EastAction()
        elif action[0] == 'W':
            return WestAction()
        elif action[0] == 'F':
            return ForwardDirection()
        elif action[0] == 'R':
            return TurnRightAction()
        elif action[0] == 'L':
            return TurnLeftAction()
        else:
            raise Exception


if __name__ == '__main__':
    with open('input.txt') as data:
        ship = Ship((0, 0), 'E')
        for direction in data.readlines():
            ship.move(direction)

        manhattan_distance = abs(ship.coordinates[0]) + abs(ship.coordinates[1])
        print(manhattan_distance)