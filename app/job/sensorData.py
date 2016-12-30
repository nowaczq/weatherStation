from Adafruit_BME280 import *
from app.config.databaseConfig import db_session
from app.dao.daoObjects import CurrentValues, HistoricalValues
import sched, time
from datetime import datetime

class SensorData():
    sensor = BME280(mode=BME280_OSAMPLE_8)

    def insert_data_to_db(self):
        temperature = self.sensor.read_temperature()
        humidity = self.sensor.read_humidity()
        pressure = self.sensor.read_pressure()
        percent_humidity = humidity / 100
        if temperature and humidity and pressure:
            insert_sensor_data = CurrentValues(float(temperature),float(percent_humidity),float(pressure))
            db_session.add(insert_sensor_data)
            db_session.commit()

            id_current_data = CurrentValues.query.order_by(CurrentValues.id.desc()).first()
            insert_historical_data = HistoricalValues(datetime.now(),id_current_data.id)
            db_session.add(insert_historical_data)
            db_session.commit()



    def insert_data_to_db_timestamp(self,time_stamp):
        s = sched.scheduler(time.time, time.sleep)
        while 1:
            s.enter(time_stamp, 1, self.insert_data_to_db, ())
            s.run()


    def __init__(self):
        pass