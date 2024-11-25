import datetime
from logging import Logger


class Kanban:
    def __init__(self, kanban_type, text):
        self.kanban_type = kanban_type
        self.text = text
        self.metadata = {"creation_date": datetime.datetime.now()}
        self.response = "Nobody"  # Nobody, All, A, B, C, D, day, night

    def __str__(self):
        return str(self.text)

    __repr__ = __str__

    def start(self, start_date: datetime.datetime = None):
        start_date = datetime.datetime.now() if not start_date else start_date
        self.metadata["board"].in_work.append(self)
        self.metadata["board"].tasks_list.remove(self)
        self.metadata["started_date"] = start_date
        # TODO modify response type
        for shift in self.metadata["board"].date_field:
            if shift.start < start_date < shift.end:
                shift.kanbans.append(self)

    def finish(self, finish_date: datetime.datetime = None):
        finish_date = datetime.datetime.now() if not finish_date else finish_date
        self.metadata["board"].completed.append(self)
        self.metadata["board"].in_work.remove(self)
        self.metadata["finish_date"] = finish_date
        for shift in self.metadata["board"].date_field:
            if self in shift.kanbans:
                shift.kanbans.remove(self)

