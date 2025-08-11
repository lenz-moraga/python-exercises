from flask import render_template, request, redirect, url_for
from app.domain.services.task_service import TaskService
from app.infrastructure.repositores.task_repository import TaskRespository


repository = TaskRespository()
service = TaskService(repository)


def register_routes(app):

    @app.route('/')
    def index():
        tasks = service.list_tasks(sort_by="priority")
        return render_template('index.html', tasks=tasks)

    @app.route('/add', methods=['POST'])
    def add_task():
        title = request.form.get('title')
        priority = int(request.form.get('priority', 3))
        service.add_task(title, priority)
        return redirect(url_for('index'))

    @app.route('/complete/<task_id>')
    def complete_task(task_id):
        service.complete_task(task_id)
        return redirect(url_for('index'))

    @app.route('/uncomplete/<task_id>')
    def uncomplete_task(task_id):
        service.uncomplete_task(task_id)
        return redirect(url_for('index'))
