import telebot

TOKEN = '993151135:AAH9A7tLqxS83FJnL0SLuF2HRFhJrj_-PCw' #bot token @BotFather

bot = telebot.TeleBot(config.TOKEN)

bot.message_handler(commands=['sart'])
def start(message):
	bot.send_message(message.chat.id, "Hello, {0.first_name}!\nМеня зовут {1.first_name}. Я являюсь ботом, для запоминания английского языка, которого ты можешь обучить.")
	print('start')
#config.welcome(message)

@bot.message_handler(commands=['start'])
def sart(message):
	print('start')
	bot.send_message(message.chat.id, "Hello, {0.first_name}!\nМеня зовут {1.first_name}. Я являюсь ботом, для запоминания английского языка, которого ты можешь обучить.")
	
	

@bot.message_handler(commands=['help'])
def helpcomand(message):
	H = open('Help.txt', 'r')
	Help = H.read()
	H.close()
	bot.send_message(message.chat.id, Help)

@bot.message_handler(commands=['remember'])
def Remember(message):
	textuser = message.text
	wr = open('Remember.txt', 'w')
	wr.write('1')
	wr.close()
	bot.send_message(message.chat.id, 'Write word: ')

@bot.message_handler(commands=['read'])
def WordsRead(message):
	textuser = message.text
	userid = str(message.from_user.id)
	Words = open("Words_user/" + userid + ".txt", 'r')
	d = Words.read()
	bot.send_message(message.chat.id, d)
	Words.close()


@bot.message_handler(content_types=['text'])
def text(message):
	textuser = message.text
	a = open('Remember.txt', 'r')
	c = a.read()
	a.close()
	if c == '2':
		userid = str(message.from_user.id)
		wr = open("Words_user/" + userid + ".txt", 'a')
		wr.write(textuser + '\n')
		wr.close()
		kick = open('Remember.txt', 'w')
		kick.write('0')
		kick.close()
		bot.send_message(message.chat.id, 'Теперь слово записано в словарь')
	if c == '1':
		userid = str(message.from_user.id)
		wr = open("Words_user/" + userid + ".txt", 'a')	
		wr.write(textuser + ' - ')
		wr.close()
		kick = open('Remember.txt', 'w')
		kick.write('2')
		kick.close()
		bot.send_message(message.chat.id, 'Good, а теперь перевод: ')
	else:
		bot.send_message(message.chat.id, "I am don't understand")



#RUN
bot.polling(none_stop=True)