from sqlalchemy.orm import relationship
from init import db
from app.config.databaseConfig import base
from flask.ext.sqlalchemy import SQLAlchemy


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

