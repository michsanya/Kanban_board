import datetime
import time

from Board_field import BoardField
from kanban import Kanban

current_week_num = time.strftime("%U", time.gmtime())
next_week_num = time.strftime("%U", time.gmtime(time.time() + 7 * 24 * 60 * 60))


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
                  "D": "B"} if not names else names
    return names_dict[day_shift]


class Board:
    first_shift_of_first_shift = datetime.datetime(2024, 1, 2)

    def __init__(self, name):
        self.name = name
        self.in_work = []
        self.tasks_list = []
        self.completed = []
        self.date_field = []
        for x in get_dates_list():
            self.date_field.append(BoardField(x, True, n := get_day_shift_name(x, Board.first_shift_of_first_shift)))
            self.date_field.append(BoardField(x, False, get_night_shift_name(n)))

    def __str__(self):
        return f"* {self.name} *\nNot started: {self.tasks_list}\nIn work: {self.in_work}\nCompleted: {self.completed}"

    def create_kanban(self, text):
        kanban = Kanban("WO", text)
        kanban.metadata["board"] = self
        self.tasks_list.append(kanban)
        return kanban

    def get_kanbans(self) -> list[Kanban]:
        return self.tasks_list + self.in_work + self.completed
