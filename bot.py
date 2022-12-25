import telegram.ext
TOKEN = ''

def start(update, context):
    update.message.reply_text("Hello, bot is working!")

updater = telegram.ext.Updater(TOKEN, use_context=True)
disp = updater.dispatcher

disp.add_handler(telegram.ext.CommandHandler("start", start))

updater.start_polling()
updater.idle()
