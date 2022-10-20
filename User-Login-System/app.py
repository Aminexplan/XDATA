from flask import Flask, render_template, session, redirect,request
from functools import wraps
import pymongo

app = Flask(__name__)
app.secret_key = b'\xcc^\x91\xea\x17-\xd0W\x03\xa7\xf8J0\xac8\xc5'

title = "TODO sample application with Flask and MongoDB"
heading = "TODO Reminder with Flask and MongoDB"

# Database
client = pymongo.MongoClient('localhost', 27017)
db = client.XDATA
clients = db.clients 
projects = db.projects
users = db.users
# Decorators
def login_required(f):
  @wraps(f)
  def wrap(*args, **kwargs):
    if 'logged_in' in session:
      return f(*args, **kwargs)
    else:
      return redirect('/')
  
  return wrap

# Routes
from model import routes
from flask import Flask

@app.route('/')
def home():
  return render_template('home.html')

@app.route('/dashboard/')
@login_required
def dashboard():
  return render_template('dashboard.html')

@app.route('/userdashboard/')
@login_required
def userdashboard():
  return render_template('userdashboard.html')

#CRUD

@app.route("/projects/", methods=['GET'])
def list_projects():
    cursor = projects.find().limit(10)
    return list(cursor)

@app.route("/clients/", methods=['GET'])
def list_clients():
    cursor = clients.find().limit(10)
    return list(cursor)

@app.route("/users/", methods=['GET'])
def list_users():
    cursor = users.find().limit(10)
    return list(cursor)

  