from sqlalchemy.orm import relationship
from init import db
from app.config.databaseConfig import base
from flask.ext.sqlalchemy import SQLAlchemy

class StatisticValues(base):
    __tablename__ = 'statistic_values'
    id = db.Column('id', db.INTEGER, primary_key = True)
    periodStart = db.Column('period_start', db.TIMESTAMP, nullable = False)
    periodStop = db.Column('period_stop', db.TIMESTAMP, nullable = False)
    idTempStats = db.Column('id_temp_stats', db.INTEGER, db.ForeignKey('TemperatureStats.id'))
    idHumStats = db.Column('id_hum_stats', db.INTEGER, db.ForeignKey('HumidityStats.id'))
    idPressStats = db.Column('id_press_stats', db.INTEGER, db.ForeignKey('PressureStats.id'))
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

