from icalendar import Calendar,Event
from datetime import datetime
import pytz
import unittest

class rCal:
    """ Container for the Calendar we will server
    """
    debug = True

    def __init__(self, name, description=''):
        cal = Calendar()
        cal.add('prodid', '-//roco ical exporter//roco.com//')
        cal.add('version', '2.0')
        cal.add('calscale','GREGORIAN')
        cal.add('method','PUBLISH')
        cal.add('x-wr-calname', name)
        cal.add('x-original-url','http://cal.roco.com')
        cal.add('x-wr-caldesc', description)
        self.cal = cal

    def to_ical(self, rendered=False):
        cal = self.cal.to_ical()
        if self.debug:
            print cal
        return cal

    def make_time(self, year, month, day, hour, minute):
        return datetime(year, month, day, hour, minute, tzinfo=pytz.timezone('America/New_York'))

    def add_event(self, summary, start):
        ev = Event()
        ev.add('summary', summary)
        ev.add('dtstart', start)
        self.cal.add_component(ev)


class Test(unittest.TestCase):
    def test_ical_render(self):
        rcal = rCal('test calendar')
        rcal.add_event(summary='a new event', start=rcal.make_time(year=2015,month=10,day=1,hour=3,minute=0))
        print(rcal.to_ical())

if __name__ == '__main__':
    unittest.main()

if __name__ == 'aaaa__main__':
    rcal = rCal()
    rcal.add_event(summary='a new event', start=rcal.make_time(year=2015,month=10,day=1,hour=3,minute=0))
    print(rcal.to_ical())