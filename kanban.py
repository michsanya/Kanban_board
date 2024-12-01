import datetime
from logging import Logger

from Board_field import BoardField


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
        """
        Start kanban from Tasks List. Put its in In Work, and in current DateField
        :param start_date:
        :return:
        """
        start_date = datetime.datetime.now() if not start_date else start_date
        self.metadata["board"].in_work.append(self)
        self.metadata["board"].tasks_list.remove(self)
        self.metadata["started_date"] = start_date
        # TODO modify response type
        for shift in self.metadata["board"].date_field:
            if shift.start < start_date < shift.end:
                shift.kanbans.append(self)
                self.metadata["location"] = shift

    def finish(self, finish_date: datetime.datetime = None):
        """
        Finish kanban. Move it from In work and Datefield to Completed
        :param finish_date:
        :return:
        """
        finish_date = datetime.datetime.now() if not finish_date else finish_date
        self.metadata["board"].completed.append(self)
        self.metadata["board"].in_work.remove(self)
        self.metadata["finish_date"] = finish_date
        self.metadata["location"] = self.metadata["board"].completed
        for shift in self.metadata["board"].date_field:
            if self in shift.kanbans:
                shift.kanbans.remove(self)

    def move(self, dist_board_field):
        """
        Move kanban from datefield to other datefield or completed
        :param dist_board_field:
        :return:
        """
        if type(self.metadata["location"]) is BoardField:
            self.metadata["location"].kanbans.remove(self)
            self.metadata["board"].in_work.remove(self)
        else:
            self.metadata["location"].remove(self)
        if type(dist_board_field) is BoardField:
            dist_board_field.kanbans.append(self)
            self.metadata["board"].in_work.append(self)
        else:
            dist_board_field.append(self)
        self.metadata["location"] = dist_board_field
