from infrastructure.database import SessionLocal
from domain.models.models import Task
from domain.models.enums import TaskType

def get_tasks():
    with SessionLocal() as db:
        result = db.query(Task).order_by(Task.priority).all()

        print("result >>>>>>>>>>>>>>>>>>>>>>>>", result)
        return result

def add_task(title: str, priority: int, task_type: TaskType):
    with SessionLocal() as db:
        task = Task(title=title, priority=priority, type=task_type)
        db.add(task)
        db.commit()
        db.refresh(task)
        return task

def complete_task(task_id: int):
    with SessionLocal() as db:
        task = db.query(Task).filter(Task.id == task_id).first()
        if task:
            task.completed = True
            db.commit()
            return task
        return None

def uncomplete_task(task_id: int):
    with SessionLocal() as db:
        task = db.query(Task).filter(Task.id == task_id).first()
        if task:
            task.completed = False
            db.commit()
            return task
        return None
