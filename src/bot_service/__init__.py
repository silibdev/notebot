from src.tasks import TaskModel, task_manager

WELCOME_MESSAGE = 'Hello! Welcome to NoTeBot: the Telegram Bot that integrates Notion.so'


def get_list_name():
    return "Notion's page title: HardCoded"


def get_task_list():
    msg = TaskModel.FORMAT + '\n' + str(task_manager)
    return msg
