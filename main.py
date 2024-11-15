import datetime
import time
from kanban import Board, get_day_shift_name
from collections import namedtuple

current_week_num = time.strftime("%U", time.gmtime())
next_week_num = time.strftime("%U", time.gmtime(time.time() + 7 * 24 * 60 * 60))

b = Board("Test_board")

# print(*b.date_field, sep="\n")
# print(get_dates_list())
