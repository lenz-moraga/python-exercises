import uuid
from datetime import datetime


class Task:
    def __init__(self, title, priority):
        self.id = str(uuid.uuid4())
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
    def from_dict(cls, data):
        task_type = data.get("type", "Task")
        if task_type == "TimedTask":
            return TimedTask.from_dict(data)
        elif task_type == "RecurringTask":
            return RecurringTask.from_dict(data)
        else:
            return Task._from_base_dict(data)

    @classmethod
    def _from_base_dict(cls, data):
        task = cls(data["title"], data["priority"])
        task.id = data["id"]
        task.created_at = datetime.fromisoformat(data["created_at"])
        task.completed = data["completed"]
        return task


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
