from flask import Flask, request, jsonify
import requests
import json
from threading import Thread  # 👈 importante

app = Flask(__name__)

STORAGE_URL = "http://localhost:5002/storage/tasks"
LOGGING_URL = "http://localhost:5003/log"
NOTIF_URL = "http://localhost:5004/notify"

def log_event(msg):
    try:
        requests.post(LOGGING_URL, json={"message": f"[Task Service] {msg}"})
    except Exception as e:
        print(f" No se pudo registrar log en logging_service: {e}")

def notify(msg):
    try:
        requests.post(NOTIF_URL, json={"message": msg}, timeout=1)
    except Exception as e:
        print(f" No se pudo enviar notificación: {e}")

@app.route('/')
def home():
    return "Task Service activo", 200

@app.route('/tasks', methods=['GET'])
def get_tasks():
    try:
        res = requests.get(STORAGE_URL)
        tasks = json.loads(res.text)
        Thread(target=log_event, args=("Listado de tareas",)).start()  # 🔄
        return jsonify(tasks), 200
    except Exception as e:
        Thread(target=log_event, args=(f"Error al obtener tareas: {e}",)).start()
        return jsonify([]), 200

@app.route('/tasks', methods=['POST'])
def create_task():
    try:
        new = request.get_json(force=True)
        res = requests.get(STORAGE_URL)
        tasks = json.loads(res.text)
        new_id = max([t.get("id", 0) for t in tasks] + [0]) + 1
        new["id"] = new_id
        tasks.append(new)
        requests.post(STORAGE_URL, json=tasks)
        Thread(target=log_event, args=(f"Tarea creada: {new}",)).start()
        Thread(target=notify, args=(f"Nueva tarea: {new.get('title', '(sin título)')}",)).start()
        return jsonify(new), 201
    except Exception as e:
        Thread(target=log_event, args=(f"Error al crear tarea: {e}",)).start()
        return jsonify({"error": "No se pudo crear tarea"}), 500


@app.route('/tasks/<int:task_id>/complete', methods=['PUT'])
def complete_task(task_id):
    try:
        res = requests.get(STORAGE_URL)
        tasks = res.json()

        for task in tasks:
            if task.get("id") == task_id:
                task["completed"] = True  
                break
        else:
            return jsonify({"error": "Tarea no encontrada"}), 404

        requests.post(STORAGE_URL, json=tasks)
        Thread(target=log_event, args=(f"Tarea completada: ID {task_id}",)).start()
        Thread(target=notify, args=(f"Tarea completada: ID {task_id}",)).start()
        return jsonify({"message": "Tarea completada"}), 200

    except Exception as e:
        Thread(target=log_event, args=(f"Error al completar tarea: {e}",)).start()
        return jsonify({"error": "No se pudo completar la tarea"}), 500

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    try:
        res = requests.get(STORAGE_URL)
        tasks = json.loads(res.text)
        filtered = [t for t in tasks if t.get("id") != task_id]
        requests.post(STORAGE_URL, json=filtered)
        Thread(target=log_event, args=(f"Tarea eliminada: ID {task_id}",)).start()
        Thread(target=notify, args=(f"Tarea eliminada: ID {task_id}",)).start()
        return jsonify({"message": "Tarea eliminada"}), 200
    except Exception as e:
        Thread(target=log_event, args=(f"Error al eliminar tarea: {e}",)).start()
        return jsonify({"error": "No se pudo eliminar tarea"}), 500

if __name__ == "__main__":
    app.run(port=5001)
