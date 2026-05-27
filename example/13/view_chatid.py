import telegram

token = '962058964:AAG5G53iMXjqjHWPE8d17FDgnE0lC_-pnhA'
bot = telegram.Bot(token=token)
a = bot.getUpdates()
print(a[-1].message.chat.id)
