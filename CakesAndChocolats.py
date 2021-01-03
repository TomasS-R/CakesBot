import os
import sys
import logging #Ver lo que hace el Bot
import telegram
#from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageFilter, Filters

#Send or recibe
#https://stackoverflow.com/questions/60111361/how-to-download-a-google-drive-file-using-python-and-the-drive-api-v3

logging.basicConfig(
    level = logging.INFO, format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s,"
)

logger = logging.getLogger()

#solicito TOKEN
TOKEN = os.getenv("TOKEN")


def getBotInfo(update, context):
    bot = context.bot
    ChatId = update.message.chat_id
    userName = update.effective_user["first_name"]
    logger.info(f'El Usuario {userName} ah solicitado informacion sobre el bot')
    bot.sendMessage(
        chat_id = ChatId,
        parse_mode = "HTML",
        text = f'Soy un bot creado para enviar informacion sobre <b>Cakes and Chocolat´s</b>\nPara regresar al menu haz click aqui:\n/Menu'
    )


def Menu(update, context):
    bot = context.bot
    userName = update.effective_user["first_name"]
    logger.info(f'El Usuario {userName} ah accedido al menu')
    update.message.reply_text(f'*****Menu*****\nElige una de estas opciones:\n1-Informacion sobre el bot: /Info\n2-Nuestro WhatsApp: /WhatsApp\n3-Lista de precios: *Proximamente*\n4-Bot para WhatsApp: /WhatsAppBot\n5-Redes Sociales: /Redes')


def start(update, context):
    bot = context.bot
    userName = update.effective_user["first_name"]
    logger.info(f'El Usuario {userName} ah iniciado el bot')
    update.message.reply_text(f'!Hola gracias por llamarme!\nElige una de estas opciones:\n1-Informacion sobre el bot: /Info\n2-Nuestro WhatsApp: /WhatsApp\n3-Lista de precios: *Proximamente*\n4-Bot para WhatsApp: /WhatsAppBot\n5-Redes Sociales: /Redes')


def WhatsApp(update, context):
    bot = context.bot
    ChatId = update.message.chat_id
    userName = update.effective_user["first_name"]
    logger.info(f'El Usuario {userName} ah solicitado el WhatsApp')
    bot.sendMessage(
        chat_id = ChatId,
        parse_mode = "HTML",
        text = f'Este es nuestro WhatsApp\n<a href="https://api.whatsapp.com/send?phone=+54115328-7043">Cakes And Chocolat´s WhatsApp</a>\nSi quieres realizar una compra puedes hacerlo mediante el enlace\n<b>Envios a CABA, los precios no incluye envio</b>\nPara regresar al menu haz click aqui:\n/Menu'
    )


def WhatsAppBot(update, context):
    bot = context.bot
    userName = update.effective_user["first_name"]
    logger.info(f'El Usuario {userName} ah solicitado el WhatsApp')
    update.message.reply_text(f'Aun estamos trabajando en esta funcion\nMientras tanto puedes consultar los precios en: /lista\nO si tienes alguna duda nos puedes contactar aqui -> /WhatsApp\nPara regresar al menu haz click aqui:\n/Menu')


def Redes(update, context):
    bot = context.bot
    ChatId = update.message.chat_id
    userName = update.effective_user["first_name"]
    logger.info(f'El Usuario {userName} ah solicitado las redes')
    bot.sendMessage(
        chat_id = ChatId,
        parse_mode = "HTML",
        text = f'Estas son nuestras Redes Sociales\nFacebook: <a href="https://www.facebook.com/Cakes-Chocolats-132144366827721">Cakes And Chocolat´s</a>'
    )


if __name__ == "__main__":
    #Obtener informacion del bot
    myBot = telegram.Bot(token = TOKEN)
#    print(myBot.getMe())

#updater se conecta y recibe mensajes
updater = Updater(myBot.token, use_context=True)

#create dispatcher (comandos que el bot va a recibir)
dp = updater.dispatcher

#create command (manejador)
dp.add_handler(CommandHandler("Info", getBotInfo))
dp.add_handler(CommandHandler("start", start))
dp.add_handler(CommandHandler("Menu", Menu))
dp.add_handler(CommandHandler("WhatsApp", WhatsApp))
dp.add_handler(CommandHandler("WhatsAppBot", WhatsAppBot))
dp.add_handler(CommandHandler("Redes", Redes))

updater.start_polling() #pregunta sobre mensajes entrantes
print("BOT CARGADO")
updater.idle() #terminar bot con ctrl + c
