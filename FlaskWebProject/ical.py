from icalendar import Calendar,Event
from datetime import datetime
import pytz
import unittest
import hashlib

rcal_config = {'days': 14}

class rCal(Calendar):
    """ Container for the Calendar we will serve
    """
    def __init__(self, name, description, events):
        Calendar.__init__(self)
        self.add('prodid', '-//roco ical exporter//roco.com//')
        self.add('version', '2.0')
        self.add('calscale','GREGORIAN')
        self.add('method','PUBLISH')
        self.add('x-wr-calname', name)
        self.add('x-original-url','http://cal.roco.com')
        self.add('x-wr-caldesc', description)
        for event in events:
            ev = Event()
            self.add_component(ev)
            ev.add('summary', event['summary'])
            ev.add('dtstart', pytz.timezone('America/New_York').localize(event['start']))
            if 'end' in event:
                ev.add('dtend', pytz.timezone('America/New_York').localize(event['end']))
            ev.add('location', event['location'])
            ev.add('description', event['description'])
            ev.add('uid', hashlib.sha224(ev.to_ical(sorted=True)).hexdigest())

class Test(unittest.TestCase):
    def test_ical_synthetic(self):
        events = [{'summary': 'a new event', 'start': datetime(year=2015,month=10,day=1,hour=3,minute=0)}]
        rcal = rCal(name='test calendar', description='test calendar description', events=events)
        print(rcal.to_ical())

if __name__ == '__main__':
    unittest.main()
