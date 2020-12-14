import numpy
def arrival_time_time_for_bus(arrival_time: int, bus):
    time = bus
    while time <= arrival_time:
        time += bus
    return time


def calculate_earliest_departure(arrival_time: int, buses: list) -> dict:
    running_busses = buses.copy()
    while 'x' in running_busses:
        running_busses.remove('x')

    times = [arrival_time_time_for_bus(arrival_time, int(bus)) for bus in running_busses]
    best_time = min(times)
    return {running_busses[times.index(best_time)]: best_time}


def solve(bus: dict, arrival_time: int) -> int:
    bus_id = list(bus.keys())[0]
    time_to_wait = bus[bus_id] - arrival_time
    return int(bus_id) * time_to_wait


def earliest_subsequent_timestamp(busses: list) -> int:
    first_bus = int(busses[0])
    timestamp = first_bus

    rate = int(busses[0])
    timestamp = rate
    busses_to_check = []
    for bus in busses:
        busses_to_check.append(bus)
        while not is_subsequent(busses_to_check, timestamp):
            timestamp += rate
        rate = 1
        for bus in busses_to_check:
            if bus != 'x':
                rate = rate * int(bus)
    return timestamp


def get_max(busses: list) -> str:
    running_busses = busses.copy()
    while 'x' in running_busses:
        running_busses.remove('x')
    return max([int(bus) for bus in running_busses])


def is_subsequent(busses: list, timestamp: int):
    for i in range(0, len(busses)):
        bus = busses[i]
        if bus != 'x':
            if (timestamp + i) % int(bus) != 0:
                return False
    return True


if __name__ == '__main__':
    with open('input.txt') as data:
        arrival_time = int(data.readline())
        busses = data.readline().split(',')
        print(earliest_subsequent_timestamp(busses))
