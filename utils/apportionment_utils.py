def set_next_priority_value(state, priority_values, seats, populations):
    priority_values[state] = populations[state] / (seats[state] * (seats[state] + 1)) ** 0.5
    return priority_values


def apportion(populations, num_seats):
    seats = {}
    priority_values = {}
    populations = populations.copy()
    if "DC" in populations:
        del populations["DC"]

    assert num_seats >= len(populations), f"{num_seats}, {len(populations)}"

    for state in populations.keys():
        seats[state] = 1

    for state in populations.keys():
        set_next_priority_value(state, priority_values, seats, populations)

    while sum(seats.values()) < num_seats:
        state = max(priority_values.keys(), key=lambda x: priority_values[x])
        seats[state] += 1
        set_next_priority_value(state, priority_values, seats, populations)

    return seats


def determine_evs(populations, num_house_seats):
    apportionment_results = apportion(populations, num_house_seats)
    evs = {k: v + 2 for k, v in apportionment_results.items()}
    evs["DC"] = 3
    return evs
