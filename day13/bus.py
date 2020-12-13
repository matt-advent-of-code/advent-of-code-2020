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


if __name__ == '__main__':
    with open('input.txt') as data:
        arrival_time = int(data.readline())
        busses = data.readline().split(',')
        best_bus = calculate_earliest_departure(arrival_time, busses)
        print(solve(best_bus, arrival_time))
