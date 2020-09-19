import telebot
from telebot import types

#main variables
TOKEN = "1393916807:AAELsjsCnr8rOeCul7OpwdI7areNUT-hOqA"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привіт, почуваєш себе безграмотним рагулем коли знову не можеш згадати повне ім\'я свого викладача, цей бот допоможе тобі, напиши прізвище викладача')
@bot.message_handler(commands=['help'])
def help_message(message):
    bot.send_message(message.chat.id, 'Впиши прізвиче викладача і бот видаcть тобі повне його ім')
    bot.send_animation(message.chat.id, 'CAACAgIAAxkBAAIGMl9HdIMGsjO6HBTq5titmJ4aehPXAAIPAAOAAAGnEe948HZJP4vlGwQ')

@bot.message_handler(content_types=['text'])
def get_text_message(message):
    if message.text.lower() == "костик":
        bot.send_message(message.from_user.id, text='Доцент Костик Людмила Василівна')
    if message.text.lower() == "корчак":
        bot.send_message(message.from_user.id, text='Доцент Корчак Юрій Михайлович')
    if message.text.lower() == "лучечко":
        bot.send_message(message.from_user.id, text='Доцент Лучечко Андрій Петрович')
    if message.text.lower() == "павлик":
        bot.send_message(message.from_user.id, text='Професор Павлик Боглан Васильович')
    if message.text.lower() == "лучечко":
        bot.send_message(message.from_user.id, text='Доцент Лучечко Андрій Петрович')
    if message.text.lower() == "була":
        bot.send_message(message.from_user.id, text='Асистент Була Світлана Петрівна')
    if message.text.lower() == "герцик":
        bot.send_message(message.from_user.id, text='Доцент Герцик Оксана Миронівна')
    if message.text.lower() == "лис":
        bot.send_message(message.from_user.id, text='Доцент Лис Роман Миронович')
    if message.text.lower() == "доцент":
        bot.send_message(message.from_user.id, text='Доцент Герцик Оксана Миронівна')
    if message.text.lower() == "Ковалишин":
        bot.send_message(message.from_user.id, text='Асистент Герцик Оксана Миронівна')



bot.polling(none_stop=True)
