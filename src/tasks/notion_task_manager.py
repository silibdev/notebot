from notion.client import NotionClient
from notion.collection import NotionDate

from src.tasks import TaskModel, Priority
from src.tasks.task_manager_abstract import TaskManagerAbstract


class NotionTaskManager(TaskManagerAbstract):
    def __init__(self, token, block_url):
        super(NotionTaskManager, self).__init__({})
        self._notion_client = NotionClient(token_v2=token)
        self._page = self._notion_client.get_block(block_url)
        self._cv = self._notion_client.get_collection_view(block_url)
        self._map_task_row = {}
        self.get_tasks_list()

    def get_page_name(self):
        return self._page.title

    def get_tasks_list(self):
        self._task_list = {}
        self._map_task_row = {}
        for row in self._cv.default_query().execute():
            self._map_task_row[row.id] = row
            self._task_list[row.id] = NotionTaskManager._row_to_task(row, row.id)
        return self._task_list.values()

    def get_task(self, task_id):
        return self._task_list[task_id]

    def add_task(self, task):
        row = self._cv.collection.add_row()
        NotionTaskManager._task_to_row(task, row)
        row.refresh()
        self._map_task_row[row.id] = row
        self._task_list[row.id] = task
        return task

    def modify_task(self, task):
        row = self._map_task_row[task.id]
        NotionTaskManager._task_to_row(task, row)
        row.refresh()

        self._task_list[task.id] = task
        return task

    def remove_task(self, task_id):
        row = self._map_task_row[task_id]
        if row is not None:
            task = NotionTaskManager._row_to_task(row, task_id)
            row.remove()
            self.get_tasks_list()
            return task
        else:
            return None

    @staticmethod
    def _row_to_task(row, task_id):
        if row.priority == Priority.HIGH.value:
            priority = Priority.HIGH
        elif row.priority == Priority.MEDIUM.value:
            priority = Priority.MEDIUM
        else:
            priority = None
        due_date = None if row.due_date is None else row.due_date.start
        task = TaskModel(row.title, row.description, priority, due_date)
        task.id = task_id
        task.isDone = row.done
        return task

    @staticmethod
    def _task_to_row(task: TaskModel, row):
        row.title = task.title
        row.description = task.description
        row.priority = None if task.priority is None else task.priority.value
        row.due_date = NotionDate(task.due_date)
        row.done = task.isDone
        task.id = row.id
        row.refresh()


def main():
    from src.config import BLOCK_URL, NOTION_TOKEN
    notion_service = NotionTaskManager(NOTION_TOKEN, BLOCK_URL)
    print("The page name is:", notion_service.get_page_name())
    print("The list is:")
    print("Name\t\tDescription\t\tTags\t\tDone")

    for row in notion_service._cv.collection.get_rows():
        print("{}\t\t{}\t\t{}\t\t{}\t\t{}".format(row.title, row.description, row.due_date.start, row.priority, row.done))


if __name__ == '__main__':
    main()
