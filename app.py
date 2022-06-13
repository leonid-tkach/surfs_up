from flask import Flask
import datetime as dt

app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'Hello world'

@app.route('/time')
def what_time_is_it_now():
  return dt.datetime.now().strftime("%H:%M:%S")