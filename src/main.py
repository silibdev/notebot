import telebot
import os
import logging


bot = telebot.TeleBot(os.environ["TELEGRAM_BOT_TOKEN"])
telebot.logger.setLevel(logging.DEBUG)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Hello! Welcome to NoTeBot: the Telegram Bot that integrates Notion.so")


def main():
    bot.polling()


if __name__ == '__main__':
    main()
