from app import db


class profile(db.Model):
    __tablename__ = "profiles"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True)
    password = db.Column(db.String(10), unique=True)

    def __repr__(self):
        return f'<profile: {self.username}>'


class       User(db.Model):
    __tablename__ = "students"
    user_id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(50), unique=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(50), unique=True)


class new_data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True)

    password = db.Column(db.String(10), unique=True)

    def __repr__(self):
        return f'<username: {self.username}>'
