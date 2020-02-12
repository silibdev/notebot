from typing import Dict, List

from src.tasks.task_model import TaskModel


class TaskManagerAbstract:
    def __init__(self, task_list: Dict[str, TaskModel]):
        self._task_list = task_list

    def get_task_list(self) -> List[TaskModel]:
        pass

    def get_task(self, task_id: str) -> TaskModel:
        pass

    def add_task(self, task: TaskModel) -> TaskModel:
        pass

    def remove_task(self, task_id: str) -> TaskModel:
        pass

    def __str__(self):
        return '\n'.join(map(lambda t: str(t), self._task_list.values()))
