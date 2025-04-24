from flask import Flask, request, jsonify
import requests

LOGGING_SERVICE_URL = "http://localhost:5003/log"

def log_event(message):
    try:
        requests.post(LOGGING_SERVICE_URL, json={"message": f"[Client] {message}"})
    except:
        print("⚠️ No se pudo registrar log desde client")

app = Flask(__name__)
TASK_SERVICE_URL = "http://localhost:5001"

@app.route('/')
def home():
    return "Bienvenido al Client del Microservicio"

@app.route('/tasks', methods=['GET'])
def list_tasks():
    res = requests.get(f"{TASK_SERVICE_URL}/tasks")
    return jsonify(res.json())

@app.route('/tasks', methods=['POST'])
def create_task():
    task_data = request.json
    res = requests.post(f"{TASK_SERVICE_URL}/tasks", json=task_data)
    return jsonify(res.json())

@app.route('/tasks/<int:task_id>/complete', methods=['PUT'])
def complete_task(task_id):
    res = requests.put(f"{TASK_SERVICE_URL}/tasks/{task_id}/complete")
    return jsonify(res.json())

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    res = requests.delete(f"{TASK_SERVICE_URL}/tasks/{task_id}")
    return jsonify(res.json())

if __name__ == "__main__":
    app.run(port=5000)
