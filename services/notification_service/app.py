from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return 'Notification Service (WIP)'

@app.route('/notify', methods=['POST'])
def notify():
    data = request.get_json(force=True)
    return jsonify({'message': 'Notification received', 'data': data}), 200

@app.route('/status', methods=['GET'])
def status():
    return jsonify({'status': 'Not implemented'}), 200

if __name__ == '__main__':
    app.run(port=5004)