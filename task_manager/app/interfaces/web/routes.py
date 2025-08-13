from flask import render_template, request, redirect, url_for, session
from app.domain.services.task_service import TaskService
from app.infrastructure.repositories.json_task_repository import JsonTaskRespository
from app.infrastructure.repositories.sql_task_repository import SQLTaskRepository


def get_service():
    repo_type = session.get('repo_type', 'json')
    if repo_type == "sql":
        repository = SQLTaskRepository()
    else:
        repository = JsonTaskRespository()
    return TaskService(repository)


def register_routes(app):

    @app.route('/', methods=['GET', 'POST'])
    def index():
        if request.method == "POST":
            repo_type = request.form.get("repository")
            session['repo_type'] = repo_type

        service = get_service()
        tasks = service.list_tasks(sort_by="priority")
        return render_template('index.html', tasks=tasks)

    @app.route('/add', methods=['POST'])
    def add_task():
        service = get_service()
        title = request.form.get('title')
        priority = int(request.form.get('priority', 3))
        service.add_task(title, priority)
        return redirect(url_for('index'))

    @app.route('/complete/<task_id>')
    def complete_task(task_id):
        service = get_service()
        service.complete_task(task_id)
        return redirect(url_for('index'))

    @app.route('/uncomplete/<task_id>')
    def uncomplete_task(task_id):
        service = get_service()
        service.uncomplete_task(task_id)
        return redirect(url_for('index'))
