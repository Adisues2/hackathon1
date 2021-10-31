import os

from app import app

basedir = os.path.abspath(os.path.dirname(__file__))

# class Config:
# 	SECRET_KEY = "B&E)H@McQeThWmZq"
# 	SQLALCHEMY_DATABASE_URI = 'sqlite:///'+os.path.join(basedir, 'app.db')
# 	SQLALCHEMY_TRACK_MODIFICATIONS = False
app.config['SECRET_KEY'] = 'you-will-never-guess'
