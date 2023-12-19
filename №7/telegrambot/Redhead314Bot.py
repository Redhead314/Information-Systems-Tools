import telebot

bot = telebot.TeleBot('6726418566:AAH1b8jpQbY-92i4DN7HuKSlGNhSeGLqzj4');

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Какую оценку поставить?":
        bot.send_message(message.from_user.id, "Потсавьте пожалуйста 4 :)")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Спросите у меня 'Какую оценку поставить?'")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")

bot.polling(none_stop=True, interval=0)



