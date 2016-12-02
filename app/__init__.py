import flask
from flask_sqlalchemy import SQLAlchemy

app = flask.Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///mydb'

db = SQLAlchemy(app)

from app.controller import views

app.url_map.strict_slashes = False

