from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Notification Service activo", 200

@app.route('/notify', methods=['POST'])
def notify():
    data = request.get_json(force=True)
    print(f"📢 Notificación recibida: {data.get('message', '')}")
    return jsonify({"message": "Notificación recibida"}), 200

if __name__ == "__main__":
    app.run(port=5004)
