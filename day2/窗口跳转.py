from selenium import webdriver

driver = webdriver.Chrome()

driver.get(r"D:/梁艺博のFiles/系统软件测试/python自动化测试/python自动化测试/day01/练习的html/跳转页面/pop.html")

driver.maximize_window()

driver.find_element_by_xpath("//*[@id='goo']").click()

# 获取所有窗口唯一标号

data = driver.window_handles  # ["s001","s002"]

driver.switch_to.window(data[1])

# 百度搜索
driver.find_element_by_xpath("//*[@id='kw']").send_keys("java")
