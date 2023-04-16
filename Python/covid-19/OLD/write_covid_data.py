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
                 "(confirmed_country, confirmed_region, confirmed_lat, confirmed_long, confirmed_date, confirmed_number)"
                 "VALUES (%s,%s,%s,%s,%s,%s)"
)

add_deaths = ("INSERT INTO deaths "
                 "(deaths_country, deaths_region, deaths_lat, deaths_long, deaths_date, deaths_number)"
                 "VALUES (%s,%s,%s,%s,%s,%s)"
)

add_recovered = ("INSERT INTO recovered "
                 "(recovered_country, recovered_region, recovered_lat, recovered_long, recovered_date, recovered_number)"
                 "VALUES (%s,%s,%s,%s,%s,%s)"
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

    for my_file, my_qry in zip(fil, qry):
        with open(my_file, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            headers = reader.fieldnames
            #reader.__next__()
            for row in reader:
                my_record = []
                for item in headers[:4]:
                    my_record.append(row[item])
                prev = 0
                for item in headers[4:]:
                    my_record_final = my_record.copy()
                    my_record_final.append(item)
                    #print(item)
                    my_record_final.append(row[item])
                    dt = my_record_final[4].split('/')
                    data = (my_record_final[1], my_record_final[0],my_record_final[2],my_record_final[3],date(int(dt[2]), int(dt[0]), int(dt[1])), my_record_final[5])
                    cursor.execute(my_qry, data)
                    prev = my_record_final[5]
        mydb.commit()

#These are queries to empty the tables before loading fresh data.
delete_tables = []
delete_tables.extend(["delete from confirmed","delete from deaths", "delete from recovered"])

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
