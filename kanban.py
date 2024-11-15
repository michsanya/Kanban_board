import datetime
from enum import Enum


def get_dates_list(date: datetime.datetime | None = None) -> list[datetime.datetime]:
    date_now = date if date else datetime.datetime.now()
    first_date = date_now - datetime.timedelta(days=date_now.weekday())
    dates = [first_date + datetime.timedelta(days=x) for x in range(14)]
    return dates


def get_day_shift_name(date: datetime.datetime,
                       first_shift_of_first_shift: datetime.datetime,
                       names: list[str] | None = None
                       ) -> str:
    names = names if names else ["A", "A", "B", "B", "C", "C", "D", "D"]
    num_of_day = date.timetuple().tm_yday
    delta = first_shift_of_first_shift.timetuple().tm_yday
    return names[(num_of_day - delta) % len(names)]


def get_night_shift_name(day_shift: str,
                         names: list[str] | None = None
                         ) -> str:
    names_dict = {"A": "C",
                  "B": "D",
                  "C": "A",
                  "D": "B"}
    return names_dict[day_shift]


class Kanban:
    def __init__(self, kanban_type, text):
        self.kanban_type = kanban_type
        self.text = text

    def __str__(self):
        return str(self.text)

    __repr__ = __str__


class Board_Field:
    def __init__(self, date: datetime.datetime, is_morning: bool, shift_name: str):
        self.date = date
        # day shift (7:30-19:30) or night shift (19:30-7:30)
        self.is_morning = is_morning
        # A,B,C or D
        self.shift_name = shift_name

    def __str__(self):
        return f"{self.date.strftime('%d.%m')},{self.shift_name},{'D' if self.is_morning else 'N'}"

    __repr__ = __str__


class Board:
    first_shift_of_first_shift = datetime.datetime(2024, 1, 2)

    def __init__(self, name):
        self.name = name
        # self.date_field = [Board_Field(x, True, "Z") for x in get_dates_list()]
        self.date_field = []
        for x in get_dates_list():
            self.date_field.append(Board_Field(x, True, n := get_day_shift_name(x, Board.first_shift_of_first_shift)))
            self.date_field.append(Board_Field(x, False, get_night_shift_name(n)))

        self.in_work = []
        self.tasks_list = []
        self.completed = []

    def create_kanban(self, text):
        self.tasks_list.append(Kanban("WO", text))
