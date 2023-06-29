from flask import Flask, render_template, request, redirect, url_for, abort
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from datetime import date, datetime
from sqlalchemy import desc

app = Flask(__name__)
app.app_context().push()
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

# Connect to DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///events.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# DB Class
class Events(db.Model):
    __tablename__ = "events"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=False)
    time = db.Column(db.String)
    date = db.Column(db.String)
    description = db.Column(db.Text, nullable=False)

db.create_all()

# Main home
@app.route('/')
def index():
    today = date.today()
    events = Events.query.order_by(desc(Events.date)).all()
    return render_template('index.html', events=events, today=today)

@app.route('/calendar')
def calendar():
    events = Events.query.all()
    return render_template('calendar.html', events=events)

# Create event
@app.route('/submit/<event_date>', methods=["POST"])
def submit_event(event_date):
    new_event = Events(
        title = request.form['title'],
        time =  request.form['time'],
        description = request.form['description'],
        date = event_date
        )
    db.session.add(new_event)
    db.session.commit()
    
    return redirect(url_for('calendar'))

@app.route('/create')
def create():
    return render_template('create.html')

@app.route('/event-details/<event_id>')
def event_details(event_id):
    event = Events.query.get(event_id)
    # starting time format
    s_time = datetime.strptime( event.time, '%H:%M')
    # date format
    date_list = event.date.split("-")
    d = datetime(int(date_list[0]), int(date_list[1]), int(date_list[2]))
    formatted_date = d.strftime("%b %d")
    s_t_am_pm = s_time.strftime('%I:%M %p')

    return render_template('event_details.html', event=event, s_time=s_t_am_pm, date=formatted_date)


if __name__ == '__main__':
    app.run(debug=True, host='192.168.4.23')