import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)



def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)
    update.message.reply_text('Error somewhere')



def photo(update, context):
    update.message.reply_text('Sent photo')
    file = update.message.photo[-1].get_file()
    file.download("temp.jpg")
    update.message.reply_text('Got photo')

def live(update, context):
    update.message.reply_text('Sys Live')

def main():
    updater = Updater("<<API KEY>>", use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("live", live))
    dp.add_handler(MessageHandler(Filters.photo, photo))



    dp.add_error_handler(error)
    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
