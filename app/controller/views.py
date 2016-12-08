from app import app
from flask import Flask,send_file, render_template, flash, redirect, session, url_for, g, request, jsonify
import json
import hashlib
from app.dao.daoObjects import User

@app.route("/")
def index():
    # print 'ala'
    return send_file("templates/index.html")


# @app.route('/login', methods=['POST'])
# def checkLoginData():
#     data = json.loads(request.data.decode())
#     login = data['email']
#     password = hashlib.md5(data['password'].encode()).hexdigest()
#     print password
#     db_email = User.query.with_entities(User.login).filter_by(login = login).first()
#     db_password = User.query.with_entities(User.password).filter_by(login = login).first()
#     print db_password[0]
#     if login == db_email[0] and password == db_password[0]:
#         return jsonify({'result': True})
#     else:
#         return jsonify({'result': False})


@app.route('/login', methods=['POST'])
def login():
    data = request.json
    login = data['email']
    password = hashlib.md5(data['password'].encode()).hexdigest()
    db_login = User.query.with_entities(User.login).filter_by(login = login).first()
    db_password = User.query.with_entities(User.password).filter_by(login = login).first()
    print password
    print db_password[0]
    if login == db_login[0] and password == db_password[0]:
        # session['logged_in'] = True
        return jsonify({'result': True})
    else:
        return jsonify({'result': False})