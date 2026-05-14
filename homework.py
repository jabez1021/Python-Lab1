from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from docx import Document
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    driver.get('https://finance.naver.com/sise/')
    elem = driver.find_element(By.ID, 'popularItemList')
    childs = elem.find_elements(By.TAG_NAME, 'li')

    for child in childs:
        print(child.text)
except Exception as e:
    print(e)
finally:
    driver.quit()