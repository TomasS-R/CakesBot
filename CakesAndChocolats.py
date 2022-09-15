import os
import sys
import logging #Ver lo que hace el Bot
import time
import telegram
import gdown #Download file to GOOGLE DRIVE
from telegram import ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

vers="Beta 0.5"
fechavers = "14/09/2022"

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
    datos = 'Mas...'
    menu = 'Menu'
    atrasmas = 'Atras'
    descarga = 'Descargar PDF'
    online = 'Ver online'
    volveratras = 'Volver'

    if informacionbot in text:
        getBotInfo(update, context)
    elif nuestroWA in text:
        WhatsApp(update, context)
    elif listprecios in text or volveratras in text:
        Lista(update, context)
    elif botWA in text:
        WhatsAppBot(update, context)
    elif RS in text:
        Redes(update, context)
    elif programador in text:
        Programador(update, context)
    elif menu in text:
        Menu(update, context)
    elif datos in text or atrasmas in text:
        Mas(update, context)
    elif descarga in text:
        Descarga(update, context)
    elif online in text:
        VerOnline(update, context)
    else:
        update.message.reply_text(f'Lo siento pero no entendi. 😔')
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
    time.sleep(2)
    update.message.reply_text(f'Mi ultima Actualizacion fue el ' + fechavers + '. Y estoy en la version ' + vers)
    time.sleep(5)
    bot.sendMessage(
        chat_id = ChatId,
        parse_mode = "HTML",
        text = f'Estoy alojado en <a href="https://www.heroku.com/">Heroku</a> y programado en <a href="https://www.python.org/">Python 3.0</a>'
    )
    time.sleep(5)
    update.message.reply_text(f'¿Te cuento una curiosidad?')
    time.sleep(5)
    bot.sendMessage(
        chat_id = ChatId,
        parse_mode = "HTML",
        text = f'Mi especialidad es trabajar con <a href="https://www.google.com/intl/es/drive/">Google drive</a>!'
    )
    time.sleep(3)
    update.message.reply_text(f'Si! el programador en la ultima actualizacion me agrego esta funcionalidad! 😍')
    time.sleep(5)
    update.message.reply_text(f'Lo unico que hago es descargar la ultima version de la lista de precios actualizada desde Google Drive.')
    time.sleep(5)
    update.message.reply_text(f'Lo mejor es que lo hago automaticamente.')
    time.sleep(5)
    update.message.reply_text(f'Que genial ¿no?')
    time.sleep(2)
    link = 'https://tenor.com/view/mind-blow-galaxy-explode-boom-fireworks-gif-5139389'
    bot.sendAnimation(chat_id = update.effective_chat.id,animation = link)
    update.message.reply_text('¿Deseas regresar al menu?', reply_markup=reply_markup)

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
    update.message.reply_text('¡Hola ' + userName + ' gracias por llamarme!\nElige una de las siguientes opciones:',  reply_markup=reply_markup)

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
        text = f'Este es nuestro WhatsApp\n<a href="https://api.whatsapp.com/send?phone=+54115328-7043">Cakes And Chocolat´s WhatsApp</a>\nSi quieres realizar una compra puedes hacerlo mediante el enlace\n<b>Envios a CABA, precio del envio no incuido.</b>'
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

def Lista(update, context):
    bot = context.bot
    ChatId = update.message.chat_id
    userName = update.effective_user["first_name"]
    updatemsg = getattr(update, 'message', None)
    #Obtener Id del mensaje
    messageId = updatemsg.message_id
    text = update.message.text
    # Menu keyboard
    keyboard = []
    keyboard.append([KeyboardButton(f'Descargar PDF 📥', callback_data='5'), KeyboardButton(f'Ver online 🌐', callback_data='6')])
    keyboard.append([KeyboardButton(f'📝 Menu', callback_data='7')])
    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True, resize_keyboard=True)
    # Fin Menu
    logger.info(f'El Usuario {userName} Id:{ChatId} ah solicitado las listas')
    update.message.reply_text('Opciones:', reply_markup=reply_markup)

def VerOnline(update, context):
    bot = context.bot
    ChatId = update.message.chat_id
    userName = update.effective_user["first_name"]
    update.message.reply_text(f'Puede ver la lista en el siguiente link:')
    bot.sendMessage( chat_id = ChatId, parse_mode = "HTML", text = f'<a href="https://bit.ly/3xo8iYZ">VER LISTA ✔️</a>')
    # Menu keyboard
    keyboard = []
    keyboard.append([KeyboardButton(f'🔙 Volver', callback_data='12'), KeyboardButton(f'📝 Menu', callback_data='7')])
    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True, resize_keyboard=True)
    # Fin Menu
    logger.info(f'El Usuario {userName} Id:{ChatId} ah solicitado ver las listas de manera online')
    update.message.reply_text('Regresar al menu?', reply_markup=reply_markup)

def Descarga(update, context, filename=None):
    bot = context.bot
    ChatId = update.message.chat_id
    userName = update.effective_user["first_name"]
    update.message.reply_text(f'Aguarde un momento por favor.')
    update.message.reply_text(f'El archivo se esta descargando...')
    #url = 'https://drive.google.com/uc?id=1cQcwACnR646EfVX0ObXmKHvvdApxNaz_'
    #output = 'Lista.pdf'
    #doc = gdown.download(url, output, quiet=False)
    link = 'https://drive.google.com/uc?id=1cQcwACnR646EfVX0ObXmKHvvdApxNaz_'
    if (FileNotFoundError):
        time.sleep(5)
        update.message.reply_text(f'Ups! parece que hay un error en la descarga')
        time.sleep(5)
        update.message.reply_text(f'Puede ver la lista en el siguiente link:')
        time.sleep(2)
        bot.sendMessage( chat_id = ChatId, parse_mode = "HTML", text = f'<a href="https://bit.ly/3xo8iYZ">VER LISTA ✔️</a>')
        logger.info(f'El usuario {userName} Id:{ChatId} solicito descargar la lista pero hubo un error en la descarga')
    else:
        bot.sendDocument(chat_id = update.effective_chat.id, Document = link)
        #bot.sendDocument(chat_id=ChatId, document=open('lista.pdf', 'rb'), filename=output)
        update.message.reply_text(f'Esta es la ultima y mas reciente lista')
        logger.info(f'Lista de precios enviada a {userName} Id:{ChatId}')
    # Menu keyboard
    keyboard = []
    keyboard.append([KeyboardButton(f'🔙 Volver', callback_data='12'), KeyboardButton(f'📝 Menu', callback_data='7')])
    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True, resize_keyboard=True)
    # Fin Menu
    update.message.reply_text('Opciones:', reply_markup=reply_markup)

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
        text = f'Creador del bot\n@TommySR'
    )
    bot.sendMessage(
        chat_id = ChatId,
        parse_mode = "HTML",
        text = f'Tambien puedes ver mi perfil de GitHub:\n<a href="https://github.com/TomasS-R">GitHub Profile</a>'
    )
    bot.sendMessage(
        chat_id = ChatId,
        parse_mode = "HTML",
        text = f'O si quieres puedes ver:\n<a href="https://heylink.me/Tom%C3%A1sSR/">Mas sobre mi!</a>'
    )
    update.message.reply_text('Seleccione una opcion:', reply_markup=reply_markup)


if __name__ == "__main__":
    #Obtener informacion del bot
    myBot = telegram.Bot(token = TOKEN)
    #print(myBot.getMe())

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