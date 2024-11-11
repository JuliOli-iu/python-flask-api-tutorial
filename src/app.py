from flask import Flask, jsonify, request

app = Flask(__name__)

todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]

@app.route('/todos', methods=['GET'])
def hello_world():
    json_text = jsonify(todos)
    return json_text

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json

    if 'label' in request_body and 'done' in request_body:
        todos.append(request_body)
        return jsonify(todos), 200
    else:
        return jsonify({"error": "Invalid todo format"}), 400

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    if position < 0 or position >= len(todos):
        return jsonify({"error": "Position out of range"}), 404  

    todos.pop(position)  
    return jsonify(todos), 200  

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)