import datetime
import time
from collections import namedtuple
shift = namedtuple("shift", "name, date, kanbans")
shifts = {num: shift for num in range(14)}

current_week_num = time.strftime("%U", time.gmtime())
next_week_num = time.strftime("%U", time.gmtime(time.time()+7*24*60*60))

date_now = datetime.datetime.now()
first_date = date_now - datetime.timedelta(days=date_now.weekday())

# Список дат
dates = [first_date+datetime.timedelta(days=x) for x in range(14)]

