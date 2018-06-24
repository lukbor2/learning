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
	while teams != []:
		x = teams[0]
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
			y = find_team(teams, player, team1)
			while y == []:
				cnt += 1
				player = list(ranking.keys())[cnt]
				y = find_team(teams, player, team1)
			short_table.append([x,y])
			teams.remove(y)
			teams.remove(x)	
					
		f.write('short table: ' + str(short_table) +'\n')
		f.write('teams: ' + str(teams) +'\n')

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

"""finds a team where the player is playing"""
def find_team(teams, player, current_team):
	res = []
	for x in teams:
		if player in x:
			team2 = set(x)
			if len((current_team & team2)) == 0:
				res = x
				break
	return(res)

#Change the list players to add/remove players
players=['Luca','Guido','Raffa','Claudio', 'Gherra', ] 

teams = create_teams()
print_teams(teams)

table = create_table(teams)
print_table(table)

short_table = create_short_table(teams)
print_table(short_table)

count_players(short_table)

generate_file(table)