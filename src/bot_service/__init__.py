from src.tasks import task_manager, TaskModel


class BotService:
    WELCOME_MESSAGE = 'Hello! Welcome to NoTeBot: the Telegram Bot that integrates Notion.so'

    def __init__(self, bot):
        self.bot = bot

    def _send_message(self, message, msg):
        self.bot.send_message(message.chat.id, msg)

    def send_welcome(self, message):
        self._send_message(message, BotService.WELCOME_MESSAGE)

    def send_list_name(self, message):
        self._send_message(message, "Notion's page title: HardCoded")

    def send_task_list(self, message):
        task_list = task_manager.get_tasks_list()
        for t in task_list:
            self._send_message(message, t)

    def add_task(self, message):
        task = TaskModel(message.text)
        task_created = task_manager.add_task(task)
        self._send_message(message, str(task_created) + '\n--Created--')

    def toggle_task_status(self, message):
        if message.reply_to_message is None:
            self._send_message(message, 'You have to reply the task to which toggle the status')
        else:
            task_id = message.reply_to_message.text.split('\n')[0]
            task = task_manager.get_task(task_id)
            task.isDone = not task.isDone
            task_manager.modify_task(task)
            self._send_message(message, str(task) + '\n--Modified--')

    def remove_task(self, message):
        if message.reply_to_message is None:
            self._send_message(message, 'You have to reply the task to remove')
        else:
            task_id = message.reply_to_message.text.split('\n')[0]
            task_removed = task_manager.remove_task(task_id)
            self._send_message(message, str(task_removed) + '\n--Deleted--')

