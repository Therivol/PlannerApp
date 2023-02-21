import calendar


class Entry:
    def __init__(self, title, description, date, priority, entry_type):
        self.title = title
        self.description = description
        self.priority = priority
        self.date = date
        self.entry_type = entry_type

    def set_title(self, title):
        self.title = title

    def set_description(self, description):
        self.description = description

    def set_date(self, date):
        self.date = date

    def set_entry_type(self, entry_type):
        self.entry_type = entry_type
