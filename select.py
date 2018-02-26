from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
from time import sleep
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get('http://www.baidu.com')
# 鼠标悬停至“设置”链接
driver.find_element_by_link_text('设置').click()
sleep(5)
# 打开搜索设置
driver.find_element_by_link_text("搜索设置").click()
sleep(5)
# 搜索结果显示条数
sel = driver.find_element_by_xpath("//select[@id='nr']")
Select(sel).select_by_value('50')  # 显示50条
sleep(5)
driver.quit()