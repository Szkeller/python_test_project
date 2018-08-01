# sample of selenium

from selenium import webdriver

browse = webdriver.Chrome()

browse.get('https://www.taobao.com')

print(browse.page_source)

browse.close()
