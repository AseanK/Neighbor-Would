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
    s_time = db.Column(db.String, nullable=False)
    e_time = db.Column(db.String, nullable=False)
    date = db.Column(db.String)
    e_date = db.Column(db.String, nullable=True)
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
        s_time =  request.form['s_time'],
        e_time =  request.form['e_time'],
        description = request.form['description'],
        date = event_date,
        e_date = request.form['ending_date']
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
    # time format
    s_time = datetime.strptime( event.s_time, '%H:%M')
    e_time = datetime.strptime( event.e_time, '%H:%M')
    s_t_am_pm = s_time.strftime('%I:%M %p')
    e_t_am_pm = e_time.strftime('%I:%M %p')
    # date format
    date_list = event.date.split("-")
    d = datetime(int(date_list[0]), int(date_list[1]), int(date_list[2]))
    formatted_date = d.strftime("%b %d")

    if event.e_date:
        e_date_list = event.e_date.split("-")
        e_d = datetime(int(e_date_list[0]), int(e_date_list[1]), int(e_date_list[2]))
        formatted_e_date = e_d.strftime("%b %d")
    else:
        formatted_e_date = None

    return render_template('event_details.html', event=event, s_time=s_t_am_pm, e_time=e_t_am_pm, date=formatted_date, e_date =formatted_e_date)


if __name__ == '__main__':
    app.run(debug=True)