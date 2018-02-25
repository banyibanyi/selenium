from selenium import webdriver

driver = webdriver.Firefox()
driver.get("http://m.baidu.com")

# 参数数字为像素点
print("设置浏览器宽480、高800显示")
driver.set_window_size(480, 800)
driver.quit()


