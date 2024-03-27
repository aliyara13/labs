#ex1
import datetime
x = datetime.datetime.now()
print(x.day-5)

#ex2
from datetime import date
x = date.today()
print(x.day)

#ex3
def delete_microseconds():
    def drop_microseconds(dt):
        return dt.replace(microsecond=0)

    now = datetime.datetime.now()
    print(f'Original datetime {now}')

    without_microseconds = drop_microseconds(now)
    print(f'Withoud microseconds {without_microseconds}')

#ex4
from datetime import datetime

def seconds_difference(date1, date2):
    
    datetime1 = datetime.strptime(date1, "%Y-%m-%d %H:%M:%S")
    datetime2 = datetime.strptime(date2, "%Y-%m-%d %H:%M:%S")
    
    difference = (datetime2 - datetime1).total_seconds()
    
    return difference





