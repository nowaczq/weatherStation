from sqlalchemy.orm import relationship
from app.config.databaseConfig import base
from app import db

class User(base):
    __tablename__ = 'user_info'
    id = db.Column('id', db.INTEGER, primary_key=True)
    login = db.Column('login', db.VARCHAR(50), nullable=False)
    password = db.Column('password', db.VARCHAR(50), nullable=False)

    def __init__(self, login):
        self.login = login

    def get_login(self):
        return self.login

    def to_json(self):
        return {'User': {'id': self.id, 'login': self.login}}

    def __repr__(self):
        return '<User: %r>' % (self.login)


class HistoricalValues(base):
    __tablename__ = 'historical_values'
    id = db.Column('id', db.INTEGER, primary_key = True)
    date = db.Column('date', db.TIMESTAMP, nullable = False)
    idCurrentVal = db.Column('id_current_val', db.INTEGER, db.ForeignKey('current_values.id'))
    current = relationship('CurrentValues', back_populates = 'history')

    def __init__(self,date,idCurrent):
        self.date = date
        self.idCurrentVal = idCurrent

    def get_date(self):
        return self.date

    def get_tablename(self):
        return self.__tablename__

    def get_current(self):
        return self.current

    def to_json(self):
        return {'Historical values' : {'id' : self.id , 'date' : self.date, 'id_current_val' : self.idCurrentVal}}

    def __repr__(self):
        return '<Date %r>' % self.date


class CurrentValues(base):
    __tablename__ = 'current_values'
    id = db.Column('id', db.INTEGER, primary_key=  True)
    temperature = db.Column('temperature', db.FLOAT, nullable = False)
    humidity = db.Column('humidity', db.FLOAT, nullable = False)
    pressure = db.Column('pressure', db.FLOAT, nullable = False )
    history = relationship('HistoricalValues', uselist = False, back_populates = 'current')

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

    def get_tablename(self):
        return self.__tablename__

    def get_history(self):
        return self.history

    def to_json(self):
        return {'Current values' : {'temperature' : self.temperature, 'humidity' : self.humidity, 'pressure' : self.pressure}}

    def __repr__(self):
        return '<Current value id %r>' % self.id

class TemperatureStats(base):
    __tablename__ = 'temp_stats'
    id = db.Column('id', db.INTEGER, primary_key = True)
    minTemp = db.Column('min_temp', db.FLOAT, nullable = False)
    maxTemp = db.Column('max_temp', db.FLOAT, nullable = False)
    avgTemp = db.Column('avg_temp', db.FLOAT, nullable = False)
    statsTemp = relationship("StatisticValues", uselist = False, back_populates = "tempStats")

    def __init__(self,minTemp,maxTemp,avgTemp):
        self.minTemp = minTemp
        self.maxTemp = maxTemp
        self.avgTemp = avgTemp

    def get_min(self):
        return self.minTemp

    def get_max(self):
        return self.maxTemp

    def get_avg(self):
        return self.avgTemp

    def to_json(self):
        return {'Temperature stats' : {'minimal' : self.minTemp , 'maximal' : self.maxTemp, 'average' : self.avgTemp}}

    def __repr__(self):
        return '<Min temp %r>' % self.minTemp

class PressureStats(base):
    __tablename__ = 'press_stats'
    id = db.Column('id', db.INTEGER, primary_key=True)
    minPress = db.Column('min_press', db.FLOAT, nullable=False)
    maxPress = db.Column('max_press', db.FLOAT, nullable=False)
    avgPress = db.Column('avg_press', db.FLOAT, nullable=False)
    statsPress = relationship("StatisticValues", uselist = False, back_populates="pressStats")

    def __init__(self, minPress, maxPress, avgPress):
        self.minPress = minPress
        self.maxPress = maxPress
        self.avgPress = avgPress

    def get_min(self):
        return self.minPress

    def get_max(self):
        return self.maxPress

    def get_avg(self):
        return self.avgPress

    def to_json(self):
        return {'Pressure stats': {'minimal': self.minPress, 'maximal': self.maxPress, 'average': self.avgPress}}

    def __repr__(self):
        return '<Min hum %r>' % self.minPress

class HumidityStats(base):
    __tablename__ = 'hum_stats'
    id = db.Column('id', db.INTEGER, primary_key=True)
    minHum = db.Column('min_hum', db.FLOAT, nullable=False)
    maxHum = db.Column('max_hum', db.FLOAT, nullable=False)
    avgHum = db.Column('avg_hum', db.FLOAT, nullable=False)
    statsHum = relationship("StatisticValues", uselist = False, back_populates="humStats")

    def __init__(self, minHum, maxHum, avgHum):
        self.minHum = minHum
        self.maxHum = maxHum
        self.avgHum = avgHum

    def get_min(self):
        return self.minHum

    def get_max(self):
        return self.maxHum

    def get_avg(self):
        return self.avgHum

    def to_json(self):
        return {'Humidity stats': {'minimal': self.minHum, 'maximal': self.maxHum, 'average': self.avgHum}}

    def __repr__(self):
        return '<Min hum %r>' % self.minHum

class StatisticValues(base):
    __tablename__ = 'statistic_values'
    id = db.Column('id', db.INTEGER, primary_key = True)
    periodStart = db.Column('period_start', db.TIMESTAMP, nullable = False)
    periodStop = db.Column('period_stop', db.TIMESTAMP, nullable = False)
    idTempStats = db.Column('id_temp_stats', db.INTEGER, db.ForeignKey('temp_stats.id'))
    idHumStats = db.Column('id_hum_stats', db.INTEGER, db.ForeignKey('hum_stats.id'))
    idPressStats = db.Column('id_press_stats', db.INTEGER, db.ForeignKey('press_stats.id'))
    tempStats = relationship("TemperatureStats", back_populates = "statsTemp")
    humStats = relationship("HumidityStats", back_populates = "statsHum")
    pressStats = relationship("PressureStats", back_populates = "statsPress")

    def __init__(self,start,stop):
        self.periodStart = start
        self.periodStop = stop

    def get_start(self):
        return self.periodStart

    def get_stop(self):
        return self.periodStop

    def to_json(self):
        return {'Statistic values' : {'period start' : self.periodStart , 'period stop' : self.periodStop ,
                                      'id temp' : self.idTempStats , 'id hum' : self.idHumStats,
                                      'press id' : self.idPressStats}}

    def __repr__(self):
        return '<Period start %r>' % self.periodStart
