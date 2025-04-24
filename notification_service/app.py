from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Notification Service activo (WIP)"

@app.route('/notify', methods=['POST'])
def notify():
    data = request.json
    print(f"Notificación enviada: {data.get('message')}")
    return jsonify({"message": "Notificación enviada (simulada)"})

@app.route('/status')
def status():
    return jsonify({"status": "activo"})

if __name__ == "__main__":
    app.run(port=5004)
