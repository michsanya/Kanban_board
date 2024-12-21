import datetime
from typing import TypeVar

Kanban = TypeVar('Kanban')

class BoardField:
    def __init__(self, date: datetime.datetime, is_morning: bool, shift_name: str):
        self.is_morning:bool = is_morning
        if self.is_morning:
            self.start:datetime.datetime = date.replace(hour=7, minute=30, second=0, microsecond=0)
        else:
            self.start:datetime.datetime = date.replace(hour=19, minute=30, second=0, microsecond=0)
        self.end:datetime.datetime = self.start + datetime.timedelta(hours=12)
        # A,B,C or D
        self.shift_name:str = shift_name
        self.kanbans:list[Kanban] = []

    def __str__(self):
        return f"{self.start.strftime('%d.%m %H:%M')}, {self.shift_name}, {len(self.kanbans)}"

    __repr__ = __str__

    def add(self, kanban:Kanban):
        """
        add kanban in list kanbans
        :param kanban:
        :return:
        """
        self.kanbans.append(kanban)
