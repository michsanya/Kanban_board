import datetime
import time

from Board_field import BoardField
from kanban import Kanban

current_week_num = time.strftime("%U", time.gmtime())
next_week_num = time.strftime("%U", time.gmtime(time.time() + 7 * 24 * 60 * 60))


def get_dates_list(date: datetime.datetime | None = None) -> list[datetime.datetime]:
    """
    Return list of 14 Datetimes objects for date board. First object is a Monday of current week or param date.
    :param date: date for creating table
    :return: list of 14 date from Monday. Date from param is in first week
    """
    date_now = date if date else datetime.datetime.now()
    first_date = date_now - datetime.timedelta(days=date_now.weekday())
    dates = [first_date + datetime.timedelta(days=x) for x in range(14)]
    return dates


def get_day_shift_name(date: datetime.datetime,
                       first_shift_of_first_shift: datetime.datetime,
                       names: list[str] | None = None
                       ) -> str:
    """
    Return morning shift name by date in param
    :param date: what is morning shift in this date?
    :param first_shift_of_first_shift: first date when shift A was working in year
    :param names: cycle of names
    :return: shift name
    """
    names = names if names else ["A", "A", "B", "B", "C", "C", "D", "D"]
    num_of_day = date.timetuple().tm_yday
    delta = first_shift_of_first_shift.timetuple().tm_yday
    return names[(num_of_day - delta) % len(names)]


def get_night_shift_name(day_shift: str,
                         names: list[str] | None = None
                         ) -> str:
    """
    Return name of night shift by morning shift
    :param day_shift:
    :param names: dict Morning - Night
    :return: name of night shift
    """
    names_dict = {"A": "C",
                  "B": "D",
                  "C": "A",
                  "D": "B"} if not names else names
    return names_dict[day_shift]


class Board:
    first_shift_of_first_shift = datetime.datetime(2024, 1, 2)

    def check_expire(self):
        """
        Проверка доски на наличие канбанов, которые утсановлены в ячейки-даты, которые уже в прошлом.
        Если находится такой канбан - он передвигается на текущую дату
        :return:
        """
        now = datetime.datetime.now()
        for num, shift in enumerate(self.date_field):
            if shift.kanbans and shift.end < now:
                for kanban in  shift.kanbans:
                    kanban.move(self.date_field[num+1])

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
        """
        Create WO kanban and put it in Tasks List
        :param text:
        :return: kanban
        """
        kanban = Kanban("WO", text)
        kanban.metadata["board"] = self
        kanban.metadata["location"] = self.tasks_list
        self.tasks_list.append(kanban)
        return kanban

    def get_kanbans(self) -> list[Kanban]:
        """
        Return all kanbans from Tasks list, In work, Completed
        :return:
        """
        return self.tasks_list + self.in_work + self.completed
