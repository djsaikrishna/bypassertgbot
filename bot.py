import requests
from telegram.ext import Updater, CommandHandler
from tld import get_tld
import PyBypass as bypasser
import PyBypass
import os
#Made with Love by KATPER

def return_bypass():
    
    userLink = input("\nEnter Link to bypass\n")
    res = get_tld(userLink, as_object=True)
 
    if res.domain not in ["gplinks","try2link","adf","bitly","ouo","shareus","shortly","tinyurl","thinfi","hypershort","sirigan","gtlinks","theforyou","linkvertise","shortest","pkin","tekcrypt","short2url","rocklinks","rocklinks","moneykamalo","easysky","indianshortner","crazyblog","tnvalue","shortingly","dulink","bindaaslinks","pdiskshortener","mdiskshortner","earnl","rewayatcafe","crazyblog","bitshorten","rocklink","droplink","earn4link","tnlink","ez4short","xpshort","vearnl","adrinolinks","techymozo","linkbnao","linksxyz","short-jambo","droplink","linkpays","pi-l","tnlink","open2get","anonfiles","antfiles","1fichier","gofile","hxfile","krakenfiles","mdisk","mediafire","pixeldrain","racaty","sendcm","sfile","solidfiles","sourceforge","uploadbaz","uploadee","uppit","userscloud","wetransfer","yandex","zippyshare","fembed","mp4upload","streamlare","streamsb","streamtape","appdrive","gdtot","hubdrive","sharerpw"]:
        return("That url is not supported yet, come back later!")
    elif (res.domain == "link-center"):
        bypassed_link = bypasser.bypass(userLink, name="linkvertise")
        return("Output URL>>",bypassed_link)
        print("Made with Love by KATPER")
    elif (res.domain == "sharer"):
        return ("sharer")
        print("Made with Love by KATPER")
    elif (res.domain == "gdtot"):
        crypt = input('\nEnter crypt value with double quotes\nExample "OXZIcTlGEF5Z3dxcTdkQdThJnBmKZdc5Dc6DcGhErWVhM2g5bjY0NnhlWERzQT0%3D"\n')
        bypassed_link = PyBypass.bypass(userLink, gdtot_crypt=crypt)
        return("Output URL>>",bypassed_link)
        print("Made with Love by KATPER")
    else:
        bypassed_link = bypasser.bypass(userLink)
        return("Output URL>>",bypassed_link)
        print("Made with Love by KATPER")
        #again = input("Wanna bypass another?")

def bypass(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text=return_bypass())
    
def start(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text='Hi! This is bypass bot, send /bypass <url> ')
    
def main():
    
    TOKEN = os.getenv('BOTAPIKEY')
    updater = Updater(token=TOKEN, use_context=True)
    dispatcher = updater.dispatcher
    
    bypass_handler = CommandHandler('bypass', bypass)
    start_handler = CommandHandler('start',start)

    dispatcher.add_handler(bypass_handler)
    dispatcher.add_handler(start_handler)

    PORT = int(os.environ.get('PORT', '443'))
    HOOK_URL = 'https://bypassertgbot-eqqgxx.codecapsules.co.za' + '/' + TOKEN
    updater.start_webhook(listen='0.0.0.0', port=PORT, url_path=TOKEN, webhook_url=HOOK_URL)
    updater.idle()

if __name__ == '__main__':
    main()
