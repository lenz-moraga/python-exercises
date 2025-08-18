import enum

class TaskType(enum.Enum):
    TASK = "Task",
    TIMED_TASK = "Timed task",
    RECURRING_TASK = "Recurring task"