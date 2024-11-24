import datetime
from Board import Board

b = Board("Test_board")

k1 = b.create_kanban("My kanban")

k1.start(datetime.datetime(year=2024, month=11, day=25, hour=20))
