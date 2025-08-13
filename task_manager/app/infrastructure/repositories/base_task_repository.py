from abc import ABC, abstractmethod
from app.domain.models.task import Task
from typing import List

class TaskRepository(ABC):
    
    @abstractmethod
    def load_tasks(self) -> List[Task]:
        pass

    @abstractmethod
    def save_task(self, task: Task) -> None:
        pass

    # @abstractmethod
    # def complete_task(self, task_id: str) -> None:
    #     pass

    # @abstractmethod
    # def uncomplete_task(self, task_id: str) -> None:
    #     pass
