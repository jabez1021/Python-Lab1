import telegram
token = '발급받은 토큰'
bot = telegram.Bot(token)
bot.send_message(채팅ID, '메시지')