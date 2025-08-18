from flask import Blueprint, jsonify, request, render_template
from domain.services.services import get_tasks, add_task, complete_task, uncomplete_task
from domain.models.enums import TaskType

bp = Blueprint("tasks", __name__)

@bp.route("/tasks", methods=["GET"])
def list_tasks():
    tasks = get_tasks()
    # return jsonify([{
    #     "id": t.id,
    #     "title": t.title,
    #     "priority": t.priority,
    #     "completed": t.completed,
    #     "type": t.type
    # } for t in tasks])
    return render_template("index.html", tasks=tasks)

@bp.route("/tasks", methods=["POST"])
def create_task():
    data = request.json
    task = add_task(
        title=data["title"],
        priority=data["priority"],
        task_type=TaskType(data["type"])
    )
    return jsonify({"id": task.id, "message": "Task created"}), 201

@bp.route("/tasks/<int:task_id>/complete", methods=["PATCH"])
def mark_complete(task_id):
    task = complete_task(task_id)
    if not task:
        return jsonify({"error": "Task not found"}), 404
    return jsonify({"message": "Task marked as complete"})

@bp.route("/tasks/<int:task_id>/uncompleted", methods=["PATCH"])
def mark_uncomplete(task_id):
    task = uncomplete_task(task_id)
    if not task:
        return jsonify({"error": "Task not found"}), 404
    return jsonify({"message": "Task marked as incomplete"})

@bp.route("/ping")
def ping():
    return "pong"
