import telebot
import wikipedia
bot = telebot.TeleBot(" Telegram API ")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    print("Hello There")
    bot.reply_to(message,"Hello There")

"""
normal message handling  // Commented out
@bot.message_handler(func=lambda message: True)
def send_welcome(message):
    bot.reply_to(message,message.text)
"""
@bot.message_handler(func=lambda message: True)
def start(message):
    try:
        print(wikipedia.summary(message.text))  # printed in the console
        bot.reply_to(message, wikipedia.summary(message.text))
    except:
        print(" some error occured  ")   #This will be printed in the console
        bot.reply_to(message,"no results found")


bot.polling()
