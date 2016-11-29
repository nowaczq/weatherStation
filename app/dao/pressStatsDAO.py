from sqlalchemy.orm import relationship
from init import db
from app.config.databaseConfig import base
from flask.ext.sqlalchemy import SQLAlchemy


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