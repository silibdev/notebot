from src.tasks.task_model import TaskModel, Priority

# from src.tasks.in_memory_task_manager import InMemoryTaskManager
# task_manager = InMemoryTaskManager()

from src.tasks.notion_task_manager import NotionTaskManager
from src.config import BLOCK_URL, NOTION_TOKEN
task_manager = NotionTaskManager(NOTION_TOKEN, BLOCK_URL)


def main():
    from datetime import datetime

    print('init')
    print(task_manager)
    print('')

    add1 = task_manager.add_task(TaskModel('Title 1', 'Desc 1'))
    print('added task 1')
    print(task_manager)
    print('')

    add1.due_date = datetime.now()
    task_manager.modify_task(add1)
    print('added due date today to task 1')
    print(task_manager)
    print('')

    add2 = task_manager.add_task(TaskModel('Title 2', 'Desc 2'))
    print('added task 2')
    print(task_manager)
    print('')

    add2.priority = Priority.HIGH
    task_manager.modify_task(add2)
    print('set priority high to task 2')
    print(task_manager)
    print('')

    add2.isDone = True
    task_manager.modify_task(add2)
    print('done task 2')
    print(task_manager)
    print('')

    task_manager.remove_task(add2.id)
    print('removed task 2')
    print(task_manager)
    print('')


if __name__ == '__main__':
    main()
