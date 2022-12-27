"""
@author  KATPER
@date    28-12-2022
@desc
    Ad link bypasser bot which can also bypass gdtot links
@change
    basic bot created ----------------------------------- 20-12-2022
    added gdtot support --------------------------------- 21-12-2022
    added check if url is not provided ------------------ 22-12-2022
    added icons and emojis ------------------------------ 23-12-2022
    added bot start info display in logs ---------------- 24-12-2022
    added logging info for each task in logs ------------ 28-12-2022
    reserved -------------------------------------------- 00-12-2022
"""
from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
from telegram import Update
from tld import get_tld
import PyBypass as bypasser
import PyBypass
import os
import logging

#Made with Love by KATPER
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logging.info('Starting Bot...')

def bypass(update, context):
    if len(context.args) == 0: #If no url is sent, than this will show this msg
        logging.info("Error: No Link provided!")
        update.message.reply_text("You havent provided any link!\nSend command as /bypass <url>")
    else:
        url = context.args[0]
        res = get_tld(url, as_object=True)
        logging.info(f"Link detected: {url}")
    
    if res.domain in ["gplinks","try2link","adf","link-center","bitly","ouo","shareus","shortly","tinyurl","thinfi","hypershort","sirigan","gtlinks","theforyou","linkvertise","shortest","pkin","tekcrypt","short2url","rocklinks","rocklinks","moneykamalo","easysky","indianshortner","crazyblog","tnvalue","shortingly","dulink","bindaaslinks","pdiskshortener","mdiskshortner","earnl","rewayatcafe","crazyblog","bitshorten","rocklink","droplink","earn4link","tnlink","ez4short","xpshort","vearnl","adrinolinks","techymozo","linkbnao","linksxyz","short-jambo","droplink","linkpays","pi-l","tnlink","open2get","anonfiles","antfiles","1fichier","gofile","hxfile","krakenfiles","mdisk","mediafire","pixeldrain","racaty","sendcm","sfile","solidfiles","sourceforge","uploadbaz","uploadee","uppit","userscloud","wetransfer","yandex","zippyshare","fembed","mp4upload","streamlare","streamsb","streamtape","appdrive","gdtot","hubdrive","sharerpw"]:
        if (res.domain == "link-center"):
            bypassed_link = bypasser.bypass(url, name="linkvertise")
            update.message.reply_text(f"✅ Bypassed Link➡️ {bypassed_link}",disable_web_page_preview=True, quote=True)
            update.message.reply_text("⭐ Made with Love by KATPER")
            logging.info("Link bypassed successfully!")
        elif (res.domain == "gdtot"):
            crypt = os.getenv('CRYPT') #CRYPT is env variable stored in codecapsules.io 
            bypassed_link = PyBypass.bypass(url, gdtot_crypt=crypt)
            update.message.reply_text(f"✅ Bypassed GDTOT Link➡️ {bypassed_link}",disable_web_page_preview=True)
            update.message.reply_text("⭐ Made with Love by KATPER")
            logging.info("File copied to privided google account!")
        else:
            bypassed_link = bypasser.bypass(url)
            update.message.reply_text(f"✅ Bypassed Link➡️ {bypassed_link}",disable_web_page_preview=True)
            update.message.reply_text("⭐ Made with Love by KATPER")
            logging.info("Link bypassed successfully!")
    else:
        
        update.message.reply_text(f"❌ Link not supported!\nDetected Domain ➡️ {res.domain}",disable_web_page_preview=True)
        update.message.reply_text("⭐ Made with Love by KATPER")
        logging.info("Error: Link not supported!")

    
def start(update: Update, context: CallbackContext):
    update.message.reply_text("Hello, This is bypasser bot madee by AD")
    logging.info("/start command!")

def owner(update: Update, context: CallbackContext):
    update.message.reply_text("Owner of this bot is KATPER SAHAB")
    logging.info("/owner command!")

def help(update: Update, context: CallbackContext):
    update.message.reply_text("type /bypass <url>") 
    logging.info("/help command!")
    
def unknown_text(update: Update, context: CallbackContext):
    update.message.reply_text("Sorry I can't recognize you , you said '%s'" % update.message.text)
    logging.info("unknown command!")
  
def unknown(update: Update, context: CallbackContext):
    update.message.reply_text("Sorry '%s' is not a valid command" % update.message.text)    

def error(update, context):
    # Logs errors
    logging.error(f'Update {update} caused error {context.error}')
    
    '''   
def test_callback(update, context):
    chat_id = (bot.get_updates())[-1].message.chat_id
    user_says = " ".join(context.args)
    update.message.chat_id("You said: " + user_says)

def test1_callback(update, context):
    chat_id = (bot.get_updates())[-1].message.chat_id
    user_says = " ".join(context.args)
    update.message.reply_text(chat_id=update.effective_chat.id, text="Hello world!")
    ''' 
 
def main():
    
    TOKEN = os.getenv('BOTAPIKEY')
    updater = Updater(token=TOKEN, use_context=True)
    dispatcher = updater.dispatcher
    
    updater.dispatcher.add_handler(CommandHandler('bypass', bypass))
    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CommandHandler('owner', owner))
    updater.dispatcher.add_handler(CommandHandler('help', help))
    updater.dispatcher.add_handler(CommandHandler("test", test_callback))
    updater.dispatcher.add_handler(CommandHandler("test1", test1_callback))
    updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))
    updater.dispatcher.add_handler(MessageHandler(
    # Filters out unknown commands
    Filters.command, unknown))
    updater.dispatcher.add_error_handler(error)
  
    # Filters out unknown messages.
    updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))
    PORT = int(os.environ.get('PORT', '443'))
    HOOK_URL = 'https://bypassertgbot-eqqgxx.codecapsules.co.za' + '/' + TOKEN
    updater.start_webhook(listen='0.0.0.0', port=PORT, url_path=TOKEN, webhook_url=HOOK_URL)
    updater.idle()

if __name__ == '__main__':
    main()
