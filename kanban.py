class Kanban:
    def __init__(self, kanban_type, text):
        self.kanban_type = kanban_type
        self.text = text

    def __str__(self):
        return str(self.text)

    __repr__ = __str__


class Board:
    def __init__(self, name):
        self.name = name
        self.date_field = []
        self.tasks_list = []
        self.completed = []

    def create_kanban(self, text):
        self.tasks_list.append(Kanban("WO", text))

