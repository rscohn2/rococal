"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, send_file
from FlaskWebProject import app
from FlaskWebProject.nec import get_cal as nec_get_cal
from io import BytesIO
from os import getcwd

resp = '''BEGIN:VCALENDAR
PRODID:-//ROCO//ROCO Calendar 70.9054//EN
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
UID:tmfe0nrjslietpapsu7fvt7sc0@roco.com
CREATED:20151025T140629Z
DESCRIPTION:description of event
LAST-MODIFIED:20151025T140629Z
LOCATION:location for event
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:title of event
TRANSP:OPAQUE
END:VEVENT
END:VCALENDAR
'''

@app.route('/api/getcwd')
def wd():
    #send_file(BytesIO(resp),attachment_filename='x.ics',as_attachment=True)
    return getcwd()

@app.route('/test/plainfile')
def test_plain():
    return send_file('x.txt')

@app.route('/test/fp')
def test_fp():
    return send_file(BytesIO('abc'),mimetype='text/plain',as_attachment=True,attachment_filename='x.txt')

@app.route('/test/cal')
def test_cal():
    return send_file(BytesIO(resp),mimetype='text/calendar',as_attachment=True,attachment_filename='rocox.ics')

@app.route('/test/harvard')
def test_harvard():
    return send_file('body.txt',mimetype='text/calendar',as_attachment=True,attachment_filename='ical-event-1111122333.ics')

@app.route('/test/harvard2')
def test_harvard2():
    return send_file('body2.txt',mimetype='text/calendar',as_attachment=True,attachment_filename='ical-event-1111122333.ics')

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
