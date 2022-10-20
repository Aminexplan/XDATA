from flask import Flask

from app import app
from model.Client import Client
from model.User import User

@app.route('/client/signup', methods=['POST'])
def signup():
  return Client().signup()

@app.route('/client/signout')
def signout():
  return Client().signout()

@app.route('/client/login', methods=['POST'])
def login():
  return Client().login()
  

@app.route('/user/login', methods=['POST'])
def userLogin():
  return User().login()

@app.route('/user/signout')
def userSignout():
  return User().signout()

