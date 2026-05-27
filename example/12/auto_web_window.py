from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    driver.get('https://www.quirksmode.org/js/popup.html#create')

    btn = driver.find_element(By.LINK_TEXT, "Open popup")
    btn.click()

    wins = driver.window_handles
    driver.switch_to.window(wins[1])

    print(driver.title)

    input()

except Exception as e:
    print(e)
finally:
    driver.quit()
