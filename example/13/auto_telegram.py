import telegram
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

msg = ''
try:
    driver.get('https://naver.com')
    
    elem = driver.find_element(By.ID, 'query')
    elem.send_keys('파이썬')
    elem.send_keys(Keys.RETURN)

    view = driver.find_element(By.LINK_TEXT, "VIEW")
    view.click()

    ul = driver.find_element(By.CLASS_NAME, '_list_base')
    blogs = ul.find_elements(By.XPATH, './li')

    for blog in blogs:
        title_tag = blog.find_element(By.CLASS_NAME, 'total_tit')
        msg += title_tag.text + '\n'

except Exception as e:
    print(e)
finally:
    driver.quit()

token = '962058964:AAG5G53iMXjqjHWPE8d17FDgnE0lC_-pnhA'
bot = telegram.Bot(token)
bot.send_message(57841042, msg)
