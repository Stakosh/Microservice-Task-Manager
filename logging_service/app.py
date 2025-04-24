from flask import Flask, request, jsonify
import os
import datetime

app = Flask(__name__)
LOG_FILE = 'log.txt'

def write_log(message):
    timestamp = datetime.datetime.now().isoformat()
    with open(LOG_FILE, 'a') as f:
        f.write(f"[{timestamp}] {message}\n")

@app.route('/')
def home():
    write_log("Acceso a ruta / de Logging Service")
    return "Logging Service activo"

@app.route('/log', methods=['POST'])
def log():
    try:
        data = request.json
        if not data or "message" not in data:
            raise ValueError("JSON inválido: falta 'message'")
        write_log(data["message"])
        return jsonify({"message": "Evento registrado"})
    except Exception as e:
        write_log(f"❌ Error al registrar evento: {str(e)}")
        return jsonify({"error": str(e)}), 400

@app.route('/logs', methods=['GET'])
def get_logs():
    try:
        if not os.path.exists(LOG_FILE):
            return jsonify([])
        with open(LOG_FILE, 'r') as f:
            logs = f.readlines()
        return jsonify([line.strip() for line in logs])
    except Exception as e:
        write_log(f"❌ Error al leer logs: {str(e)}")
        return jsonify({"error": "No se pudieron leer los logs"}), 500

if __name__ == "__main__":
    app.run(port=5003)
