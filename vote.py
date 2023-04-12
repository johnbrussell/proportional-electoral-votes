from data.apportionment_data import populations_1990, populations_2010
from data.election_results import president_1992, president_2000, president_2016, president_2020
from utils.voting_utils import print_detailed_election_results_analysis, \
    print_detailed_election_results_analysis_with_custom_ev_dict, \
    print_house_size_election_results_analysis


state_ev_dict_2012_2020 = {
    "Alabama": 9,
    "Alaska": 3,
    "Arizona": 11,
    "Arkansas": 6,
    "California": 55,
    "Colorado": 9,
    "Connecticut": 7,
    "Delaware": 3,
    "DC": 3,
    "Florida": 29,
    "Georgia": 16,
    "Hawaii": 4,
    "Idaho": 4,
    "Illinois": 20,
    "Indiana": 11,
    "Iowa": 6,
    "Kansas": 6,
    "Kentucky": 8,
    "Louisiana": 8,
    "Maine": 2,
    "ME-1": 1,
    "ME-2": 1,
    "Maryland": 10,
    "Massachusetts": 11,
    "Michigan": 16,
    "Minnesota": 10,
    "Mississippi": 6,
    "Missouri": 10,
    "Montana": 3,
    "Nebraska": 2,
    "NE-1": 1,
    "NE-2": 1,
    "NE-3": 1,
    "Nevada": 6,
    "New Hampshire": 4,
    "New Jersey": 14,
    "New Mexico": 5,
    "New York": 29,
    "North Carolina": 15,
    "North Dakota": 3,
    "Ohio": 18,
    "Oklahoma": 7,
    "Oregon": 7,
    "Pennsylvania": 20,
    "Rhode Island": 4,
    "South Carolina": 9,
    "South Dakota": 3,
    "Tennessee": 11,
    "Texas": 38,
    "Utah": 6,
    "Vermont": 3,
    "Virginia": 13,
    "Washington": 12,
    "West Virginia": 5,
    "Wisconsin": 10,
    "Wyoming": 3,
}
assert sum(state_ev_dict_2012_2020.values()) == 538

print_house_size_election_results_analysis(populations_1990, president_1992)

# print_house_size_election_results_analysis(populations_1990, president_2000)

# print_house_size_election_results_analysis(populations_2010, president_2016)

# print_house_size_election_results_analysis(populations_2010, president_2020)

print_detailed_election_results_analysis("1992 proportional EVs:", populations_1990, 435, president_1992)

# print_detailed_election_results_analysis("2000 proportional EVs:", populations_1990, 435, president_2000, 5)

# print_detailed_election_results_analysis_with_custom_ev_dict("2016 proportional EVs:", state_ev_dict_2012_2020,
#                                                              president_2016, 5)

# print_detailed_election_results_analysis("2016 proportional EVs no CD EVs:", populations_2010, 435, president_2016, 5)
# 2016 battlegrounds would have been:
#  Alabama (Ds are three points away from 4th EV)
#  California (Rs are a point ahead of getting an 18th seat and a point behind a 19th)
#  Florida (Ds are less than a point behind winning the state, which would flip an EV)
#  Georgia (Ds are less than half a point ahead of the threshold for the 8th EV)
#  Hawaii (Rs are four points away from winning a second EV)
#  Idaho (Ds are five points away from winning a second EV)
#  Illinois (Rs are 1.5 points away from winning a ninth EV)
#  Indiana (Ds are less than a point away from winning a fifth EV)
#  Iowa (Ds are only 3.5 points ahead of winning their third EV)
#  Kansas (Ds are 2.5 points behind their third EV)
#  Maryland (Rs are only a point ahead of winning their 4th EV)
#  Mississippi (Ds fell half a point behind their third EV)
#  New York (Rs were two points ahead of the 11th EV and 1.5 points behind the 12th)
#  North Carolina (Ds were less than two points away from winning the state and flipping an EV)
#  North Dakota (Ds were three points behind of their first EV)
#  Ohio (Ds were 1.5 points behind their ninth EV)
#  Oklahoma (Ds were five points behind their third EV)
#  South Dakota (Ds were a point away from their first EV)
#  Texas (Ds were less than half a point ahead of their 17th EV)
#  Utah (Three candidates win EVs; Evan McMullin close to a second EV using two-party race priority values)
#  Vermont (Rs a point away from their first EV)
#  West Virginia (Ds a point away from their second EV)

# print_detailed_election_results_analysis("2016 proportional EVs with 573 2010 districts:",
#                                          populations_2010, 573, president_2016)
#
# print_detailed_election_results_analysis("2016 proportional EVs with 653 2010 districts:",
#                                          populations_2010, 653, president_2016)

# print_detailed_election_results_analysis("2020 proportional EVs:", populations_2010, 435, president_2020, 5)
# 2020 battlegrounds would have been:
#  Alabama: Ds less than two points away from a fourth EV
#  Arizona: Rs less than a point away from winning the state and flipping an EV
#  California: Rs less than 0.4 points away from a 20th EV
#  Florida: Ds less than two points ahead of their 14th EV, less than two points behind flipping the state and an EV
#  Hawaii: Rs less than two points behind their second EV
#  Idaho: Ds 2.5 points behind their second EV
#  Illinois: Rs 1 point behind their ninth EV
#  Indiana: Ds less than a point ahead of their fifth EV
#  Kansas: Ds a point ahead of their third EV
#  Maryland: Rs two points behind their fourth EV
#  Massachusetts: Rs a point ahead of their fourth EV
#  Michigan: Rs only two points ahead of their eighth EV
#  Minnesota: Rs only 1.5 points ahead of their fifth EV
#  Mississippi: Ds less than 0.2 points ahead of their third EV
#  New York: Rs only two points ahead of their 11th EV and less than 1.5 behind their 12th
#  North Carolina: Ds less than a point away from flipping the state and an EV
#  North Dakota: Ds less than 1.5 points away from their first EV
#  Ohio: Ds less than 1.5 points away from their ninth EV
#  Oklahoma: Ds less than 2.5 points away from their third EV
#  Pennsylvania: Rs less than 2 points ahead of their 10th EV
#  South Dakota: Ds only three points ahead of their first EV
#  Tennessee: Ds only two points away from their fifth EV
#  Texas: Ds only a point ahead of their 18th EV
#  Utah: Ds less than two points away from their third EV
#  Vermont: Rs only two points away from their first EV
#  West Virginia: Ds only a point ahead of their second EV
