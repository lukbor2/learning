import csv
import mysql.connector
from datetime import date

#file_to_open = '/home/luca/git/learning/csv_read.csv'
#the one below is a test file.
#TODO: think whether to put the file and location in a config file.
#TODO: think whether to write some messages in a log file as the program executes.
file_to_open = '/home/luca/git/COVID-19_world/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Confirmed_copy.csv'

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="cacca1971",
  database="covid19"
)

cursor = mydb.cursor()
add_confirmed = ("INSERT INTO confirmed "
                 "(confirmed_country, confirmed_region, confirmed_lat, confirmed_long, confirmed_date, confirmed_number)"
                 "VALUES (%s,%s,%s,%s,%s,%s)"
)

with open(file_to_open, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    headers = reader.fieldnames
    reader.__next__()
    for row in reader:
        # print(row['Name'], row['Surname'])
        my_record = []
        for item in headers[:4]:
            my_record.append(row[item])
        for item in headers[4:]:
            # my_record_final=[]
            my_record_final = my_record.copy()
            my_record_final.append(item)
            my_record_final.append(row[item])
            #print(my_record_final)
            dt = my_record_final[4].split('/')
            data = (my_record_final[1], my_record_final[0],my_record_final[2],my_record_final[3],date(int(dt[2]), int(dt[0]), int(dt[1])), my_record_final[5])
            #data = ('Japan', '', '15', '101', '20200122', '2')
            cursor.execute(add_confirmed, data)
mydb.commit()
