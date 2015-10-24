from icalendar import Calendar,Event
from datetime import datetime
import pytz

class rCal:
    """ Container for the Calendar we will server
    """
    def __init__(self):
        cal = Calendar()
        cal.add('prodid', '-//roco ical exporter//roco.com//')
        cal.add('version', '0.1')
        self.cal = cal

    def to_ical(self):
        return self.cal.to_ical()

    def make_time(self, year, month, day, hour, minute):
        return datetime(year, month, day, hour, minute, tzinfo=pytz.timezone('America/New_York'))

    def add_event(self, summary, start):
        ev = Event()
        ev.add('summary', summary)
        ev.add('dtstart', start)
        self.cal.add_component(ev)

if __name__ == '__main__':
    rcal = rCal()
    rcal.add_event(summary='a new event', start=rcal.make_time(year=2015,month=10,day=1,hour=3,minute=0))
    print(rcal.to_ical())