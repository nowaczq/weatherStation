from app import app
from flask import Flask,send_file, render_template, flash, redirect, session, url_for, g, request, jsonify
import json
import hashlib
from app.dao.daoObjects import User,HistoricalValues,CurrentValues

@app.route("/")
def index():
    return send_file("templates/index.html")


@app.route('/current', methods=['GET','POST'])
def get_current():
    result_list = []
    current_stats = CurrentValues.query.join(HistoricalValues.current).with_entities(CurrentValues.temperature,
        CurrentValues.humidity, CurrentValues.pressure, HistoricalValues.date).order_by(CurrentValues.id.desc()).first()

    result_list.append({"temperature" : current_stats[0], "humidity" : current_stats[1], "pressure" : current_stats[2], "date" : current_stats[3]})

    return jsonify(result = result_list)

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    login = data['email']
    password = hashlib.md5(data['password'].encode()).hexdigest()
    db_login = User.query.with_entities(User.login).filter_by(login = login).first()
    db_password = User.query.with_entities(User.password).filter_by(login = login).first()
    if login == db_login[0] and password == db_password[0]:
        return jsonify({'result': True})
    else:
        return jsonify({'result': False})


@app.route('/history', methods=['GET','POST'])
def get_history():
    data = request.json
    print data
    date_start = data['start']
    date_end = data['end']
    historical_data = HistoricalValues.query.join(CurrentValues.history).filter(HistoricalValues.date >=  date_start)\
        .filter(HistoricalValues.date <=  date_end)\
        .values(CurrentValues.temperature, CurrentValues.humidity, CurrentValues.pressure, HistoricalValues.date)
    result_list = []

    for temperature, humidity, pressure, date in historical_data:
        result_list.append(
            {"temperature" : temperature, "humidity" : humidity, "pressure" : pressure, "date" : date}
        )

    return jsonify(result = result_list)


@app.route('/tempHistory', methods=['GET','POST'])
def get_temp_history():
    data = request.json
    date_start = data['start']
    date_end = data['end']
    historical_temp_data = HistoricalValues.query.join(CurrentValues.history).filter(HistoricalValues.date >=  date_start)\
        .filter(HistoricalValues.date <=  date_end)\
        .values(CurrentValues.temperature, HistoricalValues.date)

    result_list = []

    for temperature, date in historical_temp_data:
        result_list.append(
            {"temperature" : temperature, "date" : date}
        )

    return jsonify(result = result_list)

@app.route('/humHistory', methods=['GET','POST'])
def get_hum_history():
    data = request.json
    date_start = data['start']
    date_end = data['end']
    historical_hum_data = HistoricalValues.query.join(CurrentValues.history).filter(
        HistoricalValues.date >= date_start) \
        .filter(HistoricalValues.date <= date_end) \
        .values(CurrentValues.humidity, HistoricalValues.date)

    result_list = []

    for humidity, date in historical_hum_data:
        result_list.append(
            {"humidity": humidity, "date": date}
        )

    return jsonify(result=result_list)


@app.route('/pressHistory', methods=['GET','POST'])
def get_press_history():
    data = request.json
    date_start = data['start']
    date_end = data['end']
    historical_press_data = HistoricalValues.query.join(CurrentValues.history).filter(
        HistoricalValues.date >= date_start) \
        .filter(HistoricalValues.date <= date_end) \
        .values(CurrentValues.pressure, HistoricalValues.date)

    result_list = []

    for pressure, date in historical_press_data:
        result_list.append(
            {"pressure": pressure, "date": date}
        )

    return jsonify(result=result_list)