from flask import Flask, request, jsonify
import os
import datetime

app = Flask(__name__)
LOG_FILE = 'log.txt'

def write_log(message):
    timestamp = datetime.datetime.now().isoformat()
    with open(LOG_FILE, 'a', encoding='utf-8') as f:
        f.write(f"[{timestamp}] {message}\n")

@app.route('/')
def home():
    write_log("Acceso a ruta / de Logging Service")
    return "Logging Service activo", 200

@app.route('/log', methods=['POST'])
def log_message():
    try:
        data = request.get_json(force=True)
        msg = data.get('message', 'Sin mensaje')
        write_log(msg)
        return jsonify({"message": "Log registrado"}), 201
    except Exception as e:
        write_log(f" Error al registrar log: {e}")
        return jsonify({"error": "No se pudo registrar el log"}), 500

@app.route('/logs', methods=['GET'])
def get_logs():
    try:
        if not os.path.exists(LOG_FILE):
            return jsonify([]), 200
        with open(LOG_FILE, 'r', encoding='utf-8') as f:
            lines = [l.strip() for l in f]
        return jsonify(lines), 200
    except Exception as e:
        write_log(f"❌ Error al leer logs: {e}")
        return jsonify({"error": "No se pudieron leer los logs"}), 500

if __name__ == "__main__":
    app.run(port=5003)
