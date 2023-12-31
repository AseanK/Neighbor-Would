from flask import Flask, render_template, request, redirect, url_for, abort
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from datetime import date, datetime
from sqlalchemy import desc
import os

KEY_VAL = os.getenv("key")
MAP_KEY = os.getenv("MAP_KEY")
DATABASE_URL = os.getenv("DB_URL")

app = Flask(__name__)
app.app_context().push()
app.config['SECRET_KEY'] = KEY_VAL
Bootstrap(app)

# Connect to DB
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# DB Class
class Events(db.Model):
    __tablename__ = "events"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=False)
    s_time = db.Column(db.String, nullable=False)
    e_time = db.Column(db.String, nullable=False)
    date = db.Column(db.String)
    e_date = db.Column(db.String, nullable=True)
    description = db.Column(db.Text, nullable=False)
    color = db.Column(db.String, nullable=True)
    address = db.Column(db.String, nullable=False)
    lng = db.Column(db.Float, nullable=False)
    lat = db.Column(db.Float, nullable=False)

db.create_all()


# Date format e.g. Jan 21
def date_format(date):
    d_list = date.split('-')
    d = datetime(int(d_list[0]), int(d_list[1]), int(d_list[2]))
    # First three words of the month and the date
    return d.strftime("%b %d")

# Time format e.g. 4:00PM
def time_format(time):
    t = datetime.strptime(time, '%H:%M')
    return t.strftime('%I:%M %p')

# Date fomat to compare
def d_format(date):
    return datetime.strptime(date, '%Y-%m-%d').date()


# Main home
@app.route('/')
def index():
    today = date.today()
    events = Events.query.order_by(Events.date).all()
    return render_template('index.html', events=events, today=today, tf=time_format, df=date_format, d_f=d_format)

@app.route('/calendar')
def calendar():
    events = Events.query.all()
    return render_template('calendar.html', events=events)

# Create event
@app.route('/submit/<event_date>', methods=["POST"])
def submit_event(event_date):
    new_event = Events(
        title = request.form['title'],
        s_time =  request.form['s_time'],
        e_time =  request.form['e_time'],
        description = request.form['description'],
        date = event_date,
        e_date = request.form['ending_date'],
        color = request.form ['color'],
        address = request.form['address'],
        lng = request.form['longitude'],
        lat = request.form['latitude']
        )
    db.session.add(new_event)
    db.session.commit()
    
    return redirect(url_for('calendar'))

@app.route('/create')
def create():
    return render_template('create.html', MAP_KEY=MAP_KEY)

@app.route('/event-details/<int:event_id>')
def event_details(event_id):
    event = Events.query.get(event_id)
    
    # time format
    s_t_am_pm = time_format(event.s_time)
    e_t_am_pm = time_format(event.e_time)
    
    # staring date format
    formatted_date = date_format(event.date)

    # ending date format
    if event.e_date:
        formatted_e_date = date_format(event.e_date)
    else:
        formatted_e_date = None

    return render_template('event_details.html', event=event, s_time=s_t_am_pm, e_time=e_t_am_pm, date=formatted_date, e_date =formatted_e_date, MAP_KEY=MAP_KEY)

@app.route('/map')
def event_map():
    today = date.today()
    events = Events.query.all()
    return render_template('map.html', events=events, today=today, d_f=d_format, MAP_KEY=MAP_KEY)