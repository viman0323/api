#!flask/bin/python
# -*- coding: utf-8 -*-

from flask import Flask, jsonify
from flask import abort
from flask import make_response
from flask import request
from flask.ext.sqlalchemy import SQLAlchemy
import config
import MySQLdb


dbUrl = "mysql://api:EXhW5FU8zhoM@127.0.0.1:3306/api?charset=utf8"

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = dbUrl
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

db = SQLAlchemy(app)

## Model
class UserModel(db.Model):

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(20), nullable=False)
    age = db.Column(db.Integer, nullable=False)

    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age

    def __repr__(self):
        return '' %(self.id, self.name)

db.create_all()

## 接受post请求数据并写如数据库
@app.route('/api/v1.0/addUser', methods=['POST'])
def AddUser():
    if not request.json:
        abort(400)
    user = {
        'id': request.json['id'],
        'name': request.json['name'],
        'age': request.json['age']
    }

    ## 初始化对象
    initUser = UserModel(int(user['id']), user['name'], int(user['age']))

    ## 插入数据库
    db.session.add(initUser)

    ## 递交修改
    db.session.commit()

    return "Add User Success.\n"

## 获取数据
@app.route('/api/v1.0/getUserInfo', methods=['GET'])
def GetUserInfo():
    if not  request.args['id']:
        ## 不带id的请求为非法请求
        abort(400)
    get_id = request.args['id']
    ## 获取表数据
    result = UserModel.query.all()
    ## 使用filter找到指定项目
    get = UserModel.query.filter_by(id = get_id).first()
    ## 获取成员属性
    resultUser = [
        {
            'id': get.id,
            'name': get.name,
            'age': get.age
        }
    ]

    return jsonify({'UserInfo': resultUser}),201

if __name__ == '__main__':
    app.run(debug=True)
