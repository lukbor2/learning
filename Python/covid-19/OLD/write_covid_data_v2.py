# The idea is to have the 3 file names in a list. Then a list with the 3 queries.
# Then pass the 2 lists with files and queries to a function. Then the function iterates on files and queries and writes the db.
# The pre-requisite is the 3 files have the same structure.

# At the end of the process the data to be used for analysis and reporting are going to be in MySQL in the table final_01.
# In the process, some of the ratios are already calculated and are available in the table.

import csv
import mysql.connector
from datetime import date

#These are the test files with some data.
# file_confirmed = '/home/luca/git/COVID-19_world/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Confirmed_copy.csv' # add path to file with confirmed data.
# file_deaths = '/home/luca/git/COVID-19_world/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Deaths_copy.csv' # add path to file with deaths data.
# file_recovered = '/home/luca/git/COVID-19_world/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Recovered_copy.csv' # add path to file with data.

#These are the real files with the data.
file_confirmed = '/home/luca/git/COVID-19_world/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv' # add path to file with confirmed data.
file_deaths = '/home/luca/git/COVID-19_world/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv' # add path to file with deaths data.
file_recovered = '/home/luca/git/COVID-19_world/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv' # add path to file with data.

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
                res = 0
                res_p = 0
                for item in headers[4:]:
                    my_record_final = my_record.copy()
                    my_record_final.append(item)
                    my_record_final.append(row[item])
                    if headers.index(item) >= 5: #For the first date the delta is 0 by definition.
                        res = int(my_record_final[5]) - int(prev) #NOTE: I have to do the cast on prev!!
                    if int(prev) != 0:
                        res_p = res / int(prev)
                    dt = my_record_final[4].split('/')
                    data = (my_record_final[1], my_record_final[0],my_record_final[2],my_record_final[3],date(int(dt[2]), int(dt[0]), int(dt[1])), my_record_final[5],res, res_p)
                    cursor.execute(my_qry, data)
                    prev = my_record_final[5]
        mydb.commit()

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

def update_final_01():
    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      passwd="cacca1971",
      database="covid19",
      buffered=True #I need this param to execute the two queries below.
    )
    cursor_keys = mydb.cursor()
    cursor_data = mydb.cursor()
    cursor = mydb.cursor()
    qry_1 = ("SELECT DISTINCT country_region from current_positive ORDER BY country_region") #This query returns the keys country_region to be used later.
    qry_2 = ("SELECT * from current_positive ORDER BY confirmed_country, confirmed_region, confirmed_date") #This query just returns all records which will be needed anyways.

    add_final = ("INSERT INTO final_01 "
                 "(final_01_country, final_01_region, final_01_date, confirmed_number, deaths_number, recovered_number, current_positive, confirmed_delta, confirmed_delta_p, deaths_delta, deaths_delta_p, recovered_delta, recovered_delta_p, current_positive_delta, current_positive_delta_p)"
                 "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                 )

    cursor_keys.execute(qry_1)
    for row in cursor_keys:
        #print(row[0])
        cursor_data.execute(qry_2) #qry_2 needs to be re-executed to reload the data after every loop.
        prev = 0
        for data in cursor_data:
            if row[0] in data:
                #print(data)
                current_positive_delta_p = 0
                if prev != 0:
                    current_positive_delta_p = data[13]/prev
                #print(data,' ', current_positive_delta_p)
                prev = data[6] #current positive field.
                my_data = list(data[:14])
                #print(my_data)
                my_data.append(current_positive_delta_p)
                cursor.execute(add_final, my_data)
    mydb.commit()

remove_data(delete_tables)
add_data(queries_list, file_names)
update_final_01()
