import datetime
from datetime import date, datetime

log_file = '/home/luca/git/learning/Python/covid-19/covid_log.txt'
try:
    with open(log_file, 'a') as f:
        f.write('Starting Log ... ' + str(datetime.now()) + '\n')
except IOError as error:
    print("Error opening log file: " + str(log_file))

f.write('Cacca')
