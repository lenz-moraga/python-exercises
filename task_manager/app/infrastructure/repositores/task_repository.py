import os
import json
from app.domain.factories.task_factory import TaskFactory

class TaskRespository:
    def __init__(self, filepath="app/infrastructure/local_persistence/tasks.json"):
        self.file_path = filepath

    def save_tasks(self, tasks):
        with open(self.file_path, "w") as f:
            json.dump([task.to_dict() for task in tasks], f, indent=4)

    def load_tasks(self):
        folder = os.path.dirname(self.file_path)
        if not os.path.exists(folder):
            print("La carpeta local_persistence no existe!")
            return []
    
        if os.path.exists(self.file_path) and os.path.getsize(self.file_path) == 0:
            print("La carpeta local_persistence existe pero la lista esta vacia!")
            return []
        
        try:                
            with open(self.file_path, "r") as f:
                data_list = json.load(f)
                tasks = [TaskFactory(data) for data in data_list]
                return tasks
        except ValueError as error:
            print("Warning: Error al cargar el archivo JSON", error)
            return []
            
