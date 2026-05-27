from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    driver.get('http://naver.com')

    elem = driver.find_element(By.CLASS_NAME, 'query')

except Exception as e:
    print(e)
finally:
    driver.quit()
