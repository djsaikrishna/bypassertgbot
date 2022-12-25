import telegram.ext
TOKEN = '1795538833:AAEXfZEI2JCK0dhxXMIB-nU3eJOtQLqS3s8'

def start(update, context):
    update.message.reply_text("Hello, bot is working!")

updater = telegram.ext.Updater(TOKEN, use_context=True)
disp = updater.dispatcher

disp.add_handler(telegram.ext.CommandHandler("start", start))

updater.start_polling()
updater.idle()
