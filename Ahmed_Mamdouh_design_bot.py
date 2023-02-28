import telebot
from telebot import types 

TOKEN = '6138040690:AAEDnK8ntamcKR0d4KZLfQwXWVO6YceEqc0'
ABOUT_TEXT = """This bot is designed by Ahmed Adel, It can reply with links from youtube specifically related to """
bot = telebot.TeleBot(TOKEN)
def generate_buttons(bts_names, markup):
    for button in bts_names:
        markup.add(types.KeyboardButton(button))
    return markup
@bot.message_handler(commands=['start'])
def Design_choose(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    markup = generate_buttons(['line circle','two line circles','chess board','about'],markup)
    message = bot.reply_to("Design", """choose a design""",
                 reply_markup=markup)
    bot.register_next_step_handler(message,Design_choice)
def Design_choice(message):
        if message.text=="line circle":
            bot.reply_to(message, 'https://github.com/Ahmed8742/cs/blob/main/1.py')
            markup = types.ReplyKeyboardMarkup(row_width=2)
            Design = bot.reply_to(message, "Here is the link for it", reply_markup=markup)
        elif message.text=="two line circles":
            markup = types.ReplyKeyboardMarkup(row_width=2)
            bot.reply_to(message,'https://github.com/Ahmed8742/cs/blob/main/2.py')
            Design = bot.reply_to(message, "Here is the link for it", reply_markup=markup)
        elif message.text=="chess board":
            markup = types.ReplyKeyboardMarkup(row_width=2)
            bot.reply_to (message,'https://github.com/Ahmed8742/cs/blob/main/3.py')
            Design = bot.reply_to(message, "Here is the link for it", reply_markup=markup)
        bot.register_next_step_handler(message,Design_choose)
bot.infinity_polling()
