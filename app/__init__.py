from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import sqlite3
import psycopg2

# Flask Object
app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'

app.config[
    'SQLALCHEMY_DATABASE_URI'] = f'postgresql://postgres:12345@localhost/hackathon'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['DEBUG'] = True
# Database Representation
db = SQLAlchemy(app)
migrate = Migrate(app, db)
db.init_app(app)
from app import models, routes
