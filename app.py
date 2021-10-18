from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_marshmallow import Marshmallow

app = Flask(__name__)
cors = CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    done = db.Column(db.String(5), nullable=False)

    def __init__(self, title, description, done):
        self.title = title
        self.description = description
        self.done = done


class TodoSchema(ma.Schema):
    class Meta:
        fields = ['id', 'title', 'description', 'done']


todo_Schema = TodoSchema()
todos_Schema = TodoSchema(many=True)


""" Welcome Api Rest """
@app.route('/', methods=['GET'])
def index():
    return jsonify({
        "message": "Welcome to my API!!"
    })



""" Get all tasks """
@app.route('/todos', methods=['GET'])
def getTodos():
    allTodos = Todo.query.all()
    results = todos_Schema.dump(allTodos)
    return jsonify(results)


""" Create task """
@app.route('/create', methods=['POST'])
def createTodo():
    title = request.json['title']
    description = request.json['description']
    done = request.json['done']
    new_todo = Todo(title, description, done)
    db.session.add(new_todo)
    db.session.commit()
    result = todo_Schema.jsonify(new_todo)
    return result


""" Get single task """
@app.route('/todo/<id>', methods=['GET'])
def getTodo(id):
  todo = Todo.query.get(id)
  result = todo_Schema.jsonify(todo)
  return result



""" Edit task """
@app.route('/edit/<id>', methods=['PUT'])
def editTodo(id):
    edit_todo =  Todo.query.get(id)
    title = request.json['title']
    description = request.json['description']
    done = request.json['done']
    edit_todo.title = title
    edit_todo.description = description
    edit_todo.done = done
    db.session.commit()
    result = todo_Schema.jsonify(edit_todo)
    return result



""" Delete task """
@app.route('/delete/<id>', methods=['DELETE'])
def deleteTodo(id):
    delete_todo =  Todo.query.get(id)
    db.session.delete(delete_todo)
    db.session.commit()
    result = todo_Schema.jsonify(delete_todo)
    return result



if __name__ == '__main__':
    app.run(debug=True)