votes_winner = 10000000000


def loser_gets_next_ev(loser_votes, desired_evs, total_seats):
    seats_loser_has = desired_evs - 1
    seats_winner_has = total_seats - seats_loser_has - 1
    loser_priority_value = loser_votes / (seats_loser_has * (seats_loser_has + 1)) ** 0.5
    winner_priority_value = votes_winner / (seats_winner_has * (seats_winner_has + 1)) ** 0.5
    return loser_priority_value > winner_priority_value


def percentage(winner_votes, loser_votes):
    return float(loser_votes) / (winner_votes + loser_votes)


def bisect_find_percentage(desired_evs, total_seats):
    lower_bound = 0
    upper_bound = votes_winner
    while upper_bound - lower_bound >= 1:
        midpoint = (upper_bound + lower_bound) / 2.0
        if loser_gets_next_ev(midpoint, desired_evs, total_seats):
            upper_bound = midpoint
        else:
            lower_bound = midpoint
    return percentage(votes_winner, (upper_bound + lower_bound) / 2.0)


num_evs = 3
while num_evs <= 55:
    threshold_votes = 1 / (num_evs - 1) * votes_winner
    votes_loser = round(threshold_votes) - 1
    threshold_dict = {1: round(percentage(votes_winner, threshold_votes), 4)}
    desired_seats = 2
    while desired_seats <= num_evs / 2:
        threshold_dict[desired_seats] = round(bisect_find_percentage(desired_seats, num_evs), 4)
        desired_seats += 1
    print(f"With {num_evs} electoral votes:", threshold_dict)
    num_evs += 1
