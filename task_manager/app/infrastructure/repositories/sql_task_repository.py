from app.domain.models.task import Task
from app.infrastructure.external_db.db_connection import get_connection
from app.infrastructure.repositories.base_task_repository import TaskRepository

class SQLTaskRepository(TaskRepository):
    def load_tasks(self, sort_by="priority"):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(f"SELECT id, title, priority, completed FROM tasks ORDER BY {sort_by}")
        rows = cursor.fetchall()
        conn.close()
        return [Task(id=row[0], title=row[1], priority=row[2], completed=row[3]) for row in rows]

    def save_task(self, task: Task) -> None:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO tasks (id, title, priority, completed) VALUES (%s, %s, %s, %s)",
            (task.id, task.title, task.priority, task.completed)
        )
        conn.commit()
        conn.close()

    def complete_task(self, task_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE tasks SET completed = TRUE WHERE id = %s", (task_id,))
        conn.commit()
        conn.close()

    def uncomplete_task(self, task_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE tasks SET completed = FALSE WHERE id = %s", (task_id,))
        conn.commit()
        conn.close()
