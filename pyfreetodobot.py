import telebot

token = ""

bot = telebot.TeleBot(token)

word = "Денис"

@bot.message_handler(content_types=["text"])
def echo(string):
    if word in string.text:
        text = "Ба! Знакомые лица"
    else:
        text = string.text
    bot.send_message(string.chat.id, text)

bot.polling(none_stop=True)