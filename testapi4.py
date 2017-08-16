#!flask/bin/python
# -*- coding: utf-8 -*-

from flask import Flask, jsonify
from flask import abort
from flask import make_response
from flask import request
from flask.ext.httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()
app = Flask(__name__)


tasks = [
    {
	'id':1,
	'title':u'Bu groceries',
	'description':u'Milk, Cheese, Pizza, Fruit, Tyleon',
	'done': False
    },
    {
	'id':2,
	'title':u'Leran Python',
	'title':u'Need to find a good Python tutorial on the web',
	'done': False,
    }
]

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@auth.get_password
def get_password(username):
    if username == 'viman':
        return '12345'
    return None

@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Unauthorized access'}), 401)

## 通过id获取数据
@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['GET'])
def get_tasks(task_id):
    task = filter(lambda t: t['id'] == task_id, tasks)
    if len(task) == 0:
        abort(404)
    return jsonify({'task': task[0]})

## 获取全部数据
@app.route('/todo/api/v1.0/tasks', methods=['GET'])
@auth.login_required
def get_tasks_all():
    #return jsonify({'tasks': tasks})
    return jsonify({'tasks': tasks})

## Http Post
@app.route('/todo/api/v1.0/tasks', methods=['POST'])
def create_task():
    if not request.json or not 'title' in request.json:
        abort(400)
    task = [
	{
		'id': tasks[-1]['id'] + 1,
		'title':request.json['title'],
		'description': request.json.get('description', ""),
		'done': False
	}
	   ]

    tasks.append(task)
    return jsonify({'task': task}),201


if __name__ == '__main__':
    app.run(debug=True)
