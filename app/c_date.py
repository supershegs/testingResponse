import datetime

from datetime import datetime
# import pytz

# current_date = datetime.datetime.now()

current_date = datetime.now()
current_day_of_week = current_date.strftime("%A")

# utc_timezone = pytz.timezone('UTC')
# current_utc_time = datetime.datetime.now(utc_timezone)
# formatted_utc_time = current_utc_time.strftime('%Y-%m-%dT%H:%M:%SZ')



current_utc_time = datetime.utcnow()
formatted_utc_time = current_utc_time.strftime("%Y-%m-%dT%H:%M:%SZ")



print("Current Day of the Week:", current_day_of_week)
print(current_date)
print('utc: ',current_utc_time)
print('utc 1:',formatted_utc_time) #utc 1: 2023-09-09T13:43:27Z




