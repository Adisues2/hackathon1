from flask import Flask
from flask import render_template, url_for, redirect, flash, session, logging, request
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, PasswordField, BooleanField, SubmitField, validators
from wtforms.validators import DataRequired, email
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import psycopg2

from app.forms import LoginForm
from app.models import profile, User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'

app.config[
    'SQLALCHEMY_DATABASE_URI'] = f'postgresql://postgres:12345@localhost/hackathon'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['DEBUG'] = True
# Database Representation
db = SQLAlchemy(app)
migrate = Migrate(app, db)


# class LoginForm(FlaskForm):
#     username = StringField('Username', validators=[DataRequired()])
#     password = IntegerField('Password', validators=[DataRequired()])


class ContactForm(FlaskForm):
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('email ', [validators.Length(min=6, max=35)])
    password = StringField('password', [validators.Length(min=3, max=10)])


@app.route('/')
def hello():
    return render_template('home.html')


@app.route('/about')
def about():
    form = LoginForm
    return render_template('layout.html', form=form)


@app.route('/contact', methods=['GET', 'POST'])
def register():
    form = ContactForm()
    if request.method == 'POST':
        username = request.form['username']
        email= request.form['email']
        password = request.form['password']
        # return '<h1>' + username + " " + email + " " + password + '</h1>'
        #  check username
        users = User.query.filter_by(username=username).first()
        if users:
            return 'someone has been login'
        user = User(username=username, email=email, password=password)
        db.session.add(user)
        db.session.commit()
        return 'inserted'
    return render_template('new.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login_page():
    form = LoginForm()
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # return '<h1>' + username + " " + email + " " + password + '</h1>'
        #  check username
        users = User.query.filter_by(username=username).first()
        if users:
            return 'someone has been login'
        new_object = profile(username=username, password=password)
        db.session.add(new_object)
        db.session.commit()
        return '<h2> new user created<h2>'
    return render_template('login.html', form=form)


@app.route('/home')
def page():
    return render_template('register.html')


if __name__ == "__main__":
    app.run(debug=True, port=8080)
