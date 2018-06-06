from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


updater = Updater(token='554425042:AAHnLVakFnVxyUAfnO27sMGUxOc8jqg3ylU')
dispatcher = updater.dispatcher


def start_command(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text='Whats up')


def text_message(bot, update):
    response = 'Received: ' + update.message.text
    bot.send_message(chat_id=update.message.chat_id, text=response)


start_command_handler = CommandHandler('start', start_command)
text_message_handler = MessageHandler(Filters.text, text_message)

dispatcher.add_handler(start_command_handler)
dispatcher.add_handler(text_message_handler)

updater.start_polling(clean=True)

updater.idle()
