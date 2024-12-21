import datetime
import time

from Board_field import BoardField
from kanban import Kanban

current_week_num:str = time.strftime("%U", time.gmtime())
next_week_num:str = time.strftime("%U", time.gmtime(time.time() + 7 * 24 * 60 * 60))


def get_dates_list(date: datetime.datetime | None = None) -> list[datetime.datetime]:
    """
    Return list of 14 Datetimes objects for date board. First object is a Monday of current week or param date.
    :param date: date for creating table
    :return: list of 14 date from Monday. Date from param is in first week
    """
    date_now:datetime.datetime = date if date else datetime.datetime.now()
    first_date:datetime.datetime = date_now - datetime.timedelta(days=date_now.weekday())
    dates:list[datetime.datetime] = [first_date + datetime.timedelta(days=x) for x in range(14)]
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
    names:list[str] = names if names else ["A", "A", "B", "B", "C", "C", "D", "D"]
    num_of_day:int = date.timetuple().tm_yday
    delta:int = first_shift_of_first_shift.timetuple().tm_yday
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
    names_dict:dict[str, str] = {"A": "C",
                  "B": "D",
                  "C": "A",
                  "D": "B"} if not names else names
    return names_dict[day_shift]


class Board:
    first_shift_of_first_shift:datetime.datetime = datetime.datetime(2024, 1, 2)

    def check_expire(self):
        """
        Проверка доски на наличие канбанов, которые утсановлены в ячейки-даты, которые уже в прошлом.
        Если находится такой канбан - он передвигается на текущую дату
        :return:
        """
        now:datetime.datetime = datetime.datetime.now()
        for num, shift in enumerate(self.date_field):
            if shift.kanbans and shift.end < now:
                for kanban in  shift.kanbans.copy():
                    kanban.move(self.date_field[num+1])

    def check_responsibility(self):
        """
        Проверка доски на соответствие ответственнеости канбана и смены
        """
        for num, shift in enumerate(self.date_field[:-1]):
            if shift.kanbans:
                for kanban in shift.kanbans.copy():
                    splitted_response = kanban.response.split()
                    if "Nobody" in splitted_response:
                        continue
                    
                    if kanban.response == "All":
                        if shift.shift_name in "ABCD":
                            continue
                        else:
                            kanban.move(self.date_field[num+1])
                    
                    if any(("A" in splitted_response,"B" in splitted_response,"C" in splitted_response,"D" in splitted_response)):
                        if shift.shift_name not in splitted_response:
                            kanban.move(self.date_field[num+1])

                    if (("day" in splitted_response) or ("night" in splitted_response)):
                        if shift.is_morning and "day" in splitted_response:
                            continue
                        # else:
                        #     kanban.move(self.date_field[num+1])
                        if "night" in splitted_response and not shift.is_morning:
                            continue
                        else:
                            kanban.move(self.date_field[num+1])


    def __init__(self, name):
        self.name:str = name
        self.in_work:list[None|Kanban] = []
        self.tasks_list:list[None|Kanban] = []
        self.completed:list[None|Kanban] = []
        self.date_field:list[None|BoardField] = []
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
        kanban:Kanban = Kanban("WO", text)
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
