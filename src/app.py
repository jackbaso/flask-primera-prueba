from flask import Flask, jsonify, request
import json
app = Flask(__name__)

todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]

@app.route('/todos', methods=['GET'])
def hello_world():
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_todo = json.loads(request.data)
    todos.append(request_todo)
    return jsonify(todos), 200

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    if (position >= len(todos)):
       return 'Posición no existe', 400
    if (position < 0):
        return 'La posición no puede ser menor a cero', 400
    todos.pop(position)
    return jsonify(todos), 200

#arranque de la App
# These two lines should always be at the end of your app.py file.
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)