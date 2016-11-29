from init import db
from app.config.databaseConfig import base



class User(base):
    __tablename__ = 'user'
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
