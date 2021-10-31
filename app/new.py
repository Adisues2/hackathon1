# from flask import Flask, request, render_template, url_for
#
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
# import psycopg2
#
# app = Flask(__name__)
#
# app.config[
#     'SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:12345@localhost/hackathon'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#
# app.config['DEBUG'] = True
# db = SQLAlchemy(app)
#
#
# class User(db.Model):
#     __tablename__ = "students"
#     user_id = db.Column(db.Integer(), primary_key=True)
#     username = db.Column(db.String(50), unique=True)
#     email = db.Column(db.String(50), unique=True)
#     password = db.Column(db.String(50), unique=True)
#
#
# @app.route('/')
# def index():
#     return render_template('index.html')
#
#
# @app.route('/submit', methods=['GET', 'POST'])
# def register():
#     if request.method == 'POST':
#         username = request.form['username']
#         email = request.form['email']
#         password = request.form['password']
#         users = User(username, email, password)
#         db.session.add(users)
#         db.session.commit()
#         # if request.method == 'GET':
#         Results = db.session.query().filter_by().all
#         for result in Results:
#             print(result.email)
#         return 'inserted data'
#     return render_template('new.html',data = email)
#
#
# if __name__ == '__main__':
#     app.run(debug=True)
