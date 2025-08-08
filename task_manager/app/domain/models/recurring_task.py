from .task import Task
from datetime import datetime

class RecurringTask(Task):
    def __init__(self, title, priority, recurrence):
        super().__init__(title, priority)
        self.recurrence = recurrence
        self.type = "RecurringTask"

    def to_dict(self):
        base = super().to_dict()
        base["recurrence"] = self.recurrence
        return base

    @classmethod
    def from_dict(cls, data):
        task = cls(
            data["title"],
            data["priority"],
            data["recurrence"]
        )
        task.id = data["id"]
        task.created_at = datetime.fromisoformat(data["created_at"])
        task.completed = data["completed"]
        return task
