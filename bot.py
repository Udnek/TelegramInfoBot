import logging
import settings
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

open("bot.log", "w").close()
logging.basicConfig(filename='bot.log', level=logging.INFO)


def add_phrase(phrase):
    with open(settings.PHRASES_FILE, 'a') as file:
        file.write("\n"+phrase)


def start(update, context):
    print('Вызван /start')
    update.message.reply_text('Бебра')


def add(update, context):
    if context.args:
        print(f'Вызван /add {context.args}')
        phrase = " ".join(context.args)
        add_phrase(phrase)
        update.message.reply_text(f'Добавленно {phrase}')
    else:
        update.message.reply_text(f'Нюнул бебру')


def random(update, context):
    pass
#    with open(settings.PHRASES_FILE, 'a') as file:
#        file.write("\n"+phrase)


def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)


def main():
    mybot = Updater(settings.API_KEY, use_context=True)

    dispatcher = mybot.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("add", add))
    dispatcher.add_handler(CommandHandler("random", add))
    dispatcher.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info("Бот стартовал")
    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
