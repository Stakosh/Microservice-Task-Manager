from flask import Flask, request, jsonify
import requests

app = Flask(__name__)
STORAGE_URL = 'http://localhost:5002'
LOGGING_URL = 'http://localhost:5003'

@app.route('/', methods=['GET'])
def index():
    return 'Task Service is running'

@app.route('/tasks', methods=['GET'])
def list_tasks():
    resp = requests.get(f'{STORAGE_URL}/storage/tasks')
    return jsonify(resp.json()), resp.status_code

@app.route('/tasks', methods=['POST'])
def create_task():
    task = request.get_json(force=True)
    resp = requests.get(f'{STORAGE_URL}/storage/tasks')
    tasks = resp.json()
    new_task = {'id': len(tasks), 'title': task.get('title'), 'completed': False}
    tasks.append(new_task)
    requests.post(f'{STORAGE_URL}/storage/tasks', json=tasks)
    requests.post(f'{LOGGING_URL}/log', json={'event': f"Tarea creada: {new_task['title']}"})
    return jsonify(new_task), 201

@app.route('/tasks/<int:task_id>/complete', methods=['PUT'])
def complete_task(task_id):
    resp = requests.get(f'{STORAGE_URL}/storage/tasks')
    tasks = resp.json()
    if task_id < 0 or task_id >= len(tasks):
        return jsonify({'error': 'Invalid task ID'}), 400
    tasks[task_id]['completed'] = True
    requests.post(f'{STORAGE_URL}/storage/tasks', json=tasks)
    requests.post(f'{LOGGING_URL}/log', json={'event': f"Tarea completada: {tasks[task_id]['title']}"})
    return jsonify(tasks[task_id])

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    resp = requests.get(f'{STORAGE_URL}/storage/tasks')
    tasks = resp.json()
    if task_id < 0 or task_id >= len(tasks):
        return jsonify({'error': 'Invalid task ID'}), 400
    removed = tasks.pop(task_id)
    for idx, t in enumerate(tasks):
        t['id'] = idx
    requests.post(f'{STORAGE_URL}/storage/tasks', json=tasks)
    requests.post(f'{LOGGING_URL}/log', json={'event': f"Tarea eliminada: {removed['title']}"})
    return jsonify({'message': 'Task deleted'}), 200

if __name__ == '__main__':
    app.run(port=5001)