import requests
from bs4 import BeautifulSoup
from ical import rCal

necURL = 'http://necmusic.edu'
calURL = necURL + '/calendar_event'

def get_links(s):
    events = s.find_all('td', 'list-event')
    links = []
    titles = []
    for e in events:
        links.append(e.a['href'])
        titles.append(e.a.text)
    return (links,titles)

def get_events(day):
    return extract_events(parse_day_data(get_day_data(day)))


def extract_events(s):
    times = s.find_all('td','list-time')
    locations = s.find_all('td', 'list-price')
    descriptions = s.find_all('div', 'list-description')
    (links, titles) = get_links(s)
    events = []
    for (time,loc,desc,link,title) in zip(times, locations, descriptions, links, titles):
        events.append({'time': time.text, 'location': loc.text, 'description': desc.text + ' ' + necURL +  link, 'title': title})
    return events

def get_item(s, item):
    return s.find_all('td', item)


def get_day_data(day):
    return requests.get(calURL + '/' + day).text

def parse_day_data(text):
    return BeautifulSoup(text, 'html.parser')

def get_cal():
    rcal = rCal()
    rcal.add_event(summary='a new event', start=rcal.make_time(year=2015,month=10,day=1,hour=3,minute=0))
    return rcal.to_ical()

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

if __name__ == '__main__':
    sample_date = '2015-10-11'
    # get_day('2015-10-11')
    #d = extract_events(parse_day_data(sample_day))
    # d = get_events(sample_date)
    #print(str(d))
    print(get_cal())