"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, send_file
from FlaskWebProject import app,nec,mit
from io import BytesIO

@app.route('/nec/ical')
def nec_ical():
    """Renders the nec calendar."""
    return send_file(BytesIO(nec.get_cal()), mimetype='text/calendar', as_attachment=True,attachment_filename='ical-event-nec.ics')

@app.route('/mit/ical')
def mit_ical():
    """Renders the MIT calendar."""
    return send_file(BytesIO(mit.get_cal()), mimetype='text/calendar', as_attachment=True,attachment_filename='ical-event-mit.ics')
@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Rococal',
        year=datetime.now().year,
    )

