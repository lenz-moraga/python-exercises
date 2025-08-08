from .task import Task
from datetime import datetime


class TimedTask(Task):
    def __init__(self, title, priority, deadline):
        super().__init__(title, priority)
        self.deadline = deadline
        self.type = "TimedTask"

    def to_dict(self):
        base = super().to_dict()
        base["deadline"] = self.deadline.isoformat()
        return base

    @classmethod
    def from_dict(cls, data):
        task = cls(
            data["title"],
            data["priority"],
            datetime.fromisoformat(data["deadline"])
        )
        task.id = data["id"]
        task.created_at = datetime.fromisoformat(data["created_at"])
        task.completed = data["completed"]
        return task
