import telebot
import logging
from src.authorization import authorize
from src.bot_service import BotService
from src.config import TELEGRAM_BOT_TOKEN, WEBHOOK_URL
from flask import Flask, request

bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)
telebot.logger.setLevel(logging.DEBUG)

bot_service = BotService(bot)

app = Flask(__name__)


@bot.message_handler(commands=['start', 'help'])
@authorize(bot)
def send_welcome(message):
    bot_service.send_welcome(message)


@bot.message_handler(commands=['listname'])
@authorize(bot)
def send_page_title(message):
    bot_service.send_list_name(message)


@bot.message_handler(commands=['tasklist'])
@authorize(bot)
def send_task_list(message):
    bot_service.send_task_list(message)


@bot.message_handler(commands=['togglestatus'])
@authorize(bot)
def toggle_task_status(message):
    bot_service.toggle_task_status(message)


@bot.message_handler(commands=['removetask'])
@authorize(bot)
def remove_task(message):
    bot_service.remove_task(message)


@bot.message_handler(commands=['addtask'])
@authorize(bot)
def add_task(message):
    bot_service.add_task(message)


@app.route('/' + TELEGRAM_BOT_TOKEN, methods=['POST'])
def get_message():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200


@app.route("/")
def welcome_page():
    return "Here a telegram bot is trying to work. Leave me alone please :D", 200


if __name__ == "__main__":
    bot.polling()
else:
    webhook_url = WEBHOOK_URL + TELEGRAM_BOT_TOKEN
    if webhook_url != bot.get_webhook_info().url:
        bot.remove_webhook()
        bot.set_webhook(url=webhook_url)
