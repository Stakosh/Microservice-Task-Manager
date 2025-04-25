from flask import Flask, request, jsonify, render_template
import requests

LOGGING_SERVICE_URL = "http://localhost:5003/log"
TASK_SERVICE_URL = "http://localhost:5001"

def log_event(message):
    try:
        requests.post(LOGGING_SERVICE_URL, json={"message": f"[Client] {message}"})
    except:
        print(" No se pudo registrar log desde client")

# Agrega el parámetro 'template_folder'
app = Flask(__name__, template_folder='templates')

@app.route('/')
def home():
    # Renderiza index.html desde la carpeta templates
    return render_template("index.html")

@app.route('/tasks', methods=['GET'])
def list_tasks():
    res = requests.get(f"{TASK_SERVICE_URL}/tasks")
    return jsonify(res.json())

@app.route('/tasks', methods=['POST'])
def create_task():
    task_data = request.json
    log_event(f"Intento de creación de tarea: {task_data}")
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
