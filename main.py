import datetime
import time
from collections import namedtuple

shift = namedtuple("shift", "name, date, kanbans")
shifts = {num: shift for num in range(14)}

current_week_num = time.strftime("%U", time.gmtime())
next_week_num = time.strftime("%U", time.gmtime(time.time() + 7 * 24 * 60 * 60))


def get_dates_list(date: datetime.datetime | None = None) -> list[datetime.datetime]:
    date_now = date if date else datetime.datetime.now()
    first_date = date_now - datetime.timedelta(days=date_now.weekday())
    dates = [first_date + datetime.timedelta(days=x) for x in range(14)]
    return dates


#print(get_dates_list())
