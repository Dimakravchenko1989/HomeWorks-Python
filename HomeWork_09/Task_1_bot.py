# Задача 1. Напишите Бота, удаляющего из текста все слова, содержащие "абв". (Ввод от пользователя)
# Пример:
# привет приабвет ограбпв
# Ответ:
# привет ограбпв


from telegram import Bot, Update
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters, CallbackContext)

# Токен моего телеграм бота
token = '5564736708:AAGdXYl50Iqt2i5w-bv_VZRymvFOrRxOvNg'

bot = Bot(token)
updater = Updater(token)
dispatcher = updater.dispatcher

# Функция для старта нашего бота

def start(update: Update, context: CallbackContext):
    context.bot.send_message(update.effective_chat.id, 'Привет!\n\
Напиши мне сообщение, и я удалю из него слова,\n\
содержащие "абв"')

# Функция для удаления слов, содержащих "абв"

def delete_text(update: Update, context: CallbackContext):
    message_text = update.message.text.split()
    corrected_text = [i for i in message_text if 'абв' not in i]
    corrected_text = ' '.join (corrected_text) if corrected_text else 'Работа завершена!'
    context.bot.send_message(update.effective_chat.id,corrected_text)

# Обучаем нашего бота

start_handler = CommandHandler('start', start)
message_handler = MessageHandler(Filters.text, delete_text)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(message_handler)


updater.start_polling()
updater.idle()