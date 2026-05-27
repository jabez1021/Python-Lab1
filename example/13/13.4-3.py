import telegram

token = '962058964:AAG5G53iMXjqjHWPE8d17FDgnE0lC_-pnhA'
bot = telegram.Bot(token=token)
bot.send_photo(57841042, open('사진 파일 경로', 'rb'))
