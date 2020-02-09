# NoTeBot

### No(tion)Te(legram)Bot

This project aims to integrate [Notion.so](https://www.notion.so) into [Telegram](https://telegram.org) through [Telegram Bot API](https://core.telegram.org/bots/api).

##Libraries
* Python 3.7
* Python Telegram Bot Api: [pyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI)
* Python Notion Unofficial API:  [notion-py](https://github.com/jamalex/notion-py)

## Dev
#### Python Dependencies
* A `virtualenv` is suggested in order to install python dependencies. 
```
$ virtualenv <env_name>
$ source <env_name>/bin/activate
(<env_name>)$ pip install -r requirements.txt
```
> *NOTE*  
> Use this to create deps file `pip freeze > requirements.txt`

#### Bot Configuration
The bot api needs a token, this bot searches it in the environment variable `TELEGRAM_BOT_TOKEN`.  
You can retrieve the from BotFather in Telegram.