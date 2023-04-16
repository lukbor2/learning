# The idea is to have the 3 file names in a list. Then a list with the 3 queries.
# Then pass the 2 lists with files and queries to a function. Then the function iterates on files and queries and writes the db.
# The pre-requisite is the 3 files have the same structure.

# At the end of the process the data to be used for analysis and reporting are going to be in MySQL in the table final_01.
# In the process, some of the ratios are already calculated and are available in the table.

import csv
import mysql.connector
import datetime
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
delete_tables.extend(["delete from confirmed","delete from deaths", "delete from recovered", "delete from final_01", "delete from us_states", "delete from italy"])

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
            #if row[0] in data:
            if row[0] == data[14]:
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

def add_us_states():
    qry = ("INSERT INTO final_01"
           " (final_01_country, final_01_date, final_01_region, confirmed_number, deaths_number) "
           " VALUES (%s,%s,%s,%s,%s)"
           )

    file_us_states = '/home/luca/git/COVID-19_usa/us-states.csv'

    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      passwd="cacca1971",
      database="covid19"
    )
    cursor = mydb.cursor()

    with open(file_us_states, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        headers = reader.fieldnames
        for row in reader:
            my_record = []
            my_record.append('US')
            for item in headers:
                my_record.append(row[item])
            #print(qry)
            #print(data)
            my_record.pop(3)
            cursor.execute(qry, my_record)

    mydb.commit()
    cursor.close()
    mydb.close()
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="cacca1971",
        database="covid19"
    )

    qry_states_list = ("SELECT DISTINCT final_01_region from final_01 WHERE final_01_country = 'US' ORDER BY final_01_region") # This is the list of the states.
    qry_data = ("SELECT * from final_01 WHERE final_01_country = 'US' AND final_01_region = %s ORDER BY final_01_region, final_01_date")
    qry_update = ("UPDATE final_01 "
             "SET confirmed_delta = %s, confirmed_delta_p = %s, deaths_delta = %s, deaths_delta_p = %s "
             "WHERE final_01_country = 'US' AND final_01_region = %s AND final_01_date = %s"
    )

    cursor_states = mydb.cursor(buffered=True)
    cursor_data = mydb.cursor()
    cursor = mydb.cursor()

    cursor_states.execute(qry_states_list)
    for row in cursor_states:
        #print("row is ", row[0])
        cursor_data.execute(qry_data, row)
        records = cursor_data.fetchall()

        for data in records:
            #print(data)
            i = records.index(data)
            if (i+1) < len(records):
                data_next = records[i+1]
                cases_delta = data_next[4]-data[4]
                if data[4] != 0:
                    cases_delta_p = cases_delta / data[4]
                else:
                    cases_delta_p = 0
                deaths_delta = data_next[5]-data[5]
                if data[5] != 0:
                    deaths_delta_p = deaths_delta / data[5]
                else:
                    deaths_delta_p = 0
                #print(data_next, cases_delta)
                parameters = (cases_delta, cases_delta_p, deaths_delta, deaths_delta_p, data_next[2], data_next[3])
                #print(qry_update, parameters)
                cursor.execute(qry_update, parameters)

    mydb.commit()
    mydb.close()

def add_italy_data():
    file_ita = '/home/luca/git/COVID-19_italy/dati-andamento-nazionale/dpc-covid19-ita-andamento-nazionale.csv'
    add_ita = ("UPDATE final_01 "
               "SET hospitalized = %s, in_icu = %s, hospitalized_tot = %s, tested = %s "
               "WHERE final_01_country = 'Italy' AND final_01_date = %s")

    file_names=[]
    file_names.append(file_ita) #I thought I could use the logic below to load multiple files using multiple queries; that's not the case but I did not change the code.

    queries_list = []
    queries_list.append(add_ita) #I thought I could use the logic below to load multiple files using multiple queries; that's not the case but I did not change the code.

    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      passwd="cacca1971",
      database="covid19"
    )
    cursor = mydb.cursor()

    for my_file, my_qry in zip(file_names, queries_list):
        with open(my_file, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            headers = reader.fieldnames
            for row in reader:
                parameters = (row[headers[2]], row[headers[3]], row[headers[4]], row[headers[12]], row[headers[0]][:10] + ' 00:00:00')
                #print(parameters)
                cursor.execute(my_qry, parameters)
    mydb.commit()

    qry_italy_data = ("SELECT final_01_date, confirmed_number, hospitalized, in_icu, tested FROM final_01 WHERE final_01_country ='Italy' ORDER BY final_01_date")
    qry_update = ("UPDATE final_01 "
             "SET hospitalized_delta = %s, hospitalized_delta_p = %s, in_icu_delta = %s, in_icu_delta_p = %s, tested_pos = %s, tested_pos_delta = %s, tested_pos_delta_p = %s "
             "WHERE final_01_country = 'Italy' AND final_01_date = %s"
    )

    cursor_data = mydb.cursor()
    cursor_data.execute(qry_italy_data)
    records = cursor_data.fetchall()
    for row in records:
        i = records.index(row)
        if (i+1) < len(records):
            data_next = records[i+1]
            hospitalized_delta = data_next[2] - row[2]
            if row[2] != 0:
                hospitalized_delta_p = hospitalized_delta / row[2]
            else:
                hospitalized_delta_p = 0
            in_icu_delta = data_next[3] - row[3]
            if row[3] != 0:
                in_icu_delta_p = in_icu_delta / row[3]
            else:
                in_icu_delta_p = 0
            tested_pos_delta = data_next[1] - row[1]
            if row[1] != 0:
                tested_pos_delta_p = tested_pos_delta / row[1]
            else:
                tested_pos_delta_p = 0
            parameters = (hospitalized_delta, hospitalized_delta_p, in_icu_delta, in_icu_delta_p, data_next[1], tested_pos_delta, tested_pos_delta_p, data_next[0])
            cursor.execute(qry_update, parameters)

    mydb.commit()
    mydb.close()

def add_us_details():
    #Look at the webside https://carlsonschool.umn.edu/mili-misrc-covid19-tracking-project  describing which data I can use depending on what states report.

    state_list_01 = ['NY','NJ','CA','PA','LA', 'CT','TX','MO','WA','WI','NC','RI','DE','MN','OR','IA','NM','AR','VT','MT','ND','ME'] #States reporting hospitalization figures.
    file_us_details = '/home/luca/git/COVID-19_usa_details/data/states_daily_4pm_et.csv'
    add_us_details = ("UPDATE final_01 "
               "SET tested = %s, tested_pos = %s, hospitalized = %s, in_icu = %s "
               "WHERE final_01_country = 'US' AND final_01_region = %s AND final_01_date = %s")
    qry_get_state = ("SELECT state from us_states_list WHERE code = %s ")

    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      passwd="cacca1971",
      database="covid19"
    )

    cursor = mydb.cursor()

    with open(file_us_details, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        headers = reader.fieldnames
        for row in reader:
            if row[headers[1]] in state_list_01:
                cursor_data = mydb.cursor()
                state_code = row[headers[1]]
                cursor_data.execute(qry_get_state, (state_code,))
                record = cursor_data.fetchall()
                state_name = record[0][0]
                s = row[headers[0]] # This is the field containing the date. I have to change it to the format used in the db.
                #print(s)
                hospitalized = row[headers[5]]
                in_icu = row[headers[7]]
                if hospitalized == '':
                    hospitalized = '0'
                if in_icu =='':
                    in_icu = '0'
                parameters = (row[headers[16]], row[headers[2]], hospitalized, in_icu, state_name, date(int(s[:4]),int(s[4:6]),int(s[6:8])).isoformat())
                #print(parameters)
                cursor.execute(add_us_details, parameters)
    mydb.commit()

    qry_us_data = ("SELECT final_01_date, confirmed_number, hospitalized, in_icu, tested, final_01_region FROM final_01 WHERE final_01_country ='US' ORDER BY final_01_region, final_01_date")
    qry_update = ("UPDATE final_01 "
             "SET hospitalized_delta = %s, hospitalized_delta_p = %s, in_icu_delta = %s, in_icu_delta_p = %s, tested_pos_delta = %s, tested_pos_delta_p = %s "
             "WHERE final_01_country = 'US' AND final_01_region = %s AND final_01_date = %s"
    )

    cursor_data = mydb.cursor()
    cursor_data.execute(qry_us_data)
    records = cursor_data.fetchall()
    for row in records:
        i = records.index(row)
        if (i+1) < len(records):
            data_next = records[i+1]
            hospitalized_delta = data_next[2] - row[2]
            if row[2] != 0:
                hospitalized_delta_p = hospitalized_delta / row[2]
            else:
                hospitalized_delta_p = 0
            in_icu_delta = data_next[3] - row[3]
            if row[3] != 0:
                in_icu_delta_p = in_icu_delta / row[3]
            else:
                in_icu_delta_p = 0
            tested_pos_delta = data_next[1] - row[1]
            if row[1] != 0:
                tested_pos_delta_p = tested_pos_delta / row[1]
            else:
                tested_pos_delta_p = 0
            parameters = (hospitalized_delta, hospitalized_delta_p, in_icu_delta, in_icu_delta_p, tested_pos_delta, tested_pos_delta_p, data_next[5], data_next[0])
            cursor.execute(qry_update, parameters)

    mydb.commit()
    mydb.close()

def update_time():
    #Update a field in all countries to count from the first day when confirmed cases were greater than 100.
    qry_get_country = ("SELECT DISTINCT final_01_country from final_01 WHERE final_01_region = '' ORDER BY final_01_country") #List of countries
    qry_get_country_data = ("SELECT final_01_id, final_01_country, final_01_region, final_01_date, confirmed_number FROM final_01 WHERE final_01_region = '' AND final_01_country = %s ORDER BY final_01_date ")
    qry_update_time_point = ("UPDATE final_01 "
             "SET time_point = %s "
             "WHERE final_01_id = %s "
    )

    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      passwd="cacca1971",
      database="covid19"
    )

    cursor_country = mydb.cursor(buffered=True)
    cursor_data = mydb.cursor()
    cursor = mydb.cursor()

    cursor_country.execute(qry_get_country)
    for c in cursor_country:
        cursor_data.execute(qry_get_country_data, c)
        records = cursor_data.fetchall()
        time_p = 0
        for d in records:
            if d[4] >= 100:
                time_p += 1
                parameters = (time_p, d[0])
                cursor.execute(qry_update_time_point, parameters)

    mydb.commit()
    mydb.close()


def update_time_region():
    #Update a field in all countries to count from the first day when confirmed cases were greater than 100.
    qry_get_region= ("SELECT DISTINCT final_01_country, final_01_region from final_01 WHERE final_01_region <> '' ORDER BY final_01_country, final_01_region") #List of countries and regions
    qry_get_region_data = ("SELECT final_01_id, final_01_country, final_01_region, final_01_date, confirmed_number FROM final_01 WHERE final_01_region <> '' AND final_01_country = %s AND final_01_region = %s ORDER BY final_01_country, final_01_region, final_01_date ")
    qry_update_time_point = ("UPDATE final_01 "
             "SET time_point = %s "
             "WHERE final_01_id = %s "
    )

    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      passwd="cacca1971",
      database="covid19"
    )

    cursor_region = mydb.cursor(buffered=True)
    cursor_data = mydb.cursor()
    cursor = mydb.cursor()

    cursor_region.execute(qry_get_region)
    for c, r in cursor_region:
        cursor_data.execute(qry_get_region_data, (c, r))
        records = cursor_data.fetchall()
        time_p = 0
        for d in records:
            if d[4] >= 100:
                time_p += 1
                parameters = (time_p, d[0])
                cursor.execute(qry_update_time_point, parameters)

    mydb.commit()
    mydb.close()

remove_data(delete_tables)
add_data(queries_list, file_names)
update_final_01()
add_us_states()
add_italy_data()
add_us_details()
update_time()
update_time_region()
