from app import app
from flask import send_file,request, jsonify
import hashlib
from app.model.databaseOperations import DatabaseOperations
from app.model.mathematicalOperations import MathematicalOperations
from app.model.bashOperations import BashOperations


@app.route("/")
def index():
    return send_file("templates/index.html")


@app.route('/current', methods=['GET','POST'])
def get_current():
    result_list = DatabaseOperations().get_current_stats()
    return jsonify(result = result_list)

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    login = data['email']
    password = hashlib.md5(data['password'].encode()).hexdigest()
    if DatabaseOperations().authenticate_user(login,password):
        return jsonify({"result" : True})
    else:
        return jsonify({"result": False})


@app.route('/history', methods=['GET','POST'])
def get_history():
    data = request.json
    print data
    date_start = data['start']
    date_end = data['end']
    result_list = DatabaseOperations().get_historical_values(date_start, date_end)
    return jsonify(result = result_list)


@app.route('/tempHistory', methods=['GET','POST'])
def get_temp_history():
    data = request.json
    date_start = data['start']
    date_end = data['end']
    result_list = DatabaseOperations().get_historical_temperature(date_start, date_end)
    return jsonify(result = result_list)

@app.route('/humHistory', methods=['GET','POST'])
def get_hum_history():
    data = request.json
    date_start = data['start']
    date_end = data['end']
    result_list = DatabaseOperations().get_historical_humidity(date_start, date_end)
    return jsonify(result=result_list)


@app.route('/pressHistory', methods=['GET','POST'])
def get_press_history():
    data = request.json
    date_start = data['start']
    date_end = data['end']
    result_list = DatabaseOperations().get_historical_pressure(date_start, date_end)
    return jsonify(result=result_list)


@app.route('/tempAvg', methods=['GET','POST'])
def get_avg_temp():
    data = request.json
    date_start = data['start']
    date_end = data['end']
    result_list = MathematicalOperations().temperature_average(date_start,date_end)
    return jsonify(result = result_list)

@app.route('/humAvg', methods=['GET','POST'])
def get_avg_hum():
    data = request.json
    date_start = data['start']
    date_end = data['end']
    result_list = MathematicalOperations().humidity_average(date_start, date_end)
    return jsonify(result = result_list)

@app.route('/pressAvg', methods=['GET','POST'])
def get_avg_press():
    data = request.json
    date_start = data['start']
    date_end = data['end']
    result_list = MathematicalOperations().pressure_average(date_start, date_end)
    return jsonify(result = result_list)

@app.route('/tempMinMax',methods=['GET','POST'])
def get_min_max_temp():
    data = request.json
    date_start = data['start']
    date_end = data['end']
    result_list = MathematicalOperations().temperature_min_max(date_start,date_end)
    return jsonify(result=result_list)


@app.route('/humMinMax',methods=['GET','POST'])
def get_min_max_hum():
    data = request.json
    date_start = data['start']
    date_end = data['end']
    result_list = MathematicalOperations().humidity_min_max(date_start, date_end)
    return jsonify(result=result_list)

@app.route('/pressMinMax',methods=['GET','POST'])
def get_min_max_press():
    data = request.json
    date_start = data['start']
    date_end = data['end']
    result_list = MathematicalOperations().pressure_min_max(date_start, date_end)
    return jsonify(result=result_list)

@app.route('/tempMed',methods=['GET','POST'])
def get_med_temp():
    data = request.json
    date_start = data['start']
    date_end = data['end']
    result_list = MathematicalOperations().temperature_median(date_start, date_end)
    return jsonify(result=result_list)

@app.route('/humMed',methods=['GET','POST'])
def get_med_hum():
    data = request.json
    date_start = data['start']
    date_end = data['end']
    result_list = MathematicalOperations().humidity_median(date_start, date_end)
    return jsonify(result=result_list)

@app.route('/pressMed',methods=['GET','POST'])
def get_med_press():
    data = request.json
    date_start = data['start']
    date_end = data['end']
    result_list = MathematicalOperations().pressure_median(date_start, date_end)
    return jsonify(result=result_list)

@app.route('/tempFullStats',methods=['GET','POST'])
def get_all_temp_stats():
    data = request.json
    date_start = data['start']
    date_end = data['end']
    result_list = []
    result_list.append({'temperatureAvg' : MathematicalOperations().temperature_average(date_start,date_end)[0].get('temperatureAvg'),
                        'temperatureMed' : MathematicalOperations().temperature_median(date_start,date_end)[0].get('temperatureMed'),
                        'minTemp' : MathematicalOperations().temperature_min_max(date_start,date_end)[0].get('minTemp'),
                        'maxTemp' : MathematicalOperations().temperature_min_max(date_start,date_end)[0].get('maxTemp')})
    return jsonify(result=result_list)

@app.route('/humFullStats',methods=['GET','POST'])
def get_all_hum_stats():
    data = request.json
    date_start = data['start']
    date_end = data['end']
    result_list = []
    result_list.append(
        {'humidityAvg': MathematicalOperations().humidity_average(date_start, date_end)[0].get('humidityAvg'),
         'humidityMed': MathematicalOperations().humidity_median(date_start, date_end)[0].get('humidityMed'),
         'minHum': MathematicalOperations().humidity_min_max(date_start, date_end)[0].get('minHum'),
         'maxHum': MathematicalOperations().humidity_min_max(date_start, date_end)[0].get('maxHum')})
    return jsonify(result=result_list)

@app.route('/pressFullStats',methods=['GET','POST'])
def get_all_press_stats():
    data = request.json
    date_start = data['start']
    date_end = data['end']
    result_list = []
    result_list.append(
        {'pressureAvg': MathematicalOperations().pressure_average(date_start, date_end)[0].get('pressureAvg'),
         'pressureMed': MathematicalOperations().pressure_median(date_start, date_end)[0].get('pressureMed'),
         'minPress': MathematicalOperations().pressure_min_max(date_start, date_end)[0].get('minPress'),
         'maxPress': MathematicalOperations().pressure_min_max(date_start, date_end)[0].get('maxPress')})
    return jsonify(result=result_list)


@app.route('/consoleStuff',methods=['GET','POST'])
def get_script_result():
    print 'ala ma kota a kot ma wyjebongo'
    data = request.json
    script = data['script']
    print script
    result_list = BashOperations().do_bash_script(script)
    print result_list
    return jsonify(result=result_list)


