from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS

app = Flask(__name__, static_folder="static")
CORS(app)

tasks = [
    {"id": 1, "title": "Prepare SSD document", "completed": False},
    {"id": 2, "title": "Prepare BRD document", "completed": False},
    {"id": 3, "title": "Describe API endpoints in Swagger", "completed": True},
]

next_id = 4


@app.route("/")
def index():
    return send_from_directory("static", "index.html")


@app.route("/api/tasks", methods=["GET"])
def get_tasks():
    return jsonify(tasks), 200


@app.route("/api/tasks", methods=["POST"])
def create_task():
    global next_id

    data = request.get_json()

    if not data or not data.get("title"):
        return jsonify({"error": "Task title is required"}), 400

    new_task = {
        "id": next_id,
        "title": data["title"],
        "completed": False
    }

    tasks.append(new_task)
    next_id += 1

    return jsonify(new_task), 201


@app.route("/api/tasks/<int:task_id>", methods=["PATCH"])
def update_task(task_id):
    data = request.get_json()

    for task in tasks:
        if task["id"] == task_id:
            if "completed" in data:
                task["completed"] = bool(data["completed"])
            if "title" in data and data["title"]:
                task["title"] = data["title"]

            return jsonify(task), 200

    return jsonify({"error": "Task not found"}), 404


@app.route("/api/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            return jsonify({"message": "Task deleted successfully"}), 200

    return jsonify({"error": "Task not found"}), 404


if __name__ == "__main__":
    app.run(debug=True)
