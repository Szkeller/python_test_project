#sample of selenium

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

browse = webdriver.Chrome()
try:
    browse.get('https://www.baidu.com')
    input = browse.find_element_by_id('kw')
    input.send_keys('Python')
    input.send_keys(Keys.ENTER)
    wait = WebDriverWait(browse,10)
    wait.until(EC.presence_of_element_located((By.ID, 'content_left')))
    print(browse.current_url)
    print(browse.get_cookies())
    print(browse.page_source)
finally:
    browse.close()

