import datetime
from Board import Board

b = Board("Test_board")

for i in range(10):
    b.create_kanban(f"My kanban {i}")

b.tasks_list[4].start(response="D")
b.tasks_list[2].start(response="A night")
#TODO Перепрыгивает через один канбана, так как предыдущий перемещается
b.tasks_list[2].start(datetime.datetime(year=2024, month=12, day=19, hour=11, minute=00))
k = b.tasks_list[2]
k.start()
k.move(b.completed)
print(*b.date_field, sep='\n', end = '\n\n*********************             \n')
b.check_expire()
print(*b.date_field, sep='\n', end = '\n\n*********************             \n')
b.check_responsibility()
print(*b.date_field, sep='\n', end = '\n\n*********************             \n')