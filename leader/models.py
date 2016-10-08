from flask_sqlalchemy import SQLAlchemy
from api import app
import os
import binascii


app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/micron'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    token = db.Column(db.String(40), unique=True)

    def __init__(self):
        self.token = str(binascii.b2a_hex(os.urandom(20)))

    def __repr__(self):
        return '<User %r>' % self.token

