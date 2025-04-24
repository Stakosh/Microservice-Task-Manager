from flask import Flask, request, jsonify
import json, os

app = Flask(__name__)
DATA_FILE = 'tasks.json'

@app.route('/', methods=['GET'])
def index():
    return 'Storage Service is running'

@app.route('/storage/tasks', methods=['GET'])
def get_tasks():
    # Asegura que el archivo exista
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'w') as f:
            json.dump([], f)
    with open(DATA_FILE, 'r') as f:
        tasks = json.load(f)
    return jsonify(tasks)

@app.route('/storage/tasks', methods=['POST'])
def save_tasks():
    tasks = request.get_json(force=True)
    with open(DATA_FILE, 'w') as f:
        json.dump(tasks, f)
    return jsonify({'message': 'Tasks saved'}), 201

if __name__ == '__main__':
    app.run(port=5002)