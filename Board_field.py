import datetime


class BoardField:
    def __init__(self, date: datetime.datetime, is_morning: bool, shift_name: str):
        self.is_morning = is_morning
        if self.is_morning:
            self.start = date.replace(hour=7, minute=30, second=0, microsecond=0)
        else:
            self.start = date.replace(hour=19, minute=30, second=0, microsecond=0)
        self.end = self.start + datetime.timedelta(hours=12)
        # A,B,C or D
        self.shift_name = shift_name
        self.kanbans = []

    def __str__(self):
        return f"{self.start.strftime('%d.%m %H:%M')}, {self.shift_name}, {len(self.kanbans)}"

    __repr__ = __str__

    def add(self, kanban):
        self.kanbans.append(kanban)
