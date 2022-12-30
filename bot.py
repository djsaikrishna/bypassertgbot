"""
@author  KATPER
@date    20-12-2022
@desc
    Ad link bypasser bot which can also bypass gdtot links
@change
    basic bot created ----------------------------------- 20-12-2022
    added gdtot support --------------------------------- 21-12-2022
    added check if url is not provided ------------------ 22-12-2022
    added icons and emojis ------------------------------ 23-12-2022
    added bot start info display in logs ---------------- 24-12-2022
    added logging info for each task in logs ------------ 28-12-2022
    added more formatting ------------------------------- 28-12-2022
    added status msg when link is being converted ------- 28-12-2022
"""
from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
from telegram import Update
from telegram.message import Message
import telegram
from tld import get_tld
import PyBypass as bypasser
import PyBypass
import os
import sys
import logging
import requests


#Made with Love by KATPER
BANNER = """

______       _     _             _   __  ___ ___________ ___________ 
| ___ \     | |   | |           | | / / / _ \_   _| ___ \  ___| ___ \
| |_/ / ___ | |_  | |__  _   _  | |/ / / /_\ \| | | |_/ / |__ | |_/ /
| ___ \/ _ \| __| | '_ \| | | | |    \ |  _  || | |  __/|  __||    / 
| |_/ / (_) | |_  | |_) | |_| | | |\  \| | | || | | |   | |___| |\ \ 
\____/ \___/ \__| |_.__/ \__, | \_| \_/\_| |_/\_/ \_|   \____/\_| \_|
                          __/ |                                      
                         |___/                                       
"""
#https://patorjk.com/software/taag/#p=testall&f=Graffiti&t=Bot%20by%20KATPER

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logging.info('Starting Bot...')
logging.info('BANNER')

def sendMessage(text: str, bot, update: Update):
        return bot.send_message(update.message.chat_id,
                                reply_to_message_id=update.message.message_id,
                                text=text, parse_mode='HTMl',
                                disable_web_page_preview=True)
 
        
def deleteMessage(bot, message: Message):
        bot.delete_message(chat_id=message.chat.id,
                           message_id=message.message_id)

def url_checker(url) -> bool:
	try:
		#Get Url
		get = requests.get(url)
		# if the request succeeds 
		if get.status_code == 200:
			return True
		else:
			return False

def bypass(update, context):
    if len(context.args) == 0 or : #If empty command is sent without url
        logging.info("Error: No Link provided!")
        update.message.reply_text(f"➖➖➖➖➖➖➖➖➖➖➖➖\n"
                            f" *‼ No link provided!*\n"
                            f"➖➖➖➖➖➖➖➖➖➖➖➖\n\n"
                            f"👉 Send command as <code>/bypass url</code>\n\n\n"
                            f"➖➖➖➖➖➖➖➖➖➖➖➖\n"
                            f" *Bot by KATPER*\n"
                            f"➖➖➖➖➖➖➖➖➖➖➖➖\n\n",
                            parse_mode="Markdown",
                            disable_web_page_preview=True,
                            quote=True)
                            
    elif url_checker(context.args) == False:
        logging.info("URL does not exist!")
        update.message.reply_text(f"➖➖➖➖➖➖➖➖➖➖➖➖\n"
                            f" *‼ Link does not exist!*\n"
                            f"➖➖➖➖➖➖➖➖➖➖➖➖\n\n"
                            f"👉 Your link does not exist!\nCheck any typo error and try again.\n\n\n"
                            f"➖➖➖➖➖➖➖➖➖➖➖➖\n"
                            f" *Bot by KATPER*\n"
                            f"➖➖➖➖➖➖➖➖➖➖➖➖\n\n",
                            parse_mode="Markdown",
                            disable_web_page_preview=True,
                            quote=True)

    else:
        url = context.args[0]
        res = get_tld(url, as_object=True)
        logging.info(f"Link detected: {url}")
    
    if res.domain in ["gplinks","try2link","adf","link-center","bitly","ouo","shareus","shortly","tinyurl","thinfi","hypershort","sirigan","gtlinks","theforyou","linkvertise","shortest","pkin","tekcrypt","short2url","rocklinks","rocklinks","moneykamalo","easysky","indianshortner","crazyblog","tnvalue","shortingly","dulink","bindaaslinks","pdiskshortener","mdiskshortner","earnl","rewayatcafe","crazyblog","bitshorten","rocklink","droplink","earn4link","tnlink","ez4short","xpshort","vearnl","adrinolinks","techymozo","linkbnao","linksxyz","short-jambo","droplink","linkpays","pi-l","tnlink","open2get","anonfiles","antfiles","1fichier","gofile","hxfile","krakenfiles","mdisk","mediafire","pixeldrain","racaty","sendcm","sfile","solidfiles","sourceforge","uploadbaz","uploadee","uppit","userscloud","wetransfer","yandex","zippyshare","fembed","mp4upload","streamlare","streamsb","streamtape","appdrive","gdtot","hubdrive","sharerpw"]:
        if (res.domain == "link-center"):
            msg = sendMessage(f"⫸ <b>Processing:</b> <code>{url}</code>", context.bot, update)
            logging.info(f"Processing: {url}")
            try:
                bypassed_link = bypasser.bypass(url, name="linkvertise")
            except:
                deleteMessage(context.bot, msg)
                update.message.reply_text("🔴 Sorry, Something went wrong!",quote=True)
                logging.info("🔴 Error: Something went wrong!")
            deleteMessage(context.bot, msg)
            update.message.reply_text(f"➖➖➖➖➖➖➖➖➖➖➖➖\n"
                            f" *✅ Ad Link Bypassed!*\n"
                            f"➖➖➖➖➖➖➖➖➖➖➖➖\n\n"
                            f"👉 {bypassed_link}\n\n\n"
                            f"➖➖➖➖➖➖➖➖➖➖➖➖\n"
                            f" *Bot by KATPER*\n"
                            f"➖➖➖➖➖➖➖➖➖➖➖➖\n\n",
                            parse_mode="Markdown",
                            disable_web_page_preview=True,
                            quote=True)
            
            logging.info("Link bypassed successfully!")
        elif (res.domain == "gdtot"):
            msg = sendMessage(f"⫸ <b>Processing GDTOT:</b> <code>{url}</code>", context.bot, update)
            logging.info(f"Processing GDTOT: {url}")
            crypt = os.getenv('CRYPT') #CRYPT is env variable stored in codecapsules.io 
            try:
                bypassed_link = PyBypass.bypass(url, gdtot_crypt=crypt)
            except:
                deleteMessage(context.bot, msg)
                update.message.reply_text("🔴 Sorry, Something went wrong!",quote=True)
                logging.info("🔴 Error: Something went wrong!")
            deleteMessage(context.bot, msg)
            update.message.reply_text(f"➖➖➖➖➖➖➖➖➖➖➖➖\n"
                            f" *✅ GDTOT Link copied!*\n"
                            f"➖➖➖➖➖➖➖➖➖➖➖➖\n\n"
                            f"👉 {bypassed_link}\n\n\n"
                            f"➖➖➖➖➖➖➖➖➖➖➖➖\n"
                            f" *Bot by KATPER*\n"
                            f"➖➖➖➖➖➖➖➖➖➖➖➖\n\n",
                            parse_mode="Markdown",
                            disable_web_page_preview=True,
                            quote=True)
            logging.info("File copied to privided google account!")
        else:
            msg = sendMessage(f"⫸ <b>Processing:</b> <code>{url}</code>", context.bot, update)
            logging.info(f"Processing: {url}")
            try:
                bypassed_link = bypasser.bypass(url)
                
            except:
                deleteMessage(context.bot, msg)
                update.message.reply_text("🔴 Sorry, Something went wrong!",quote=True)
                logging.info("🔴 Error: Something went wrong!")
            deleteMessage(context.bot, msg)
            update.message.reply_text(f"➖➖➖➖➖➖➖➖➖➖➖➖\n"
                            f" *✅ Ad Link Bypassed!*\n"
                            f"➖➖➖➖➖➖➖➖➖➖➖➖\n\n"
                            f"👉 {bypassed_link}\n\n\n"
                            f"➖➖➖➖➖➖➖➖➖➖➖➖\n"
                            f" *Bot by KATPER*\n"
                            f"➖➖➖➖➖➖➖➖➖➖➖➖\n\n",
                            parse_mode="Markdown",
                            disable_web_page_preview=True,
                            quote=True)
            logging.info("Link bypassed successfully!")
    else:
        
        update.message.reply_text(f"➖➖➖➖➖➖➖➖➖➖➖➖\n"
                            f" *❌ Link not supported!*\n"
                            f"➖➖➖➖➖➖➖➖➖➖➖➖\n\n"
                            f"‼ Detected Domain: *{res.domain}*\n\n\n"
                            f"➖➖➖➖➖➖➖➖➖➖➖➖\n"
                            f" *Bot by KATPER*\n"
                            f"➖➖➖➖➖➖➖➖➖➖➖➖\n\n",
                            parse_mode="Markdown",
                            disable_web_page_preview=True,
                            quote=True)
        logging.info("Error: Link not supported!")

   
def start(update: Update, context: CallbackContext):
    update.message.reply_text("Hello, This is bypasser bot made by KATPER SAHAB")
    logging.info("/start command!")

"""
def zip(update: Update, context: CallbackContext):
    update.message.reply_text("This is zip command")
    logging.info("/zip command!")
    ASK_FIRST = input("\nBoth of your source and destination is GD/TD??\n1. Yes, both are GD/TD\n2. Noo. Its some other cloud storage\nChoose either 1/2:")
    if ASK_FIRST not in ["1", "2"]:
        print("Wrong input 🤬. Exiting!!!")
        sys.exit()
        if ASK_FIRST == "1":
            CLONE_METHOD = "gclone"
            SAS = input("Do you have service accounts and want to use in gclone? 🤔\n1. Yes\n2. No\nChoose either Y/N:")
                if SAS not in ["Y", "N"]:
                    print("wrong input 🤬. Exiting!!!")
                    sys.exit()
                if SAS == "Y":
                    text_file = open("clone.conf", "w")
                    text_file.write("[gs]\ntype = drive\nscope = drive\nservice_account_file = accounts/1.json\nservice_account_file_path = accounts/")
                    text_file.close()
                    RCLONE_PATH = ("/bot/clone.conf")
                else:
                    RCLONE_PATH = "/bot/.config/rclone/rclone.conf"
        else:
            CLONE_METHOD = "rclone"
            RCLONE_PATH = "/bot/.config/rclone/rclone.conf"
                if RCLONE_PATH == "/bot/.config/rclone/rclone.conf":
                    if not os.path.isfile("/bot/.config/rclone/rclone.conf"):
                        print("rclone.conf not found at /bot/.config/rclone/rclone.conf.\nYou can't use rclone/gclone without rclone.conf\nExiting!!!")
                        sys.exit()

    ASK_SECOND = input("Want to split? 👀\n1. Yes\n2. No\nChoose either Y/N:")
        if ASK_SECOND not in ["Y", "N"]:
        print("Wrong input 🤬. Exiting!!!")
        sys.exit()
            if ASK_SECOND == "Y":
                sValue = input("Enter split size, Ex 500m or 10g")
        else:
            print("Noice, Let's go to next step\n\n")

    ASK_THIRD = input ("What kind of output compressed file you want? 🤔\n1. zip\n2. 7z\n3. rar\nChoose either 1/2/3:")
        if ASK_THIRD not in ["1", "2", "3"]:
            print("Wrong input 🤬. Exiting!!!")
            sys.exit()

  
    #Taking inputs from users
    DESIRED_FOLDER_NAME = input("Provide Folder name:\n\nWhat's this?\nIt is the folder name, which user will get after extraction.So...please select an appropriate name")
    DESIRED_FILE_NAME = input("Provide desired name for the resultant compressed file (with file extension name):\n\nProvide appropriate file extention name according to options selected above, otherwise you will face errors")
    N = "/bot/files/"+DESIRED_FOLDER_NAME

        if CLONE_METHOD == "gclone":
            if SAS == "Y":
                SOURCE_ID = input("Provide source ID:")
                DESTINATION_ID = input("Provide Destination ID:")
                S = "gs:{"+SOURCE_ID+"}"
                D = "gs:{"+DESTINATION_ID+"}"
            elif SAS == "N":
                SOURCE_REMOTE = input("Provide Source remote:")
                SOURCE_ID = input("Provide source ID:")
                DESTINATION_REMOTE = input("Provide Destination remote:")
                DESTINATION_ID = input("Provide Destination ID:")
                S = SOURCE_REMOTE+":{"+SOURCE_ID+"}"
                D = DESTINATION_REMOTE+":{"+DESTINATION_ID+"}"
            else:
                SOURCE_REMOTE = input("Provide Source remote:")
                SOURCE_PATH = input("Provide source path:")
                DESTINATION_REMOTE = input("Provide Destination remote:")
                DESTINATION_PATH = input("Provide Destination path:")
                S = SOURCE_REMOTE+":"+SOURCE_PATH
                D = DESTINATION_REMOTE+":"+DESTINATION_PATH
  
    #Actual Process
    print("Creating required directories....")
    os.system("mkdir /bot/files && mkdir /bot/zip && mkdir /bot/files/+\"{0}\"".format(DESIRED_FOLDER_NAME))
    print("\n\nDownloading to local storage.......")
    os.system(CLONE_METHOD+" --config="+RCLONE_PATH+" copy \"{0}\" \"{1}\" -P -q --stats=10s".format(S,N))
    print("\n\nStarted the compression.....")
    
        if ASK_SECOND == "Y":
            if ASK_THIRD in ["1","2"]:
                os.system("cd /bot/files && 7z a -mx=1 -v{0} /bot/zip/\"{1}\" ./\"{2}\" ".format(sValue,DESIRED_FILE_NAME,DESIRED_FOLDER_NAME))
            else:
                os.system("cd /bot/files && rar a -m0 -v{0} /bot/zip/\"{1}\" ./\"{2}\" ".format(sValue,DESIRED_FILE_NAME,DESIRED_FOLDER_NAME))
        else:
            if ASK_THIRD in ["1","2"]:
                os.system("cd /bot/files && 7z a -mx=1 /bot/zip/\"{0}\" ./\"{1}\" ".format(DESIRED_FILE_NAME,DESIRED_FOLDER_NAME))
            else:
                os.system("cd /bot/files && rar a -m0 /bot/zip/\"{0}\" ./\"{1}\" ".format(DESIRED_FILE_NAME,DESIRED_FOLDER_NAME))
    
    print("\n\nStarted uploading......")
    os.system(CLONE_METHOD+" --config="+RCLONE_PATH+" move /bot/zip \"{0}\" -P -q --stats=10s".format(D))
    print("\n\nCleaning local storage....")
    os.system("rm -r /bot/files && rm -r /bot/zip")

"""    

def owner(update: Update, context: CallbackContext):
    update.message.reply_text("Owner of this bot is 💫 KATPER SAHAB")
    logging.info("/owner command!")

def help(update: Update, context: CallbackContext):
    update.message.reply_text(f"➖➖➖➖➖➖➖➖➖➖➖➖\n"
                            f" *❓ HELP*\n"
                            f"➖➖➖➖➖➖➖➖➖➖➖➖\n\n"
                            f"type /bypass url \nSupported Sites: https://katb.in/abefuqetoxe",
                            parse_mode="Markdown",
                            disable_web_page_preview=True,
                            quote=True) 
    logging.info("/help command!")
    
def unknown_text(update: Update, context: CallbackContext):
    update.message.reply_text("Sorry I can't recognize you , you said '%s'" % update.message.text)
    logging.info("unknown command!")
  
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
    #updater.dispatcher.add_handler(CommandHandler('zip', zip))
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
