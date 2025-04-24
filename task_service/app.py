from flask import Flask, request, jsonify
import requests
import json

app = Flask(__name__)

LOGGING_URL = "http://localhost:5003/log"

def log_event(msg):
    try:
        requests.post(LOGGING_URL, json={"message": f"[Task Service] {msg}"})
    except:
        print("⚠️ No se pudo registrar log desde task_service")

STORAGE_URL = "http://localhost:5002/storage/tasks"

@app.route('/')
def home():
    return "Task Service activo"

@app.route('/tasks', methods=['GET'])
def get_tasks():
    res = requests.get(STORAGE_URL)
    return jsonify(res.json())

@app.route('/tasks', methods=['POST'])
def create_task():
    new_task = request.json
    tasks = requests.get(STORAGE_URL).json()
    new_task["id"] = len(tasks) + 1
    new_task["completed"] = False
    tasks.append(new_task)
    requests.post(STORAGE_URL, json=tasks)
    requests.post(LOGGING_URL, json={"message": f"Tarea creada: {new_task}"})
    return jsonify(new_task)

@app.route('/tasks/<int:task_id>/complete', methods=['PUT'])
def complete_task(task_id):
    tasks = requests.get(STORAGE_URL).json()
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = True
            requests.post(STORAGE_URL, json=tasks)
            requests.post(LOGGING_URL, json={"message": f"Tarea completada: {task}"})
            return jsonify(task)
    return jsonify({"error": "Tarea no encontrada"}), 404

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    tasks = requests.get(STORAGE_URL).json()
    tasks = [t for t in tasks if t["id"] != task_id]
    requests.post(STORAGE_URL, json=tasks)
    requests.post(LOGGING_URL, json={"message": f"Tarea eliminada: ID {task_id}"})
    return jsonify({"message": "Tarea eliminada"})

if __name__ == "__main__":
    app.run(port=5001)
