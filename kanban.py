import datetime
from enum import Enum


def get_dates_list(date: datetime.datetime | None = None) -> list[datetime.datetime]:
    date_now = date if date else datetime.datetime.now()
    first_date = date_now - datetime.timedelta(days=date_now.weekday())
    dates = [first_date + datetime.timedelta(days=x) for x in range(14)]
    return dates


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
    def __str__(self):
        return f"{self.date.strftime('%d.%m')},{self.shift_name},{'D' if self.is_morning else 'N'}"
    __repr__=__str__


class Board:
    def __init__(self, name):
        self.name = name
        # self.date_field = [Board_Field(x, True, "Z") for x in get_dates_list()]
        self.date_field = []
        for x in get_dates_list(): 
            self.date_field.append(Board_Field(x, True, "Z"))
            self.date_field.append(Board_Field(x, False, "Z"))
        
        self.in_work = []
        self.tasks_list = []
        self.completed = []

    def create_kanban(self, text):
        self.tasks_list.append(Kanban("WO", text))

