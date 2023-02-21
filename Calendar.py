import datetime


class Calendar:
    def __init__(self):
        self.entries = []

    def add_entry(self, entry):
        self.entries.append(entry)
        self.entries.sort(key=lambda x: x.date.timestamp())

    def remove_entry(self, entry):
        return self.entries.pop(entry.title)

    def clear_entries(self):
        self.entries.clear()

    def query_by_type(self, entry_type):
        return [entry for entry in self.entries if entry.entry_type == entry_type]

    def query_by_title(self, search):
        return [entry for entry in self.entries if search.lower() in entry.title.lower()]

    def query_by_priority(self, priority):
        return [entry for entry in self.entries if entry.priority == priority]

    def query_by_date(self, end_date, start_date=None):

        start = start_date.timestamp() if start_date else 0
        return [entry for entry in self.entries if
                start <= entry.date.timestamp() <= end_date.timestamp()]
