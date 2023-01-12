import logging
import settings
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
logging.basicConfig(filename='bot.log', level=logging.INFO)


def greet_user(update, context):
    print('Вызван /start')
    update.message.reply_text('Нюхай бебру')


def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)


def main():
    mybot = Updater(settings.API_KEY, use_context=True)

    dispatcher = mybot.dispatcher
    dispatcher.add_handler(CommandHandler("start", greet_user))
    dispatcher.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info("Бот стартовал")
    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
