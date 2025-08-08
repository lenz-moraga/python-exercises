from datetime import datetime
from app.domain.services.task_service import TaskService
from app.domain.models import TimedTask, RecurringTask
from app.infrastructure.repositores.task_repository import TaskRespository

class CLI:
    def __init__(self):
        self.repo = TaskRespository()
        self.service = TaskService(self.repo)

    def run(self):
        while True:
            print("\n--- Gestor de Tareas ---")
            print("1. Agregar tarea simple")
            print("2. Agregar tarea con fecha límite")
            print("3. Agregar tarea recurrente")
            print("4. Marcar como completada")
            print("5. Marcar como no completada")
            print("6. Listar tareas")
            print("7. Salir")


            option = input("Selecciona una opción: ").strip()

            user_action = {
                "1": self.add_task,
                "2": self.add_timed_task,
                "3": self.add_recurring_task,
                "4": self.complete_task,
                "5": self.uncomplete_task,
                "6": self.list_tasks,
            }

            if option in user_action:
                user_action[option]()
            elif option == "7":
                print("Saliendo...")
                break
            else:
                print("Opción inválida.")

    def add_task(self):
        title = input("Título: ").strip()
        priority = self.ask_priority()
        self.service.add_task(title, priority)
        print("✅ Tarea simple agregada.")

    def add_timed_task(self):
        title = input("Título: ").strip()
        priority = self.ask_priority()
        deadline_str = input("Fecha límite (YYYY-MM-DD): ").strip()
        try:
            deadline = datetime.strptime(deadline_str, "%Y-%m-%d")
        except ValueError:
            print("❌ Fecha inválida.")
            return
        task = TimedTask(title, priority, deadline)
        self.service.add_custom_task(task)
        print("✅ Tarea con fecha límite agregada.")

    def add_recurring_task(self):
        title = input("Título: ").strip()
        priority = self.ask_priority()
        recurrence = input(
            "Repetición (daily, weekly, monthly): ").strip().lower()
        if recurrence not in ["daily", "weekly", "monthly"]:
            print("❌ Recurrencia no válida.")
            return
        task = RecurringTask(title, priority, recurrence)
        self.service.add_custom_task(task)
        print("✅ Tarea recurrente agregada.")

    def complete_task(self):
        task_id = input("ID de la tarea: ").strip()
        if self.service.complete_task(task_id):
            print("✅ Completada.")
        else:
            print("❌ No encontrada.")

    def uncomplete_task(self):
        task_id = input("ID de la tarea: ").strip()
        if self.service.uncomplete_task(task_id):
            print("[ ] Marcada como no completada.")
        else:
            print("❌ No encontrada.")

    def list_tasks(self):
        tasks = self.service.list_tasks(sort_by="completed")
        if not tasks:
            print("No hay tareas.")
            return
        for t in tasks:
            status = "✅" if t.completed else "⏳"
            extra = ""
            if hasattr(t, "deadline"):
                extra = f" | Vence: {t.deadline.date()}"
                if t.deadline.date() < datetime.today().date():
                    extra += " (Vencida u.u)"
            elif hasattr(t, "recurrence"):
                extra = f" | Recurre: {t.recurrence}"
            print(
                f"[{status}] {t.title} (ID: {t.id}, Prioridad: {t.priority}{extra})")

    def ask_priority(self):
        try:
            p = int(input("Prioridad (1=Para Ayer, 2=Para Ya, 3=Aguanta): "))
            if p not in [1, 2, 3]:
                raise ValueError()
            return p
        except ValueError:
            print("❌ Prioridad inválida. Se usará 3 (lo vemos la proxima semana papito).")
            return 3
