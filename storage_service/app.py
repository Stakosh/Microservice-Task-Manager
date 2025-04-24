from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)
FILE = 'tasks.json'

import requests
LOGGING_URL = "http://localhost:5003/log"

def log_event(msg):
    try:
        requests.post(LOGGING_URL, json={"message": f"[Storage Service] {msg}"})
    except:
        print("⚠️ No se pudo registrar log desde storage_service")


@app.route('/')
def home():
    return "Storage Service activo"

@app.route('/storage/tasks', methods=['GET'])
def read_tasks():
    if not os.path.exists(FILE):
        return jsonify([])
    with open(FILE, 'r') as f:
        return jsonify(json.load(f))

@app.route('/storage/tasks', methods=['POST'])
def write_tasks():
    data = request.json
    with open(FILE, 'w') as f:
        json.dump(data, f, indent=2)
    return jsonify({"message": "Tareas guardadas"})

if __name__ == "__main__":
    app.run(port=5002)
