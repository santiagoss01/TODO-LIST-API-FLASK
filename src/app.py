from flask import Flask
from flask import Flask, jsonify
from flask import request

app = Flask(__name__)

todos = [
     { "label": "My first task", "done": False },
     { "label": "My second task", "done": False },
     
   ]

@app.route('/todos', methods=['GET'])
def hello_world():
    json_todos = jsonify(todos)
    return json_todos


@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    print("Incoming request with the following body", request_body)
    todos.append(request_body)
    return jsonify(todos)


@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("Incoming request with the following body", position)
    todos.pop(position -1)
    return jsonify(todos)







# These two lines should always be at the end of your app.py file.
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)