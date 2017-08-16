#!flask/bin/python
# -*- coding: utf-8 -*-

from flask import Flask
import time,uuid
from flask.ext.sqlalchemy import SQLAlchemy
from config import DbConf

##dbUrl = "mysql://api:EXhW5FU8zhoM@192.168.0.166:3306/api?charset=utf8"

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DbConf.MYSQL_INFO
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

db = SQLAlchemy(app)

# User Model
class User(db.Model):
    __tablename__ = 'user'

    id = db.Column('id', db.Integer, primary_key=True)
    username = db.Column('username', db.String(50), nullable=False)
    password = db.Column('password', db.String(30), nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return '<User %r>' % self.username

if __name__ == '__main__':
    db.create_all()