#TODO: in this state it does not work properly and line 73 might raise a IndexError exception (see the debug_example_study.txt file).
#One possible change: use the player to select the first team instead of the second one.

"""Given a number of players generate a table where players play in teams of 2"""

from random import shuffle
from collections import Counter
from collections import OrderedDict

"""fuction create_teams creates teams of 2 players based on the players list"""
def create_teams():
    teams=[]
    cnt=0
    for x in players:
        cnt+=1
        for y in players[cnt:]:
            if x != y:
                team = [x,y]
                teams.append(team)
    return teams

"""fuction create_table creates the table for the tournament based on the list of teams"""
def create_table(teams):
    #shuffle(teams)
    table=[]
    cnt=0
    for x in teams:
        cnt+=1
        for y in teams[cnt:]:
          team1 = set(x)
          team2 = set(y)
          #The same player can not play in two teams in a given match
          #therefore I intersect the 2 sets and create a match only whether
          #the intersection is empty
          if len((team1 & team2)) == 0:
              table.append([x,y])
    shuffle(table)
    return table
"""
function create_short_table is creating a tournament with a lower number of matches.
The principle is that each team plays only once.
This version of this function DOES NOT WORK. I have to re-write it.
In summary, while I build the table, I must look at the players who have been assigned to the lower amount of matches so far and
use those players in the next match.
"""
def create_short_table(teams):
	f = open('debug.txt', 'w+')
	#shuffle(teams)
	f.write('Starting teams: ' + str(teams) + '\n')
	short_table=[]
	x = teams[0]
	while teams != []:
		team1 = set(x)
		f.write('team1: ' + str(team1) + '\n')
		ranking = count_players(short_table) #Now I have an ordered dictionary; the first element is the player with the smaller number of matches.
		f.write('Ranking: ' + str(ranking) + '\n')
		try:
			player = list(ranking.keys())[0] #Checking whether the dictionary is empty (that's the case at the beginning).
			f.write('Player: ' + str(player) + '\n')
		except IndexError:
			f.write('Exception :')
			for y in teams[1:]:
				f.write('y in exception: ' + str(y) + '\n')
				if len((set(y) & team1)) == 0:
					short_table.append([x,y])
					teams.remove(x)	
					teams.remove(y)	
					break
		else:
			cnt = 0
			y = find_team2(teams, player, team1) # y might be [] in case player is part of the team1.
			if y == []:
				for k in ranking:
					player = str(k)
					y = find_team2(teams, player, team1)
					if y != []:
						break
			short_table.append([x,y])
			teams.remove(y)
			teams.remove(x)
		
		f.write('short table: ' + str(short_table) +'\n')
		f.write('teams: ' + str(teams) +'\n')
		
		ranking = count_players(short_table)
		f.write('Ranking: ' + str(ranking) + '\n')
		player1 = list(ranking.keys())[0]	
		player2 = list(ranking.keys())[1]	
		f.write('Player1: ' + str(player1) +'\n')
		f.write('Player2: ' + str(player2) +'\n')
		x = find_team1(teams, str(player1), str(player2), ranking, f)		
		f.write('Find Team1: ' + str(x) +'\n')
			

	f.close()
	return(short_table)

"""function print_teams is used just to print the teams in a better format"""
def print_teams(teams):
    print('**** Teams ****\n')
    for x in teams:
        print(x)
        #print('\n')
    print('\n')


"""function print_table is used just to print the table in a better format"""
def print_table(table):
    print('**** Table ****\n')
    print('Total of ' + str(len(table)) + ' Matches')
    print('\n')
    for x in table:
        print(repr(x[0])+ ' vs ' + repr(x[1]))
    print('\n')

def generate_file(table):
	f = open('partite.csv', 'w+')
	for x in table:
		for y in range(0,2):
			f.write(str(x[y][0]))
			f.write('-')
			f.write(str(x[y][1]))
			f.write(',')
		f.write('\n')
	f.close()

"""
Function used to take the matches generated so far and create a list.
Then the list is used to count how many matches each player has been assigned to.
"""
def count_players(table):
	players_matches=[]
	for x in table:
		players_matches.append(x[0][0]) 
		players_matches.append(x[0][1]) 
		players_matches.append(x[1][0]) 
		players_matches.append(x[1][1]) 
	ranking = Counter(players_matches)
	for x in players:
			if x not in ranking:
				ranking[x] = 0
	ranking = OrderedDict(sorted(ranking.items(), key=lambda t: t[1]))
	print(ranking)
	return(ranking)

"""
Used to pick team2 looking at the player with the lowest amount of matches so far.
The function returns a team.
"""
def find_team2(teams, player, current_team):
	res = []
	for x in teams:
		if player in x:
			team2 = set(x)
			if len((current_team & team2)) == 0:
				res = x
				break
	return(res)

"""
TODO: function to pick team1.
In this function I should look first at picking a team where both players have the lowest amount of matches so far, not just one player.
"""
def find_team1(teams, player1, player2, ranking, file):
	res = []
	#First looking for a team with both players.
	for x in teams:
		if (player1 in x) and (player2 in x):
			res = x
			break
	if res == []:
		for k in ranking:
			player2 = str(k)
			for x in teams:
				file.write("In find_team1, " + str(x) + ' ' + player1 + ' ' + player2 + '\n')
				if (player1 in x) and (player2 in x) and (player1 != player2):
					res = x
					break
			if res != []:
				break
	return(res)

#Change the list players to add/remove players
players=['Luca','Guido','Raffa','Claudio', 'Gherra', 'Mauro', 'Marcello', 'Sabba'] 

teams = create_teams()
print_teams(teams)

table = create_table(teams)
print_table(table)

short_table = create_short_table(teams)
print_table(short_table)

count_players(short_table)

generate_file(table)