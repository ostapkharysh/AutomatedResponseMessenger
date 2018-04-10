"""Basic example for a bot that uses inline keyboards.
# Modification of the program dedicated to the public domain under the CC0 license.
"""
import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler,  MessageHandler, Filters

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)


def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="I'm a bot, who could let you "
                                                          "answer yes/no to the certain questions!")

    keyboard = [[InlineKeyboardButton("Yes", callback_data='1'),
                 InlineKeyboardButton("No", callback_data='2')]]

    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text('Please choose:', reply_markup=reply_markup)

def echo(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text=update.message.text)

def decide(bot, update):
    print(update.message.text)
    #bot.send_message(chat_id=update.message.chat_id, text=update.message.text)

def button(bot, update):
    query = update.callback_query

    bot.edit_message_text(text="Your answer: {}".format(query.data),
                          chat_id=query.message.chat_id,
                          message_id=query.message.message_id)


def help(bot, update):
    update.message.reply_text("Use /start to test this bot.")


def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)


updater = Updater('535695146:AAHcfzozKx3scHwQFP7WlvZNZBr0mOO4y0Y')

updater.dispatcher.add_handler(CommandHandler('start', start))

def main():
    # Create the Updater and pass it your bot's token.
    #updater = Updater('535695146:AAHcfzozKx3scHwQFP7WlvZNZBr0mOO4y0Y')

    #updater.dispatcher.add_handler(CommandHandler('start', start))

    print(MessageHandler(Filters.text, echo))

    echo_handler = MessageHandler(Filters.text, echo)
    updater.dispatcher.add_handler(echo_handler)


    updater.dispatcher.add_handler(CallbackQueryHandler(button))
    updater.dispatcher.add_handler(CommandHandler('help', help))
    updater.dispatcher.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT
    updater.idle()


while True:
    main()