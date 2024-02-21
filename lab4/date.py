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
def seconds_dif(date1_str, date2_str):
    date_format = '%Y-%m-%d'

    date1 = datetime.datetime.strptime(date1_str, date_format)
    date2 = datetime.datetime.strptime(date2_str, date_format)

    difference = date2 - date1

    return difference.total_seconds()





