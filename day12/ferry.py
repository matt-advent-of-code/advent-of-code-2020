class Action:
    def act(self, action: str, ship):
        pass


class NorthAction(Action):
    def act(self, action: str, ship):
        ship.waypoint = (ship.waypoint[0], ship.waypoint[1] + int(action[1:]))


class SouthAction(Action):
    def act(self, action: str, ship):
        ship.waypoint = (ship.waypoint[0], ship.waypoint[1] - int(action[1:]))


class EastAction(Action):
    def act(self, action: str, ship):
        ship.waypoint = (ship.waypoint[0] + int(action[1:]), ship.waypoint[1])


class WestAction(Action):
    def act(self, action: str, ship):
        ship.waypoint = (ship.waypoint[0] - int(action[1:]), ship.waypoint[1])


class TurnRightAction(Action):
    def act(self, action: str, ship):
        for degree in range((int(action[1:])), 0, -90):
            relative_waypoint = calculate_relative_waypoint(ship.waypoint, ship.coordinates)
            rotated_relative_waypoint = (relative_waypoint[1], -1 * relative_waypoint[0])
            ship.waypoint = (ship.coordinates[0] + rotated_relative_waypoint[0], ship.coordinates[1]
                             + rotated_relative_waypoint[1])


def simplify_degree(degree: int):
    return degree - (360 * int(degree / 360))


class TurnLeftAction(TurnRightAction):
    def act(self, action: str, ship):
        degree = simplify_degree(int(action[1:]))
        action = 'R' + str((360 - degree))
        super(TurnLeftAction, self).act(action, ship)


class ForwardDirection(Action):
    def act(self, action: str, ship):
        multiplier = int(action[1:])
        relative_waypoint = calculate_relative_waypoint(ship.waypoint, ship.coordinates)
        x = multiplier * relative_waypoint[0] + ship.coordinates[0]
        y = multiplier * relative_waypoint[1] + ship.coordinates[1]
        ship.coordinates = x, y
        ship.waypoint = ship.coordinates[0] + relative_waypoint[0], ship.coordinates[1] + relative_waypoint[1]


def calculate_relative_waypoint(waypoint: tuple, coordinates: tuple):
    return waypoint[0] - coordinates[0], waypoint[1] - coordinates[1]


class Ship:

    def __init__(self, coordinates: tuple, waypoint: tuple):
        self.coordinates = coordinates
        self.waypoint = waypoint

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
        ship = Ship((0, 0), (10,1))
        for direction in data.readlines():
            ship.move(direction)

        manhattan_distance = abs(ship.coordinates[0]) + abs(ship.coordinates[1])
        print(manhattan_distance)
