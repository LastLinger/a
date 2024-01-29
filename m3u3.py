import sqlite3 
import telebot
import datetime
API_TOKEN = 'ф'

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Hi there, I am EchoBot.
I am here to echo your kind words back to you. Just say anything nice and I'll say the exact same thing to you!\
""")


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    con = sqlite3.connect('memory.db')
    user_id = message.from_user.id
    mes = message.text
    date = datetime.datetime.fromtimestamp(message.date)
    chat_id = message.chat.id
    with con:
        con.execute('insert into memory(user_id,massage,date,chat_id) values(?,?,?,?)',(user_id,mes,date,chat_id))
    bot.reply_to(message, message.text)


bot.infinity_polling()