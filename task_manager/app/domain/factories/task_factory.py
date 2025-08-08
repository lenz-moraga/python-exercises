from app.domain.models import Task, TimedTask, RecurringTask

def TaskFactory(data):
    task_type = data.get("type", "Task")
    
    task_type_dict = {
        "TimedTask": TimedTask.from_dict,
        "RecurringTask": RecurringTask.from_dict,
    }

    if task_type in task_type_dict:
        return task_type_dict[task_type](data)
    else:
        return Task._from_base_dict(data)
