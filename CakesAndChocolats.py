import os
import sys
import logging #Ver lo que hace el Bot
import telegram
from telegram import ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


logging.basicConfig(
    level = logging.INFO, format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s,"
)

logger = logging.getLogger()

#solicito TOKEN
TOKEN = os.getenv("TOKEN")
mode = os.getenv("MODE")

if (mode == "dev"):
    #Acceso local
    def run(updater):
        updater.start_polling() #pregunta sobre mensajes entrantes
        print("BOT CARGADO")
        updater.idle() #terminar bot con ctrl + c
elif (mode == "prod"):
    #Acceso HEROKU (Produccion)
    def run(updater):
        PORT = int(os.environ.get("PORT","8443"))
        HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME")
        updater.start_webhook(listen="0.0.0.0", port=PORT, url_path=TOKEN)
        updater.bot.set_webhook(f"https://{HEROKU_APP_NAME}.herokuapp.com/{TOKEN}")
else:
    logger.info("No se especifico el MODE.")
    sys.exit()

""" Desde Aca """

#https://stackoverflow.com/questions/48199699/telegram-bot-keyboardbutton-on-callbackqueryhandler-python

#Leer mensajes
def echo(update,context):
    bot = context.bot
    updatemsg = getattr(update, 'message', None)
    #Obtener Id del mensaje
    messageId = updatemsg.message_id
    ChatId = update.message.chat_id
    userName = update.effective_user["first_name"]
    #Obtener texto que ingreso el usuario
    text = update.message.text
    logger.info(f'El usuario {userName} ah enviado un nuevo mensaje.')

    informacionbot = 'Informacion sobre el bot'
    nuestroWA = 'Nuestro WhatsApp'
    listprecios = 'Lista de precios'
    botWA = 'Bot para WhatsApp'
    RS = 'Redes Sociales'
    programador = 'Programador del bot'
    datos = "Mas..."
    menu = 'Menu'
    atrasmas = "Atras"

    if informacionbot in text:
        getBotInfo(update, context)
    elif nuestroWA in text:
        WhatsApp(update, context)
    elif listprecios in text:
        Lista(update, context)
    elif botWA in text:
        WhatsAppBot(update, context)
    elif RS in text:
        Redes(update, context)
    elif programador in text:
        Programador(update, context)
    elif menu in text:
        Menu(update, context)
    elif datos in text:
        Mas(update, context)
    elif atrasmas in text:
        Mas(update, context)
    else:
        update.message.reply_text(f'Lo siento pero no entendi.')
        logger.info(f'El usuario {userName} introdujo un comando no valido.')



def getBotInfo(update, context):
    bot = context.bot
    ChatId = update.message.chat_id
    userName = update.effective_user["first_name"]
    # Menu keyboard
    updatemsg = getattr(update, 'message', None)
    #Obtener Id del mensaje
    messageId = updatemsg.message_id
    text = update.message.text
    keyboard = []
    keyboard.append([KeyboardButton(f'🔙 Atras', callback_data='8'), KeyboardButton(f'📝 Menu', callback_data='7')])
    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True, resize_keyboard=True)
    # Fin Menu
    logger.info(f'El Usuario {userName} Id:{ChatId} ah solicitado informacion sobre el bot')
    bot.sendMessage(
        chat_id = ChatId,
        parse_mode = "HTML",
        text = f'Soy un bot creado para enviar informacion sobre:\n<b>Cakes and Chocolat´s</b>'
    )
    update.message.reply_text('Regresar al menu?', reply_markup=reply_markup)
    


def Menu(update, context):
    bot = context.bot
    ChatId = update.message.chat_id
    userName = update.effective_user["first_name"]
    logger.info(f'El Usuario {userName} Id:{ChatId} ah accedido al menu')
    #update.message.reply_text(f'*****Menu*****\nElige una de estas opciones:\n1-Informacion sobre el bot: /Info\n2-Nuestro WhatsApp: /WhatsApp\n3-Lista de precios: /Lista\n4-Bot para WhatsApp: /WhatsAppBot\n5-Redes Sociales: /Redes\nProgramador del bot: /Creador')
    keyboard = []
    keyboard.append([KeyboardButton(f'💬 Nuestro WhatsApp', callback_data='2'), KeyboardButton(f'🏷️ Lista de precios', callback_data='3')])
    keyboard.append([KeyboardButton(f'🌐 Redes Sociales', callback_data='5'), KeyboardButton(f'🤖 Bot para WhatsApp', callback_data='4')])
    keyboard.append([KeyboardButton(f'Mas...', callback_data='5')])
    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True, resize_keyboard=True)
    update.message.reply_text('*****📝 Menu 📝*****\nElige una de las siguientes opciones:',  reply_markup=reply_markup)


def Mas(update, context):
    bot = context.bot
    ChatId = update.message.chat_id
    userName = update.effective_user["first_name"]
    logger.info(f'El Usuario {userName} Id:{ChatId} ah solicitado mas informacion sobre el bot')
    keyboard = []
    keyboard.append([KeyboardButton(f'📋 Informacion sobre el bot', callback_data='1'), KeyboardButton(f'💻 Programador del bot', callback_data='6')])
    keyboard.append([KeyboardButton(f'📝 Menu', callback_data='7')])
    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True, resize_keyboard=True)
    update.message.reply_text('Seleccione una opcion:',  reply_markup=reply_markup)



def start(update, context):
    bot = context.bot
    ChatId = update.message.chat_id
    userName = update.effective_user["first_name"]
    logger.info(f'El Usuario {userName} Id:{ChatId} ah iniciado el bot')
    #update.message.reply_text(f'Elige una de estas opciones:\n1-Informacion sobre el bot: /Info\n2-Nuestro WhatsApp: /WhatsApp\n3-Lista de precios: /Lista\n4-Bot para WhatsApp: /WhatsAppBot\n5-Redes Sociales: /Redes\nProgramador del bot: /Creador')
    keyboard = []
    keyboard.append([KeyboardButton(f'💬 Nuestro WhatsApp', callback_data='2'), KeyboardButton(f'🏷️ Lista de precios', callback_data='3')])
    keyboard.append([KeyboardButton(f'🌐 Redes Sociales', callback_data='5'), KeyboardButton(f'🤖 Bot para WhatsApp', callback_data='4')])
    keyboard.append([KeyboardButton(f'Mas...', callback_data='5')])
    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True, resize_keyboard=True)
    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True, resize_keyboard=True)
    update.message.reply_text('!Hola gracias por llamarme!\nElige una de las siguientes opciones:',  reply_markup=reply_markup)


def WhatsApp(update, context):
    bot = context.bot
    ChatId = update.message.chat_id
    userName = update.effective_user["first_name"]
    # Menu keyboard
    updatemsg = getattr(update, 'message', None)
    #Obtener Id del mensaje
    messageId = updatemsg.message_id
    text = update.message.text
    keyboard = []
    keyboard.append([KeyboardButton(f'📝 Menu', callback_data='7')])
    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True, resize_keyboard=True)
    # Fin Menu
    logger.info(f'El Usuario {userName} Id:{ChatId} ah solicitado el WhatsApp')
    bot.sendMessage(
        chat_id = ChatId,
        parse_mode = "HTML",
        text = f'Este es nuestro WhatsApp\n<a href="https://api.whatsapp.com/send?phone=+54115328-7043">Cakes And Chocolat´s WhatsApp</a>\nSi quieres realizar una compra puedes hacerlo mediante el enlace\n<b>Envios a CABA, precio no incuido.</b>'
    )
    update.message.reply_text('Regresar al menu?', reply_markup=reply_markup)


def WhatsAppBot(update, context):
    bot = context.bot
    ChatId = update.message.chat_id
    userName = update.effective_user["first_name"]
    # Menu keyboard
    updatemsg = getattr(update, 'message', None)
    #Obtener Id del mensaje
    messageId = updatemsg.message_id
    text = update.message.text
    keyboard = []
    keyboard.append([KeyboardButton(f'🏷️ Lista de precios', callback_data='3'), KeyboardButton(f'💬 Nuestro WhatsApp', callback_data='2')])
    keyboard.append([KeyboardButton(f'📝 Menu', callback_data='7')])
    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True, resize_keyboard=True)
    # Fin Menu
    logger.info(f'El Usuario {userName} Id:{ChatId} ah solicitado el Bot de WhatsApp')
    update.message.reply_text(f'Aun estamos trabajando en esta funcion.')
    update.message.reply_text('Mientras tanto puedes ver otras opciones', reply_markup=reply_markup)


def Redes(update, context):
    bot = context.bot
    ChatId = update.message.chat_id
    userName = update.effective_user["first_name"]
    # Menu keyboard
    updatemsg = getattr(update, 'message', None)
    #Obtener Id del mensaje
    messageId = updatemsg.message_id
    text = update.message.text
    keyboard = []
    keyboard.append([KeyboardButton(f'📝 Menu', callback_data='7')])
    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True, resize_keyboard=True)
    # Fin Menu
    logger.info(f'El Usuario {userName} Id:{ChatId} ah solicitado las redes')
    bot.sendMessage(
        chat_id = ChatId,
        parse_mode = "HTML",
        text = f'Estas son nuestras Redes Sociales\nFacebook: <a href="https://www.facebook.com/Cakes-Chocolats-132144366827721">Cakes And Chocolat´s</a>'
    )
    update.message.reply_text('Regresar al menu?', reply_markup=reply_markup)



def Lista(update, context,filename=None):
    bot = context.bot
    ChatId = update.message.chat_id
    userName = update.effective_user["first_name"]
    # Menu keyboard
    updatemsg = getattr(update, 'message', None)
    #Obtener Id del mensaje
    messageId = updatemsg.message_id
    text = update.message.text
    keyboard = []
    keyboard.append([KeyboardButton(f'📝 Menu', callback_data='7')])
    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True, resize_keyboard=True)
    # Fin Menu
    logger.info(f'El Usuario {userName} Id:{ChatId} ah solicitado las listas')
    update.message.reply_text(f'Aguarde un momento por favor. El archivo se esta descargando...')
    bot.sendDocument(chat_id=ChatId, document=open('ListaTortasNueva.pdf', 'rb'), filename="Lista de precios.pdf")
    logger.info(f'Lista de precios enviada a {userName} Id:{ChatId}')
    update.message.reply_text('Regresar al menu?', reply_markup=reply_markup)


def Programador(update, context):
    bot = context.bot
    ChatId = update.message.chat_id
    userName = update.effective_user["first_name"]
    # Menu keyboard
    updatemsg = getattr(update, 'message', None)
    #Obtener Id del mensaje
    messageId = updatemsg.message_id
    text = update.message.text
    keyboard = []
    keyboard.append([KeyboardButton(f'🔙 Atras', callback_data='8'), KeyboardButton(f'📝 Menu', callback_data='7')])
    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True, resize_keyboard=True)
    # Fin Menu
    logger.info(f'El Usuario {userName} Id:{ChatId} ah solicitado datos del programador')
    bot.sendMessage(
        chat_id = ChatId,
        parse_mode = "HTML",
        text = f'Creador del bot\n<a href="https://web.telegram.org/#/im?p=@TommySR">@TommySR</a>'
    )
    update.message.reply_text('Seleccione una opcion:', reply_markup=reply_markup)


if __name__ == "__main__":
    #Obtener informacion del bot
    myBot = telegram.Bot(token = TOKEN)
#    print(myBot.getMe())

#updater se conecta y recibe mensajes
updater = Updater(myBot.token, use_context=True)

#create dispatcher (comandos que el bot va a recibir)
dp = updater.dispatcher

#create command (manejador)
dp.add_handler(CommandHandler("start", start))
# Lee los mensajes
dp.add_handler(MessageHandler(Filters.text, echo))

""" Hasta aca """

run(updater)