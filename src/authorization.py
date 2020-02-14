from src.config import PERSONAL_ID


def authorize(bot):
    def authorize_decorator(func):
        def check_message_id(message):
            if str(message.from_user.id) != PERSONAL_ID:
                bot.send_message(message.chat.id, "I'm a personal bot (at the moment)."
                                                  "\nI'm sorry :(\nPlease remove me.")
            else:
                func(message)
        return check_message_id
    return authorize_decorator

