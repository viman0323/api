#!flask/bin/python

from flask import Flask, jsonify
from flask.ext.restful import Api, Resource, reqparse 
from flask import abort, request
from flask import make_response
from passlib.apps import custom_app_context as pwd_context


app = Flask(__name__)
api = Api(app)

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

def not_found():
    return make_response(jsonify({'error': 'Not found'}), 404)

class UserApi(Resource):

    def get(self, id):
        pass

    def post(self, id):
        pass

    def delete(self, id):
        pass

class TaskListApi(Resource):

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('title', type = str, required = True,
            help = 'No task title provided', location = 'json')
        self.reqparse.add_argument('description', type = str, default = "", location = 'json')
        super(TaskListApi, self).__init__()

    def get(self):
        not_found()
        return jsonify({'tasks': tasks})
        #return { 'tasks': tasks }

    def post(self):
        pass

class TaskApi(Resource):

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('title', type = str, location = 'json')
        self.reqparse.add_argument('description', type = str, location = 'json')
        self.reqparse.add_argument('done', type = bool, location = 'json')
        super(TaskApi, self).__init__()

    def get(self, id):
        task = filter(lambda t: t['id'] == id, tasks)
        if len(task) == 0:
            abort(404)
            return jsonify({'task': task[0]})

    def post(self, id):
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

    def delete(self, id):
        pass


api.add_resource(UserApi, '/users/<int:id>', endpoint = 'user')
api.add_resource(TaskListApi, '/todo/api/v1.0/tasks', endpoint = 'tasks')
api.add_resource(TaskApi, '/todo/api/v1.0/tasks/<int:id>', endpoint = 'task')


if __name__ == '__main__':
    app.run(debug=True)