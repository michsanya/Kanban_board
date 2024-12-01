import datetime
from unittest import TestCase

from Board import Board

b = Board("Test_board")
for i in range(10):
    b.create_kanban(f"My kanban {i}")


class TestKanban(TestCase):

    def test_start(self):
        b.tasks_list[4].start()
        b.tasks_list[2].start()
        b.tasks_list[2].start(datetime.datetime(year=2024, month=11, day=25, hour=11, minute=00))
        self.fail()

    def test_finish(self):
        b.tasks_list[4].start()
        b.tasks_list[2].start()
        b.tasks_list[2].start(datetime.datetime(year=2024, month=11, day=25, hour=11, minute=00))
        print(f"{b.in_work=}")
        print(f"{b.date_field=}")
        print(f"{b.completed=}")
        b.in_work[0].finish()
        print(f"{b.in_work}")
        print(f"{b.date_field=}")
        print(f"{b.completed=}")
        print(f"{b.completed[0].metadata=}")
        self.fail()


class TestKanban(TestCase):
    def test_start(self):
        self.fail()


class TestKanban(TestCase):
    def test_move(self):
        self.fail()
