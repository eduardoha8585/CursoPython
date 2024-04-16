### Dates ###
from datetime import datetime
from datetime import time
from datetime import date

#---------------TRABAJANDO CON datetime---------------
now = datetime.now()

def print_date(date):
    print('hora',date.hour)
    print('minutos',date.minute)
    print('segundos',date.second)  
    print('año', date.year)     
    print('mes',date.month)
    print('dia',date.day)
    print('timestamp', date.timestamp())

print_date(now)

year_2024 = datetime(2024, 1, 1)

print_date(year_2024)

#---------------TRABAJANDO CON time---------------

'''current_time = time(hour=2,minute=10,second=20) esta es una manera de rellenar time'''
current_time = time(now.hour, now.minute, now.second)
print('time', current_time)
print('time_hour', current_time.hour)
print('time_minute', current_time.minute)
print('time_second', current_time.second)

#---------------TRABAJANDO CON DATE---------------
current_date = date(now.year, now.month, now.day)
print('date', current_date)
print('date_year', current_date.year)
print('date_month', current_date.month)
print('date_day', current_date.day)

