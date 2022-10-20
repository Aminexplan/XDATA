from flask import Flask, jsonify, request, session, redirect
from passlib.hash import pbkdf2_sha256
from app import db
import sys


import uuid

class User:

  def start_session(self, user):
    del user['password']
    session['logged_in'] = True
    session['user'] = user
    print('USER : ', user , file=sys.stderr)
    return jsonify(user), 200

  def signup(self):
    print(request.form)

    # Create the user object
    user = {
      "_id": uuid.uuid4().hex,
      "fullname": request.form.get('fullname'),
      "email": request.form.get('email'),
      "password": request.form.get('password'),
      "postaladress": request.form.get('postaladress'),
      "phonenumber": request.form.get('phonenumber'),
      "commercialservice": request.form.get('commercialservice'),
      "technicalservice": request.form.get('technicalservice')
    }


    # Encrypt the password
    user['password'] = pbkdf2_sha256.encrypt(user['password'])

    # Check for existing email address
    if db.users.find_one({ "email": user['email'] }):
      return jsonify({ "error": "Email address already in use" }), 400

    if db.users.insert_one(user):
      return self.start_session(user)

    return jsonify({ "error": "Signup failed" }), 400
  
  def signout(self):
    session.clear()
    return redirect('/')
  
  def login(self):

    user = db.users.find_one({
      "email": request.form.get('email')
    })

    if user and pbkdf2_sha256.verify(request.form.get('password'), user['password']):
      return self.start_session(user)
    
    return jsonify({ "error": "Invalid login credentials" }), 401