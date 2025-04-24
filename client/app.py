from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask(__name__, template_folder='templates')
TASK_URL = 'http://localhost:5001/tasks'
LOGS_URL = 'http://localhost:5003/logs'

@app.route('/', methods=['GET'])
def index():
    tasks = requests.get(TASK_URL).json()
    logs = requests.get(LOGS_URL).json()
    return render_template('index.html', tasks=tasks, logs=logs)

@app.route('/add', methods=['POST'])
def add_task():
    title = request.form.get('title')
    if title:
        requests.post(TASK_URL, json={'title': title})
    return redirect(url_for('index'))

@app.route('/complete/<int:task_id>')
def complete(task_id):
    requests.put(f"{TASK_URL}/{task_id}/complete")
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>')
def delete(task_id):
    requests.delete(f"{TASK_URL}/{task_id}")
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(port=5000)