import telebot
import config

bot = telebot.TeleBot(config.TOKEN)


"""@bot.message_handler(commands=['remember'])
def remember(message):

	wr = open('remember.txt', 'w')
		#wword = int(rword) + 1
	wr.write('1')
	wr.close()"""

@bot.message_handler(commands=['Remember'])
def Remember(message):
	textuser = message.text
	wr = open('Remember.txt', 'w')
	wr.write('1')
	wr.close()
	bot.send_message(message.chat.id, 'Write word: ')

@bot.message_handler(commands=['Read'])
def WordsRead(message):
	textuser = message.text
	Words = open('Words.txt', 'r')
	d = Words.read()
	bot.send_message(message.chat.id, d)
	Words.close()


"""@bot.message_handler(content_types=['text'])
def test(message):
	bot.send_message(message.chat.id, 'test ')
	textuser = message.text
	if textuser == 'remember':

		a = open('remember.txt', 'w')
		c = a.read()
		if c == '1':
			test1(message)

		a.close()
	textuser = message.text
	bot.send_message(message.chat.id, 'test ' + textuser)
	if textuser == 'Hi':
		
		re = open('Words.txt', 'r')
		rword = re.read()
		re.close()

		wr = open('Words.txt', 'w')
		#wword = int(rword) + 1
		wr.write(textuser)
		wr.close()
"""

@bot.message_handler(content_types=['text'])
def text(message):
	textuser = message.text
	a = open('Remember.txt', 'r')
	c = a.read()
	a.close()
	if c == '2':
		wr = open('Words.txt', 'a')	
		wr.write(textuser + '\n')
		wr.close()
		kick = open('Remember.txt', 'w')
		kick.write('0')
		kick.close()
		bot.send_message(message.chat.id, 'Теперь слово записано в словарь')
	if c == '1':
		wr = open('Words.txt', 'a')	
		wr.write(textuser + ' - ')
		wr.close()
		kick = open('Remember.txt', 'w')
		kick.write('2')
		kick.close()
		bot.send_message(message.chat.id, 'Good, а теперь перевод: ')
	

	

#RUN
bot.polling(none_stop=True)





"""
re = open('Words.txt', 'r')
rword = re.read()
re.close()

wr = open('Words.txt', 'w')
wword = int(rword) + 1
wr.write(str(wword))
wr.close()
"""
