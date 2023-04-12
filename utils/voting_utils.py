from utils.apportionment_utils import determine_evs


def allocate(seats, vote_dict, vote_floor):
    threshold_dict = vote_dict.copy()
    while len(threshold_dict) > seats:
        min_votes = min(threshold_dict.keys(), key=lambda x: threshold_dict[x])
        del threshold_dict[min_votes]
    total_votes_for_threshold = sum(threshold_dict.values())
    vote_floor_votes = vote_floor / 100 * total_votes_for_threshold
    threshold_votes = min(total_votes_for_threshold / seats, max(threshold_dict.values()))
    eligible_vote_dict = {k: v for k, v in threshold_dict.items() if v >= threshold_votes and v >= vote_floor_votes}
    ev_dict = {k: 1 for k in eligible_vote_dict.keys()}
    remaining_seats = seats - sum(ev_dict.values())
    priority_dict = {votes_party: votes / (ev_dict[votes_party] * (ev_dict[votes_party] + 1)) ** 0.5
                     for votes_party, votes in eligible_vote_dict.items()}

    while remaining_seats > 0:
        remaining_seats -= 1
        party = max(priority_dict.keys(), key=lambda x: priority_dict[x])
        ev_dict[party] += 1
        priority_dict[party] = eligible_vote_dict[party] / (ev_dict[party] * (ev_dict[party] + 1)) ** 0.5

    assert sum(ev_dict.values()) == seats

    return ev_dict


def determine_winner(results_dict):
    if any(v > sum(results_dict.values()) / 2 for k, v in results_dict.items()):
        return max(results_dict.keys(), key=lambda x: results_dict[x])
    return "No candidate"


def measure_election(vote_dict, ev_dict, vote_floor):
    states = list(set(ev_dict.keys()).union(set(vote_dict.keys())))
    states = sorted([s for s in states if s in ev_dict and s in vote_dict])
    detailed_results = {}
    total_results = {}

    for state in states:
        state_allocation = allocate(ev_dict[state], vote_dict[state], vote_floor)
        for party, evs in state_allocation.items():
            if party not in total_results:
                total_results[party] = 0
            total_results[party] += evs
        detailed_results[state] = state_allocation

    return total_results, detailed_results


def print_detailed_election_results_analysis(description, populations, num_seats, election_results, vote_floor=0):
    print_detailed_election_results_analysis_with_custom_ev_dict(
        description,
        determine_evs(populations, num_seats),
        election_results,
        vote_floor,
    )


def print_detailed_election_results_analysis_with_custom_ev_dict(description, ev_dict, election_results, vote_floor=0):
    results, detailed_results = measure_election(election_results, ev_dict, vote_floor)
    print(description, results, sum(results.values()) / 2, f"{determine_winner(results)} wins")
    print(detailed_results)


def print_house_size_election_results_analysis(populations, election_results, vote_floor=0):
    seats = 50
    max_seats = 435
    previous_winner = None
    while seats <= max_seats:
        ev_dict = determine_evs(populations, seats)
        results, _ = measure_election(election_results, ev_dict, vote_floor)
        winner = determine_winner(results)
        print(f"Proportional EVs with {seats} house seats:", results, f"{winner} wins")
        seats += 1
        if winner != previous_winner:
            previous_winner = winner
            max_seats = max(max_seats, seats * 1.5)

    max_evs_apportionment = determine_evs(populations, max_seats)
    print(max_evs_apportionment)
    print({k: v for k, v in max_evs_apportionment.items() if v >= 100})
    print(round(96.0 / max(max_evs_apportionment.values()), 2) - 0.01)
