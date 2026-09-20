"""
TODO: check how to deal with the population of china and its regions. Maybe the easiest is to get the population data for all chinese regions.
"""

import csv
import mysql.connector

def delete_tables():
    delete_tables = []
    delete_tables.extend(["delete from population"])

    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      passwd="cacca1971",
      database="covid19"
    )
    cursor = mydb.cursor()
    for my_qry in delete_tables:
        cursor.execute(my_qry)
        mydb.commit()

def load_world_pop():
    file_world_pop = '/home/luca/git/population_world/data/population.csv'
    add_world_pop = ("INSERT INTO population"
                     "(population_country, population_region, population_size)"
                     "VALUES (%s,%s,%s)"
    )

    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      passwd="cacca1971",
      database="covid19"
    )
    cursor = mydb.cursor()
    with open(file_world_pop, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        headers = reader.fieldnames
        for row in reader:
            if row['Year'] == '2018': # 2018 is the most recent year available in the data.
                my_record = []
                for item in headers:
                    my_record.append(row[item])
                data = (my_record[0],'', my_record[3])
                cursor.execute(add_world_pop, data)

    mydb.commit()

def delete_exceptions():
    exceptions = ['Italy', 'US'] #For these countries the total will come as total of the regions, hence I delete the total coming from the world population file.
    qry_delete = "DELETE from population WHERE population_country = %s"

    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      passwd="cacca1971",
      database="covid19"
    )
    cursor = mydb.cursor()

    for e in exceptions:
        cursor.execute(qry_delete, (e,))
    mydb.commit()

def update_mismatch():
    #The world population file has some country names which are different from the covid data file.
    #Hence I now update the population data with the names matching the covid data file.

    exceptions = {'Bahamas, The': 'Bahamas',
                  'Brunei Darussalam': 'Brunei',
                  'Congo, Dem. Rep.': 'Congo (Kinshasa)',
                  'Congo, Rep.': 'Congo (Brazzaville)',
                  'Czech Republic': 'Czechia',
                  'Egypt, Arab Rep.': 'Egypt',
                  'Gambia, The': 'Gambia',
                  'Iran, Islamic Rep.': 'Iran',
                  'Korea, Rep.': 'Korea, South',
                  'Myanmar': 'Burma',
                  'Russian Federation': 'Russia',
                  'Slovak Republic': 'Slovakia',
                  'United States': 'US',
                  'Venezuela, RB': 'Venezuela',
                  'Yemen, Rep.': 'Yemen'
    }
    qry = ("UPDATE population SET population_country = %s WHERE population_country = %s")

    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      passwd="cacca1971",
      database="covid19"
    )
    cursor = mydb.cursor()

    for a, b in exceptions.items():
        cursor.execute(qry,(b,a))

    mydb.commit()


def load_italy_pop():
    file_italy_pop = '/home/luca/git/population_italy/population_italy.csv'
    add_italy_pop = ("INSERT INTO population"
                     "(population_country, population_region, population_size, population_surface_km)"
                     "VALUES (%s,%s,%s,%s)"
    )

    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      passwd="cacca1971",
      database="covid19"
    )
    cursor = mydb.cursor()
    with open(file_italy_pop, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        headers = reader.fieldnames
        for row in reader:
            my_record = []
            for item in headers:
                my_record.append(row[item])
            data = ('Italy', my_record[0],my_record[1],my_record[2])
            cursor.execute(add_italy_pop, data)

    mydb.commit()

def load_usa_pop():
    file_us_pop = '/home/luca/git/population_us/us_census_data/us_census_2018_population_estimates_states.csv'
    add_us_pop = ("INSERT INTO population"
                     "(population_country, population_region, population_size)"
                     "VALUES (%s,%s,%s)"
    )

    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      passwd="cacca1971",
      database="covid19"
    )
    cursor = mydb.cursor()
    with open(file_us_pop, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        headers = reader.fieldnames
        for row in reader:
            my_record = []
            for item in headers:
                my_record.append(row[item])
            data = ('US', my_record[1],my_record[3])
            cursor.execute(add_us_pop, data)

    mydb.commit()


delete_tables()
load_world_pop()
update_mismatch()
delete_exceptions()
load_italy_pop()
load_usa_pop()
