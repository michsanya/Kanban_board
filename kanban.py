class Kanban:
    def __init__(self, kanban_type, text):
        self.kanban_type = kanban_type
        self.text = text

    def __str__(self):
        return str(self.text)

    __repr__ = __str__


class Board_Field:
    def __init__(self):
        self.date = ...
        # day shift (7:30-19:30) or night shift (19:30-7:30)
        self.day_or_night = ...
        # A,B,C or D
        self.shift_name = ...


class Board:
    def __init__(self, name):
        self.name = name
        self.date_field = []
        self.tasks_list = []
        self.completed = []

    def create_kanban(self, text):
        self.tasks_list.append(Kanban("WO", text))
