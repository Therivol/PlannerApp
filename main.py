import datetime

import Constants
from Calendar import Calendar
from Entry import Entry

if __name__ == "__main__":
    calendar = Calendar()
    calendar.add_entry(
        Entry("Volleyball", "", datetime.datetime(2023, 2, 21, 19), Constants.HIGH_PRIORITY, Constants.EVENT))
    calendar.add_entry(
        Entry("Other", "", datetime.datetime(2023, 2, 21, 17), Constants.HIGH_PRIORITY, Constants.TASK))

    print(calendar.query_by_date(datetime.datetime(2023, 2, 21, 19)))

    for entry in calendar.entries:
        print(entry.title)
