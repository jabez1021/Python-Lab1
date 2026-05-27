from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    driver.get('http://cafe.naver.com/joonggonara')

    elem = driver.find_element(By.ID, 'topLayerQueryInput')
    elem.send_keys('자전거')
    elem.send_keys(Keys.RETURN)
    
    iframe = driver.find_element(By.ID, 'cafe_main')
    driver.switch_to.frame(iframe)

    elem = driver.find_elements(By.CLASS_NAME, 'article-board')[1]
    rows = elem.find_elements(By.XPATH, './table/tbody/tr')
    for row in rows:
        elem = row.find_element(By.CLASS_NAME, 'article')
        print(elem.text)

except Exception as e:
    print(e)
finally:
    driver.quit()
