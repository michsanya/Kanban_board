import datetime
import time
from kanban import Board, get_day_shift_name

current_week_num = time.strftime("%U", time.gmtime())
next_week_num = time.strftime("%U", time.gmtime(time.time() + 7 * 24 * 60 * 60))

b = Board("Test_board")

k1 = b.create_kanban("My kanban")

#k1.start()
