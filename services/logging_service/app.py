from flask import Flask, request, jsonify
import os

app = Flask(__name__)
LOG_FILE = 'log.txt'

@app.route('/', methods=['GET'])
def index():
    return 'Logging Service is running'

@app.route('/log', methods=['POST'])
def add_log():
    data = request.get_json(force=True)
    event = data.get('event', '')
    with open(LOG_FILE, 'a') as f:
        f.write(event + '\n')
    return jsonify({'message': 'Event logged'}), 201

@app.route('/logs', methods=['GET'])
def get_logs():
    if not os.path.exists(LOG_FILE):
        open(LOG_FILE, 'w').close()
    with open(LOG_FILE, 'r') as f:
        logs = f.read().splitlines()
    return jsonify(logs)

if __name__ == '__main__':
    app.run(port=5003)