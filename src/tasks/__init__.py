from src.tasks.in_memory_task_manager import InMemoryTaskManager
from src.tasks.task_model import TaskModel

task_manager = InMemoryTaskManager()


def main():
    print('init')
    print(task_manager)
    print('')

    add1 = task_manager.add_task(TaskModel('Title 1', 'Desc 1'))
    print('added task 1')
    print(task_manager)
    print('')

    add1.tags = ['tag1']
    print('added tags to task 1')
    print(task_manager)
    print('')

    add2 = task_manager.add_task(TaskModel('Title 2', 'Desc 2'))
    print('added task 2')
    print(task_manager)
    print('')

    add2.isDone = True
    print('done task 2')
    print(task_manager)
    print('')

    task_manager.remove_task(add2.id)
    print('removed task 2')
    print(task_manager)
    print('')


if __name__ == '__main__':
    main()
