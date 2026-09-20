    # The idea is to have the 3 file names in a list. Then a list with the 3 queries.
# Then pass the 2 lists with files and queries to a function. Then the function iterates on files and queries and writes the db.
# The pre-requisite is the 3 files have the same structure.

# At the end of the process the data to be used for analysis and reporting are going to be in MySQL in the table final_01.
# In the process, some of the ratios are already calculated and are available in the table.

"""
I load the data from 3 csv files which bring confirmed cases, deaths and recovered. Using these 3 numbers I calculate the current positive cases.
Then, once the data area loaded, I calculate the deltas and the deltas in percent.
In these 3 files, some countries have regions (e.g. France, UK), therefore in these cases in the db there isn't one record representing the total for the country.
I have to keep this in mind in the dashboard, because it means I have to build a pandas dataframe which sums all the region for the selected country if I want the country total.

In the 3 csv files the US is showed as a total, there are no states. I load state data from another source.
That means at db level the US is an exception because it has records for the states (i.e. regions) and it also has a record representing the country total.
I can not simply remove the record representing US as total because that holds the number of recovered patients which is NOT available by state.
So if I removed the total US I would lose the ability to calculate the current positive cases in the US.

NOTE: if in the future I bring details for other countries (e.g. regions in Italy), I would need to treat those countries like the US.

TODO 1: calculate deltas for data about Regions in Italy (in principle I don't need it because I calculate the deltas with pandas in the dash app).
TODO 2: write some tests to check the data in the db vs the files.
TODO 4: add to the log info about records inserted/updated; can use this print("Inserted",cursor.rowcount,"row(s) of data.")
TODO 5: now the file used for US details has the number of recovered patients too, so if I add the data point I can then calculate the current positive by US state.
TODO 6: add details for Switzerland (https://github.com/daenuprobst/covid19-cases-switzerland)
    The files to use for Switzerland are:
        covid19_cases_switzerland_openzh.csv
        covid19_fatalities_switzerland_openzh.csv
        covid19_hospitalized_switzerland_openzh.csv
        covid19_icu_switzerland_openzh.csv
        covid19_released_switzerland_openzh.csv
        covid19_tested_switzerland_openzh.csv
        demographics.csv --> Population figures are in this file
    In all files cantons are by column; the last column is the total for the country.
    The challenge is that sometimes a cell is empty, which means the last reported data has to be used. I have to think how to fill these empty cells in the database.
    Remember to cancel the Swiss data coming from the first load because I want to calculate them as totals of the detailed data.



"""

import csv
import mysql.connector
import datetime
import time
from datetime import date, datetime

log_file = '/home/luca/git/learning/Python/covid-19/covid_log.txt'

def print_to_log(s):
    try:
        with open(log_file, 'a') as f:
            f.write(s + '\n')
    except IOError as error:
        print('Error opening log file: ' + str(log_file))


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
    time_start = time.time()
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
    time_end = time.time()
    print_to_log('add_data function: ' + str(time_end-time_start))


#These are queries to empty the tables before loading fresh data.
delete_tables = []
delete_tables.extend(["delete from confirmed","delete from deaths", "delete from recovered", "delete from final_01", "delete from us_states", "delete from italy"])

def remove_data(qry):
    # Takes a list of delete queries and executes them.
    time_start = time.time()

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

    time_end = time.time()
    print_to_log('remove_data function: ' + str(time_end-time_start))

def update_final_01():

    time_start = time.time()

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

    time_end = time.time()
    print_to_log('update_final_01 function: ' + str(time_end-time_start))

def add_us_states():

    time_start = time.time()

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

    time_end = time.time()
    print_to_log('add_us_states function: ' + str(time_end-time_start))

def add_italy_data():

    time_start = time.time()

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
                parameters = (row[headers[2]], row[headers[3]], row[headers[4]], row[headers[14]], row[headers[0]][:10] + ' 00:00:00')
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

    time_end = time.time()
    print_to_log('add_italy_data function: ' + str(time_end-time_start))

def add_italy_regions():

    time_start = time.time()

    file_ita_reg = '/home/luca/git/COVID-19_italy/dati-regioni/dpc-covid19-ita-regioni.csv'
    add_ita = ("INSERT INTO final_01 "
               "(final_01_country, final_01_region, final_01_date, confirmed_number, deaths_number, recovered_number, current_positive, hospitalized, in_icu, hospitalized_tot, tested, tested_pos) "
               "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) "
               )

    file_names=[]
    file_names.append(file_ita_reg) #I thought I could use the logic below to load multiple files using multiple queries; that's not the case but I did not change the code.

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
                parameters = ('Italy', row[headers[3]], row[headers[0]][:10] + ' 00:00:00' , row[headers[17]], row[headers[14]], row[headers[13]], row[headers[10]], row[headers[6]], row[headers[7]], row[headers[8]], row[headers[18]], row[headers[17]],)
                #print(parameters)
                cursor.execute(my_qry, parameters)
    mydb.commit()

    time_end = time.time()
    print_to_log('add_italy_regions function: ' + str(time_end-time_start))

def add_us_details():
    #Look at the webside https://carlsonschool.umn.edu/mili-misrc-covid19-tracking-project  describing which data I can use depending on what states report.

    time_start = time.time()

    #state_list_01 = ['NY','NJ','CA','PA','LA', 'CT','TX','MO','WA','WI','NC','RI','DE','MN','OR','IA','NM','AR','VT','MT','ND','ME', 'AK']
    state_list_01 = ['AK','AL','AR','AZ','CA','CO','CT','DC','DE','FL','GA','GU','IA','IL','IN','KY','LA','MA','MD','ME','MI','MN','MO',
    'MS','MT','NC','ND','NE','NH','NJ','NM','NV','NY','OH','OK','OR','PA','PR','RI','SC','SD','TX','UT','VA','VI','VT','WA',
    'WI','WV','WY']

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
                hospitalized = row[headers[8]]
                in_icu = row[headers[10]]
                tested = row[headers[7]]
                tested_pos = row[headers[2]]
                if hospitalized == '':
                    hospitalized = '0'
                if in_icu =='':
                    in_icu = '0'
                if tested =='':
                    tested = '0'
                if tested_pos =='':
                    tested_pos = '0'
                parameters = (tested, tested_pos, hospitalized, in_icu, state_name, date(int(s[:4]),int(s[4:6]),int(s[6:8])).isoformat())
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

    time_end = time.time()
    print_to_log('add_us_details function: ' + str(time_end-time_start))

def update_time():

    time_start = time.time()

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

    time_end = time.time()
    print_to_log('update_time function: ' + str(time_end-time_start))

def update_time_region():

    time_start = time.time()

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

    time_end = time.time()
    print_to_log('update_time_region function: ' + str(time_end-time_start))


def total_records(): #I am NOT using this function anymore. See notes at the beginning.
    """
    With the exception of US and Italy (and possibly other countries in the future), I need to calculate a country total.
    Because for the countries with Region information the data (COVID-19_world) do not have a total for the country.
    This is not a problem for the countries without Region information.
    US and Italy are an exception because I load the region data from another source, hence the data from COVID-19_world do represent a total for US and Italy.
    After this function runs:
    For countries without region, in each day there is one record where the region is called as in the label (e.g. Country Total) which is the record I get from the csv file.
    For countries with regions, in each day there are several reacors one per region plus a new record I insert which represents the country total (with the same label as above).
    For exceptions (Italy, US) the result is the same but I need a slightly different logic.

    As I am NOT re-calculating the delta and delta_p fields for these records, I have to use the DataFrame.pct_change and DataFrame.diff features in Pandas when I want to show those deltas.
    """
    label = "Country Total"
    exceptions = ['US', 'Italy']

    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      passwd="cacca1971",
      database="covid19"
    )

    qry_countries = ("SELECT DISTINCT final_01_country FROM final_01 ORDER BY final_01_country ")
    qry_regions = ("SELECT DISTINCT final_01_region FROM final_01 WHERE final_01_country = %s ORDER BY final_01_region ")
    qry_update = ("UPDATE final_01 SET final_01_region = %s WHERE final_01_country = %s ")
    qry_update_exceptions = ("UPDATE final_01 SET final_01_region = %s WHERE final_01_country = %s AND final_01_region = \"\" ")
    qry_total = ("INSERT INTO final_01 "
                 "(final_01_country, final_01_date, final_01_region, confirmed_number, deaths_number, recovered_number, current_positive, confirmed_delta, deaths_delta, recovered_delta, current_positive_delta, hospitalized, in_icu, hospitalized_tot, tested, tested_pos, hospitalized_delta, in_icu_delta, tested_pos_delta) "
                 "SELECT final_01_country, final_01_date, %s ,  SUM(confirmed_number), SUM(deaths_number), SUM(recovered_number), SUM(current_positive), SUM(confirmed_delta), SUM(deaths_delta), SUM(recovered_delta), SUM(current_positive_delta), SUM(hospitalized), SUM(in_icu), SUM(hospitalized_tot), SUM(tested), SUM(tested_pos), SUM(hospitalized_delta), SUM(in_icu_delta), SUM(tested_pos_delta) "
                 "FROM final_01 WHERE final_01_country = %s GROUP BY final_01_country, final_01_date "
                )


    cursor_countries = mydb.cursor()
    cursor_regions = mydb.cursor()
    cursor = mydb.cursor()

    cursor_countries.execute(qry_countries)
    countries = cursor_countries.fetchall()
    for c in countries:
        cursor_regions.execute(qry_regions, c)
        regions = cursor_regions.fetchall()
        if len(regions) == 1:
            param = (label, c[0])
            cursor.execute(qry_update, param)
        else:
            if c[0] not in exceptions:
                param = (label, c[0])
                cursor.execute(qry_total, param)
    mydb.commit()

    for c in exceptions:
        param = (label, c)
        cursor.execute(qry_update_exceptions, param)

    mydb.commit()

    for c in countries:
        label = (c[0]+"_OtherRegions")
        param = (label, c[0])
        cursor.execute(qry_update_exceptions, param)

    mydb.commit()
    mydb.close()

def update_exceptions():
    """
    Using this function to set to 0 some fields of those countries where I first load the totals and then the details.
    In this moment US and Italy.
    """

    time_start = time.time()

    exc = ['US', 'Italy'] # Add here more exceptions in the future.
    exc_2 = ['Italy'] # I need a second case because Italy has the number of recovered people at Region level which the US does not have.

    qry = ("UPDATE final_01 "
           "SET confirmed_number = %s, deaths_number = %s, confirmed_delta = %s, confirmed_delta_p = %s, deaths_delta = %s, deaths_delta_p = %s, hospitalized = %s, in_icu = %s, hospitalized_tot = %s, tested = %s, tested_pos = %s "
           "WHERE final_01_country = %s AND final_01_region = \'\' "
           )
    qry_2 = ("UPDATE final_01 "
           "SET current_positive = %s "
           "WHERE final_01_country = %s AND final_01_region = \'\' "
           )
    mydb = mysql.connector.connect(
          host="localhost",
          user="root",
          passwd="cacca1971",
          database="covid19"
          )
    cursor = mydb.cursor()

    for c in exc:
        param = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,c)
        cursor.execute(qry, param)

    mydb.commit()

    for c in exc_2:
        param = (0, c)
        cursor.execute(qry_2, param)

    mydb.commit()
    mydb.close()

    time_end = time.time()
    print_to_log('update_exceptions function: ' + str(time_end-time_start))

def add_canada():
    """
    In case of Canada the confirmed and deaths files have the regions details, BUT the recovered file has the total for the country only.
    Because of this reason, when I build the current_positive view in SQL Canada is not included.
    To fix this I've created totals for Canada in SQL and now I use this function to add the Canada records to final_01.
    I've lost the region details for Canada, but I did not have time to look for recovered by region in Canada.
    Furthermore, I have NOT calculated the deltas for Canada, so the deltas must be calculated with Pandas in the front end.
    """
    time_start = time.time()

    qry_add = ("INSERT INTO final_01 "
                 "(final_01_country, final_01_region, final_01_date, confirmed_number, deaths_number, recovered_number, current_positive) "
                 "SELECT confirmed_country, confirmed_region, confirmed_date, confirmed_number, deaths_number, recovered_number, current_positive "
                 "FROM canada_step_02"
            )

    mydb = mysql.connector.connect(
          host="localhost",
          user="root",
          passwd="cacca1971",
          database="covid19"
          )
    cursor = mydb.cursor()
    cursor.execute(qry_add)
    mydb.commit()
    mydb.close()

    time_end = time.time()
    print_to_log('add_canada function: ' + str(time_end-time_start))


print_to_log('*** Starting Log for: ' + str(datetime.now()) + ' ***')
remove_data(delete_tables)
add_data(queries_list, file_names)
update_final_01()
add_canada()
add_us_states()
add_italy_data()
add_italy_regions()
add_us_details()
update_time()
update_time_region()
update_exceptions()

#total_records() I DO NOT NEED THIS FUNCTION ANYMORE. See notes at the beginning.
