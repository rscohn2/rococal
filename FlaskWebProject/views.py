"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from FlaskWebProject import app
from FlaskWebProject.nec import get_cal as nec_get_cal

@app.route('/api/test')
def test_cal():
    return '''BEGIN:VCALENDAR
PRODID:-//Google Inc//Google Calendar 70.9054//EN
VERSION:2.0
CALSCALE:GREGORIAN
METHOD:PUBLISH
X-WR-CALNAME:test calendar
X-WR-TIMEZONE:America/New_York
X-WR-CALDESC:my test calendar description
BEGIN:VEVENT
DTSTART:20151025T143000Z
DTEND:20151025T153000Z
DTSTAMP:20151025T140749Z
UID:tmfe0nrjslietpapsu7fvt7sc0@google.com
CREATED:20151025T140629Z
DESCRIPTION:description of event\nwhith line feeds
LAST-MODIFIED:20151025T140629Z
LOCATION:location for event
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:title of event
TRANSP:OPAQUE
END:VEVENT
END:VCALENDAR
'''

@app.route('/api/nec')
def nec():
    """Renders the nec calendar."""
    return nec_get_cal()

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page 2',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )
