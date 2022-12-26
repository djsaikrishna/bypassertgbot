from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
from tld import get_tld
import PyBypass as bypasser
import PyBypass
import os
import logging

#Made with Love by KATPER
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logging.info('Starting Bot...')

def bypass(update, context):
    url = context.args[0]
    res = get_tld(url, as_object=True)

    
    if res.domain in ["gplinks","try2link","adf","link-center","bitly","ouo","shareus","shortly","tinyurl","thinfi","hypershort","sirigan","gtlinks","theforyou","linkvertise","shortest","pkin","tekcrypt","short2url","rocklinks","rocklinks","moneykamalo","easysky","indianshortner","crazyblog","tnvalue","shortingly","dulink","bindaaslinks","pdiskshortener","mdiskshortner","earnl","rewayatcafe","crazyblog","bitshorten","rocklink","droplink","earn4link","tnlink","ez4short","xpshort","vearnl","adrinolinks","techymozo","linkbnao","linksxyz","short-jambo","droplink","linkpays","pi-l","tnlink","open2get","anonfiles","antfiles","1fichier","gofile","hxfile","krakenfiles","mdisk","mediafire","pixeldrain","racaty","sendcm","sfile","solidfiles","sourceforge","uploadbaz","uploadee","uppit","userscloud","wetransfer","yandex","zippyshare","fembed","mp4upload","streamlare","streamsb","streamtape","appdrive","gdtot","hubdrive","sharerpw"]:
        if (res.domain == "link-center"):
            bypassed_link = bypasser.bypass(url, name="linkvertise")
        elif (res.domain == "gdtot"):
            crypt = os.getenv('CRYPT') #CRYPT is env variable stored in codecapsules.io 
            bypassed_link = PyBypass.bypass(url, gdtot_crypt=crypt)
        else:
            bypassed_link = bypasser.bypass(url)
    else:
        bypassed_link = "❌ Domain not supported:",res.domain
    

    
       # return("Output URL>>", bypassed_link)
        #print("Made with Love by KATPER")
    
        
        
        
    update.message.reply_text(f"✅ OUTPUT>>🔗 {bypassed_link}")
    update.message.reply_text("Made with Love by KATPER")
#def bypass_url(update: Update, context: CallbackContext):
#    update.message.reply_text(bypass())  
    
def start(update: Update, context: CallbackContext):
    update.message.reply_text("Hello, This is bypasser bot madee by AD")  
def owner(update: Update, context: CallbackContext):
    update.message.reply_text("Owner of this bot is KATPAR SAHAB")  
def help(update: Update, context: CallbackContext):
    update.message.reply_text("type /bypass <url>")  
    
def unknown_text(update: Update, context: CallbackContext):
    update.message.reply_text("Sorry I can't recognize you , you said '%s'" % update.message.text)
  
  
def unknown(update: Update, context: CallbackContext):
    update.message.reply_text("Sorry '%s' is not a valid command" % update.message.text)    

def error(update, context):
    # Logs errors
    logging.error(f'Update {update} caused error {context.error}')

def main():
    
    TOKEN = os.getenv('BOTAPIKEY')
    updater = Updater(token=TOKEN, use_context=True)
    dispatcher = updater.dispatcher
    
    updater.dispatcher.add_handler(CommandHandler('bypass', bypass))
    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CommandHandler('owner', owner))
    updater.dispatcher.add_handler(CommandHandler('help', help))
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
