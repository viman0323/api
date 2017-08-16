#!flask/bin/python
# -*- coding: utf-8 -*

from flask import Flask, request, jsonify
from flask import abort
from model import User
from flask.ext.sqlalchemy import SQLAlchemy
from config import DbConf

app = Flask(__name__)

## Mysql
app.config['SQLALCHEMY_DATABASE_URI'] = DbConf.MYSQL_INFO
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
db = SQLAlchemy(app)


## 用户注册
@app.route('/api/v1.0/addUser', methods=['POST'])
def AddUser():
    if not request.json:
        abort(400)
    user = {
        'username': request.json['username'],
        'password': request.json['password']
    }

    ## 初始化对象
    initUser = User(user['username'], str(user['password']))

    ## 插入数据库
    db.session.add(initUser)

    ## 递交修改
    db.session.commit()

    status = [
        {
            'code':1,
            'message': 'AddUser Success'
        }
    ]
    return jsonify({"result": status}), 201


## 用户登录
@app.route('/api/v1.0/login', methods=['POST'])
def Login():
    if not request.json:
        abort(400)

    username = request.json['username']
    password = request.json['password']

    ## 获取表数据
    result = User.query.all()
    ## 使用filter找到指定项目
    user = User.query.filter_by(username = username).first()
    if not user:
        return jsonify({'code':404, 'message':'This User Not none'})

    if user.password != password:
        return jsonify({'code':400, 'message': 'You input password error'})

    ## 返回成员信息
    resultUser = [
        {
            'code':1,
            'username': user.username,
            'message': 'Login Success'
        }
    ]

    return jsonify({'UserInfo': resultUser}),201


if __name__ == '__main__':
    app.run(debug=True)