import datetime
from main import get_dates_list
from enum import Enum



class Kanban:
    def __init__(self, kanban_type, text):
        self.kanban_type = kanban_type
        self.text = text

    def __str__(self):
        return str(self.text)

    __repr__ = __str__


class Board_Field:
    def __init__(self, date:datetime.datetime, is_morning:bool, shift_name:str):
        self.date = date
        # day shift (7:30-19:30) or night shift (19:30-7:30)
        self.is_morning = is_morning
        # A,B,C or D
        self.shift_name = shift_name
        self.kanbans = []


class Board:
    def __init__(self, name):
        self.name = name
        self.date_field = main.get_dates_list
        self.tasks_list = []
        self.completed = []

    def create_kanban(self, text):
        self.tasks_list.append(Kanban("WO", text))

bf = Board_Field(datetime.datetime.now(), True, "A")

