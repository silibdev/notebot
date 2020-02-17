from telebot import types

from src.tasks import task_manager, TaskModel, Priority


class BotService:
    WELCOME_MESSAGE = 'Hello! Welcome to NoTeBot: the Telegram Bot that integrates Notion.so'

    def __init__(self, bot):
        self.bot = bot
        self.task_in_creation = None

    def _send_message(self, message, msg, reply_markup=None):
        self.bot.send_message(message.chat.id, msg, reply_markup=reply_markup)

    def send_welcome(self, message):
        self._send_message(message, BotService.WELCOME_MESSAGE)

    def send_list_name(self, message):
        self._send_message(message, "Notion's page title: HardCoded")

    def send_task_list(self, message):
        task_list = task_manager.get_tasks_list()
        for t in task_list:
            self._send_message(message, t)

    def add_task(self, message):
        self.task_in_creation = None
        self._send_message(message, 'Title')
        self.bot.register_next_step_handler(message, lambda m: self.add_task_process_title_step(m))

    def add_task_process_title_step(self, message):
        try:
            task_title = message.text
            self.task_in_creation = TaskModel(task_title)
            markup = types.ReplyKeyboardMarkup(row_width=2, one_time_keyboard=True, resize_keyboard=True)
            high_button = types.KeyboardButton('High')
            medium_button = types.KeyboardButton('Medium')
            none_button = types.KeyboardButton('None')
            markup.add(high_button, medium_button, none_button)
            self._send_message(message, 'Priority?', reply_markup=markup)
            self.bot.register_next_step_handler(message, lambda m: self.add_task_last_step(m))
        except Exception as e:
            self._send_message(message, 'Error while creating the task')

    def add_task_last_step(self, message):
        try:
            task_priority = message.text
            if task_priority == 'High':
                self.task_in_creation.priority = Priority.HIGH
            elif task_priority == 'Medium':
                self.task_in_creation.priority = Priority.MEDIUM

            task_created = task_manager.add_task(self.task_in_creation)
            markup_remove = types.ReplyKeyboardRemove()
            self._send_message(message, str(task_created) + '\n--Created--', reply_markup=markup_remove)
        except Exception as e:
            print(e)
            self._send_message(message, 'Error while creating the task')

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
