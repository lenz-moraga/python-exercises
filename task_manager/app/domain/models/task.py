import uuid
from datetime import datetime


class Task:
    def __init__(self, title, priority, id=None, completed=False):
        self.id = id if id else str(uuid.uuid4())
        self.title = title
        self.priority = priority
        self.created_at = datetime.now()
        self.completed = False
        self.type = "Task"

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "priority": self.priority,
            "created_at": self.created_at.isoformat(),
            "completed": self.completed,
            "type": self.type
        }

    @classmethod
    def _from_base_dict(cls, data):
        task = cls(data["title"], data["priority"])
        task.id = data["id"]
        task.created_at = datetime.fromisoformat(data["created_at"])
        task.completed = data["completed"]
        return task
