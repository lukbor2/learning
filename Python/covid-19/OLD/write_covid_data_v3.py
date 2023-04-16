# The idea is to have the 3 file names in a list. Then a list with the 3 queries.
# Then pass the 2 lists with files and queries to a function. Then the function iterates on files and queries and writes the db.
# The pre-requisite is the 3 files have the same structure.

import csv
import mysql.connector
from datetime import date

#These are the files with the data.
file_confirmed = '/home/luca/git/COVID-19_world/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Confirmed_copy.csv' # add path to file with confirmed data.
file_deaths = '/home/luca/git/COVID-19_world/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Deaths_copy.csv' # add path to file with deaths data.
file_recovered = '/home/luca/git/COVID-19_world/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Recovered_copy.csv' # add path to file with data.

file_names=[]
file_names.append(file_confirmed)
file_names.append(file_deaths)
file_names.append(file_recovered)

#These are the queries to insert the files into the db.
add_confirmed = ("INSERT INTO confirmed "
                 "(confirmed_country, confirmed_region, confirmed_lat, confirmed_long, confirmed_date, confirmed_number, confirmed_delta, confirmed_delta_p)"
                 "VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
)

add_deaths = ("INSERT INTO deaths "
                 "(deaths_country, deaths_region, deaths_lat, deaths_long, deaths_date, deaths_number, deaths_delta, deaths_delta_p)"
                 "VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
)

add_recovered = ("INSERT INTO recovered "
                 "(recovered_country, recovered_region, recovered_lat, recovered_long, recovered_date, recovered_number, recovered_delta, recovered_delta_p)"
                 "VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
)

queries_list = []
queries_list.append(add_confirmed)
queries_list.append(add_deaths)
queries_list.append(add_recovered)

def add_data(qry, fil):
    #Takes a list of queries and a list of files with data.
    #Reads data from each file and uses the query to insert in the db.

    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      passwd="cacca1971",
      database="covid19"
    )
    cursor = mydb.cursor()

    with open(file_names, newline='') as target:
        pass
    open ()


#These are queries to empty the tables before loading fresh data.
delete_tables = []
delete_tables.extend(["delete from confirmed","delete from deaths", "delete from recovered", "delete from final_01"])

def remove_data(qry):
    # Takes a list of delete queries and executes them.
    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      passwd="cacca1971",
      database="covid19"
    )
    cursor = mydb.cursor()
    for my_qry in qry:
        cursor.execute(my_qry)
        mydb.commit()

remove_data(delete_tables)
add_data(queries_list, file_names)
