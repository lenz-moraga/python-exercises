import json
import os
from task import Task

class TaskManager:
    def __init__(self, file_path="tasks.json"):
        self.file_path = file_path
        self.tasks = []
        self.load_tasks()

    def add_task(self, title, priority):
        task = Task(title, priority)
        self.tasks.append(task)
        self.save_tasks()

    def add_custom_task(self, task):
        self.tasks.append(task)
        self.save_tasks()

    def complete_task(self, task_id):
        for task in self.tasks:
            if task.id.startswith(task_id):
                task.completed = True
                self.save_tasks()
                return True
        return False
    
    def uncomplete_task(self, task_id):
        for task in self.tasks:
            if task.id.startswith(task_id):
                task.completed = False
                self.save_tasks()
                return True
        return False

    def list_tasks(self, sort_by="priority"):
        return sorted(self.tasks, key=lambda t: getattr(t, sort_by, None))

    def save_tasks(self):
        with open(self.file_path, "w") as f:
            json.dump([task.to_dict() for task in self.tasks], f, indent=4)

    def load_tasks(self):
        if not os.path.exists(self.file_path):
            self.tasks = []
            return
        with open(self.file_path, "r") as f:
            data = json.load(f)
            self.tasks = [Task.from_dict(item) for item in data]
