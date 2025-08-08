# app/web/routes.py
from flask import Blueprint, render_template
from ...domain.services.task_service import TaskService

bp = Blueprint("web", __name__)
service = TaskService()

@bp.route("/")
def index():
    tasks = service.list_tasks()
    return render_template("tasks.html", tasks=tasks)
