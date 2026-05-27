from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    driver.get('http://11st.co.kr')

    elem = driver.find_element(By.CLASS_NAME, 'search_text')
    elem.send_keys('자전거')
    elem.send_keys(Keys.RETURN)

    from openpyxl import Workbook
    result_xlsx = Workbook()
    worksheet = result_xlsx.active
    worksheet.append(['상품명', '가격'])

    elems = driver.find_elements(By.XPATH, "//ul[contains(@class, 'c_listing_view_type_list')]/li")
    for elem in elems:
        title_tag = elem.find_element(By.CLASS_NAME, 'c_prd_name')
        # print(title_tag.text)
        price_tag = elem.find_element(By.XPATH, './/div[@class="c_prd_price"]//span[@class="value"]')
        print(title_tag.text, price_tag.text)
        worksheet.append([title_tag.text, price_tag.text])

    file_name = 'C:\\python\\examples\\2.6\\11st_result.xlsx'
    result_xlsx.save(file_name)

    from my_email import send_mail
    send_mail('이태화', '......@gmail.com', '테스트', file_name)
except Exception as e:
    print(e)
finally:
    driver.quit()
