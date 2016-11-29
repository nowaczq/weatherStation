from sqlalchemy.orm import relationship
from init import db
from app.config.databaseConfig import base
from flask.ext.sqlalchemy import SQLAlchemy


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