from itertools import combinations

def generate_teams(players):
    teams = []
    for team in combinations(players, 2):
        teams.append(team)
    return teams

def generate_matches(teams):
    matches = []
    for i, team1 in enumerate(teams):
        for j in range(i+1, len(teams)):
            team2 = teams[j]
            if any([player in team1 for player in team2]):
                continue
            match = (team1, team2)
            matches.append(match)
    return matches

def print_list_on_new_line(lst):
    for i, item in enumerate(lst):
        print(i, item)

""" players = ['A', 'B', 'C', 'D', 'E', 'F'] """
players = ['Luca', 'Guido', 'Raffa', 'Claudio', 'Mauro']
teams = generate_teams(players)

print_list_on_new_line(generate_matches(teams))
