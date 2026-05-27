import time
import pathlib
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains

current = pathlib.Path().resolve()
opts = webdriver.ChromeOptions()
opts.add_argument('user-data-dir=' + str(current / 'Chrome'))
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=opts)

try:
    driver.get('https://www.instagram.com')
    input()

    time.sleep(2)
    elem = driver.find_element(By.CLASS_NAME, '_aaw9')
    action = ActionChains(driver)
    action.move_to_element(elem)
    action.click()
    action.send_keys('#파이썬')
    action.perform()

    time.sleep(5)

    action = ActionChains(driver)
    action.move_by_offset(0, 50)
    action.click()
    action.perform()

    time.sleep(5)

    elem = driver.find_element(By.CLASS_NAME, '_aaq8')
    posts = elem.find_elements(By.CLASS_NAME, '_aagw')
    for post in posts:
        action = ActionChains(driver)
        action.move_to_element(post)
        action.click()
        action.perform()

        time.sleep(1)

        elem = driver.find_element(By.CLASS_NAME, '_aamw')
        svg = elem.find_element(By.TAG_NAME, 'svg')
        if svg.get_attribute('aria-label') == '좋아요':
            action = ActionChains(driver)
            action.move_to_element(elem)
            action.click()
            action.perform()
            time.sleep(1)

        action = ActionChains(driver)
        action.send_keys(Keys.ESCAPE)
        action.perform()

        time.sleep(1)
except Exception as e:
    print(e)
finally:
    driver.quit()
