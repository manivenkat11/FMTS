from flask import Flask, request, jsonify
from backend.service.task_service import create_task, get_all_tasks

app = Flask(__name__)

@app.route('/tasks', methods=['POST'])
def add_task():
    data = request.json
    return jsonify(create_task(data))

@app.route('/tasks', methods=['GET'])
def list_tasks():
    return jsonify(get_all_tasks())

if __name__ == "__main__":
    app.run(debug=True)
