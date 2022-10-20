from flask import Flask, jsonify, request, session, redirect
from passlib.hash import pbkdf2_sha256
from datetime import datetime
from app import db
import uuid


class Client:


  def start_session(self, client):
    del client['password']
    session['logged_in'] = True
    session['client'] = client
    return jsonify(client), 200

  def signup(self):
    print(request.form)
    date = datetime.now()
    # Create the client object
    client = {
      "_id": uuid.uuid4().hex,
      "fullname": request.form.get('fullname'),
      "email": request.form.get('email'),
      "password": request.form.get('password'),
      "postaladress": request.form.get('postaladress'),
      "phonenumber": request.form.get('phonenumber'),
      "commercialservice": request.form.get('commercialservice'),
      "technicalservice": request.form.get('technicalservice'),
      "timestamp" : datetime.now()

    }


    # Encrypt the password
    client['password'] = pbkdf2_sha256.encrypt(client['password'])

    # Check for existing email address
    if db.clients.find_one({ "email": client['email'] }):
      return jsonify({ "error": "Email address already in use" }), 400

    if db.clients.insert_one(client):
      return self.start_session(client)

    return jsonify({ "error": "Signup failed" }), 400
  
  def signout(self):
    session.clear()
    return redirect('/')
  
  def login(self):

    client = db.clients.find_one({
      "email": request.form.get('email')
    })
    user = db.users.find_one({
      "email": request.form.get('email')
    })


    if client and pbkdf2_sha256.verify(request.form.get('password'), client['password']):
      return self.start_session(client)

    if user and pbkdf2_sha256.verify(request.form.get('password'), user['password']):
      return self.start_session(user)
    
    
    
    return jsonify({ "error": "Invalid login credentials" }), 401