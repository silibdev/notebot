from src.tasks.task_manager_abstract import TaskManagerAbstract


class InMemoryTaskManager(TaskManagerAbstract):
    def __init__(self):
        super(InMemoryTaskManager, self).__init__({})
        self._seq = 0

    def get_task_list(self):
        return list(self._task_list.values()).sort(key=lambda t: t.id)

    def get_task(self, task_id):
        return self._task_list[task_id]

    def add_task(self, task):
        self._seq += 1
        task_id = self._seq
        task.id = task_id
        self._task_list[task_id] = task
        return task

    def remove_task(self, task_id):
        task_removed = self._task_list.pop(task_id)
        return task_removed
