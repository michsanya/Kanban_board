import datetime
from Board import Board

b = Board("Test_board")

for i in range(10):
    b.create_kanban(f"My kanban {i}")

b.tasks_list[4].start()
b.tasks_list[2].start()
b.tasks_list[2].start(datetime.datetime(year=2024, month=11, day=25, hour=11, minute=00))
k = b.tasks_list[2]
k.start()
k.move(b.completed)
print(b.date_field)
b.check_expire()
print(b.date_field)
