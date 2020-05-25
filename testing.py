import telebot
import config

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(content_types=['text'])
def text(message):
	textuser = message.text
	userid = message.from_user.id
	bot.send_message(message.chat.id, userid)




bot.polling(none_stop=True)