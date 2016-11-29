from sqlalchemy.orm import relationship
from init import db
from app.config.databaseConfig import base
from flask.ext.sqlalchemy import SQLAlchemy

class CurrentValues(base):
    __tablename__ = 'current_values'
    id = db.Column('id', db.INTEGER, primary_key=  True)
    temperature = db.Column('temperature', db.FLOAT, nullable = False)
    humidity = db.Column('humidity', db.FLOAT, nullable = False)
    pressure = db.Column('pressure', db.FLOAT, nullable = False )
    history = relationship("HistoricalValues", uselist = False, back_populates = "current")

    def __init__(self,temp,hum,press):
        self.temperature = temp
        self.humidity = hum
        self.pressure = press

    def get_temperature(self):
        return self.temperature

    def get_humidity(self):
        return self.humidity

    def get_pressure(self):
        return self.pressure

    def to_json(self):
        return {'Current values' : {'temperature' : self.temperature, 'humidity' : self.humidity, 'pressure' : self.pressure}}

    def __repr__(self):
        return '<Current value id %r>' % self.id
