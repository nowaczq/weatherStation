import flask
from flask_sqlalchemy import SQLAlchemy
import thread


app = flask.Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///mydb'


@app.route('/')
def hello_world():
    return 'Hello World!'

db = SQLAlchemy(app)

if __name__ == '__main__':
    from app.job.sensorData import SensorData
    thread.start_new_thread(SensorData().insert_data_to_db_timestamp,(5,))
    app.run(debug=True, host='0.0.0.0')

