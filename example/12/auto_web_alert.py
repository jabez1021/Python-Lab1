import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.alert import Alert

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    driver.get('https://www.w3resource.com/javascript/alert-example1.html')

    time.sleep(1)

    alert = Alert(driver)
    alert.accept()

    input()

except Exception as e:
    print(e)
finally:
    driver.quit()
