import unittest
import requests
import datetime
from ical import rCal, rcal_config

def extract_event(ar):
    #for i in range(len(ar)):
        #print(str(i) + ' ' + ar[i])
    e = {}
    event_date = datetime.datetime.strptime(ar[0], '%A %d %B %Y')
    sd = datetime.datetime.strptime(ar[1], '%I:%M %p')
    e['start'] = sd.replace(year=event_date.year, month=event_date.month, day=event_date.day )
    ed = datetime.datetime.strptime(ar[2], '%I:%M %p')
    e['end'] = ed.replace(year=event_date.year, month=event_date.month, day=event_date.day )
    e['summary'] = ar[4]
    d = ar[5]
    if ar[16] != '':
        d += '\nurl: ' + ar[16]
    if ar[12] != '':
        d += '\nprice: ' + ar[12]
    if ar[13] != '':
        d += '\ninvited: ' + ar[13]
    e['description'] = d
    e['location'] = ar[6] + ' ' + ar[7]
    #print(str(e))
    return e

def make_url():
    today = datetime.date.today()
    endDay = today + datetime.timedelta(days=rcal_config['days']-1)
    start = today.strftime('&start.month=%m&start.day=%d&start.year=%Y')
    end = endDay.strftime('&end.month=%m&end.day=%d&end.year=%Y')
    return 'http://events.mit.edu/searchresults-tab.html?fulltext=&andor=and' + start + end

def get_cal(sample_html=None):
    events = []
    text = requests.get(make_url()).text
    lines = text.strip().split('\n')
    for line in lines:
        e = line.split('\t')
        events.append(extract_event(e))
    cal = rCal(name='MIT', description='Events at MIT', events=events)
    return cal.to_ical()

class Test(unittest.TestCase):
    def test_mit_make_url(self):
        print(make_url())
    def test_mit_get_cal(self):
        get_cal()

if __name__ == '__main__':
    unittest.main()
