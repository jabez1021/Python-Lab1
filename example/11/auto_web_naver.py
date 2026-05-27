from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    driver.get('https://naver.com')
    keyword = input('검색어를 입력하세요:' )

    elem = driver.find_element(By.ID, 'query')
    elem.send_keys(keyword)
    elem.send_keys(Keys.RETURN)

    view = driver.find_element(By.LINK_TEXT, "VIEW")
    view.click()

    ul = driver.find_element(By.CLASS_NAME, '_list_base')
    blogs = ul.find_elements(By.XPATH, './li')

    for blog in blogs:
        title_tag = blog.find_element(By.CLASS_NAME, 'total_tit')
        print(title_tag.text)
        link = title_tag.get_attribute('href')
        print(link)

except Exception as e:
    print(e)
finally:
    driver.quit()
