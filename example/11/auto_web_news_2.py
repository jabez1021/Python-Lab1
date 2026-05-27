from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    driver.get('https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=105')
    elem = driver.find_element(By.ID, '_rankingList0')
    childs = elem.find_elements(By.TAG_NAME, 'li')

    for child in childs:
        print(child.text)
except Exception as e:
    print(e)
finally:
    driver.quit()
