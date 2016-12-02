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
        hectoPascals = humidity / 100
        if temperature and humidity and pressure:
            insertSensorData = CurrentValues(float(temperature),float(hectoPascals),float(pressure))
            db_session.add(insertSensorData)
            db_session.commit()

            idCurrentData = CurrentValues.query.order_by(CurrentValues.id.desc()).first()
            insertHistoricalData = HistoricalValues(datetime.now(),idCurrentData.id)
            db_session.add(insertHistoricalData)
            db_session.commit()



    def insert_data_to_db_timestamp(self,time_stamp):
        s = sched.scheduler(time.time, time.sleep)
        while True:
            s.enter(time_stamp, 1, self.insert_data_to_db, ())
            s.run()


    def __init__(self):
        pass