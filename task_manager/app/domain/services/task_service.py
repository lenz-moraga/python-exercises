from app.domain.models import Task

class TaskService:
    def __init__(self, repository):
        self.repository = repository

    def add_task(self, title, priority):
        task = Task(title, priority)
        self.repository.save_task(task)

    def add_custom_task(self, task):
        self.tasks.append(task)
        self.repository.save_task(self.tasks)

    def complete_task(self, task_id):
        for task in self.tasks:
            if task.id.startswith(task_id):
                task.completed = True
                self.repository.save_task(self.tasks)
                return True
        return False

    def uncomplete_task(self, task_id):
        for task in self.tasks:
            if task.id.startswith(task_id):
                task.completed = False
                self.repository.save_task(self.tasks)
                return True
        return False

    def list_tasks(self, sort_by="priority"):
        tasks = self.repository.load_tasks()
        return sorted(tasks, key=lambda t: getattr(t, sort_by, None))
