"""Given a number of players generate a table where players play in teams of 2"""


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
    return table

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

#Change the list players to add/remove players
players=['Luca','Guido','Raffa','Claudio'] 

teams = create_teams()
print_teams(teams)

table = create_table(teams)
print_table(table)
      
    