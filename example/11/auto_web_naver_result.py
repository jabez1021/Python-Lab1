from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

from openpyxl import Workbook
xlsx = Workbook()
sheet = xlsx.active
sheet.append(['Title', 'Link'])

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

        link = title_tag.get_attribute('href')

        sheet.append([title_tag.text, link])

except Exception as e:
    print(e)
finally:
    driver.quit()

file_name = 'result.xlsx'
xlsx.save(file_name)
from my_email import send_mail
send_mail('이태화', '......@gmail.com', '네이버 검색 결과입니다.', file_name)