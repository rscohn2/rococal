import unittest
import requests
import datetime
from bs4 import BeautifulSoup
from ical import rCal, rcal_config

necURL = 'http://necmusic.edu'
calURL = necURL + '/calendar_event'

def get_links(s):
    events = s.find_all('td', 'list-event')
    links = []
    summaries = []
    for e in events:
        links.append(e.a['href'])
        summaries.append(e.a.text)
    return (links,summaries)

def extract_events(event_date, s):
    starts = s.find_all('td','list-time')
    locations = s.find_all('td', 'list-price')
    descriptions = s.find_all('div', 'list-description')
    (urls, summaries) = get_links(s)
    events = []
    for (start,location,description,url,summary) in zip(starts, locations, descriptions, urls, summaries):
        fullURL = necURL + url
        start_date = datetime.datetime.strptime(start.text, '%I:%M %p')
        start_date = start_date.replace(year=event_date.year, month=event_date.month, day=event_date.day )
        events.append({'start': start_date, 'location': location.text, 'description': description.text + ' ' + fullURL, 'summary': summary})
    return events

def get_item(s, item):
    return s.find_all('td', item)

def get_day_html(date):
    url = calURL + '/' + date.strftime('%Y-%m-%d')
    return requests.get(url).text

def parse_day_html(text):
    return BeautifulSoup(text, 'html.parser')

def get_cal(sample_html=None):
    today = datetime.date.today()
    events = []
    for day_delta in range(rcal_config['days']):
        date = today + datetime.timedelta(days=day_delta)
        if sample_html is None:
            html = get_day_html(date)
        else:
            html = sample_html
        events.extend(extract_events(date, parse_day_html(html)))
    cal = rCal(name='NEC', description='Concerts at New England Conservatory', events=events)
    return cal.to_ical()



class Test(unittest.TestCase):
    sample_day = '''<div class="calendar-events-page-navigation"><div class="backBt"><a href="/calendar_event/2015-10-10">&lt;</a></div><div class="todayDate"><a href="/calendar_event/2015-10-11" class="active">October 11, 2015</a></div><div class="nextBt"><a href="/calendar_event/2015-10-12">&gt;</a></div><br style="clear:both";/></div><h4 class="calendar-events-list-title">Featured events</h4><table class="calendar-events-list-table"><tr>
					<td class="list-time">1:00 PM</td>
					<td class="list-event"><a href="/event/14956">Lluis Claret Cello Masterclass</a><br/><div class="list-description">Acclaimed cellist Lluis Claret leads this evening's masterclass. This masterclass will be live streamed. <a href="/event/14956">more</a></div></td>
					<td class="list-price">Pierce Hall</td>
				</tr><tr>
					<td class="list-time">8:00 PM</td>
					<td class="list-event"><a href="/event/14907">Boston Cello Quartet presents &quot;The Latin Project&quot;</a><br/><div class="list-description">In celebration of their upcoming album, Boston Cello Quartet presents "The Latin Project," a musical journey from Spain to S. America. <a href="/event/14907">more</a></div></td>
					<td class="list-price">NEC's Jordan Hall</td>
				</tr></table><h4 class="calendar-events-list-title">NEC Concerts</h4><table class="calendar-events-list-table"><tr>
					<td class="list-time">12:00 PM</td>
					<td class="list-event"><a href="/event/14825">Maria Currie</a><br/><div class="list-description">B.M. student trumpet recital. <a href="/event/14825">more</a></div></td>
					<td class="list-price">Brown Hall</td>
				</tr></table><br /><br /><p class="list-event">Are you an NEC faculty member or student who is giving a school concert? <a href="mailto:calendarlisting@necmusic.edu">Submit</a> your artist and repertoire information now!</p><p>NEC's FREE concerts do not require a ticket, unless stated in concert listing.
<br />Unreserved seating is available on a first-come, first-served basis.
<br />Doors open 30 minutes prior to the concert's start time.</p>						<br />
						<div style="clear:both"></div>
						<div id="to-top-link"></div>
						<div style="clear:both"></div>
						</div>
'''

    def test_nec_get_cal_from_string(self):
        print(get_cal(sample_html=self.sample_day))

    def test_nec_get_cal(self):
        print(get_cal())

if __name__ == '__main__':
    unittest.main()
