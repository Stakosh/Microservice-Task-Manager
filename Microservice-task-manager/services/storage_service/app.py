from flask import Flask, request, jsonify
import os
import json

app = Flask(__name__)
TASKS_FILE = 'tasks.json'

@app.route('/')
def home():
    return "Storage Service activo", 200

@app.route('/storage/tasks', methods=['GET'])
def get_tasks():
    try:
        if not os.path.exists(TASKS_FILE):
            return jsonify([]), 200
        with open(TASKS_FILE, 'r', encoding='utf-8') as f:
            tasks = json.load(f)
        return jsonify(tasks), 200
    except Exception as e:
        return jsonify({"error": f"No se pudieron obtener las tareas: {str(e)}"}), 500

@app.route('/storage/tasks', methods=['POST'])
def save_tasks():
    try:
        tasks = request.get_json(force=True)
        with open(TASKS_FILE, 'w', encoding='utf-8') as f:
            json.dump(tasks, f, indent=2, ensure_ascii=False)
        return jsonify({"message": "Tareas guardadas"}), 200
    except Exception as e:
        return jsonify({"error": f"No se pudieron guardar las tareas: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(port=5002)
