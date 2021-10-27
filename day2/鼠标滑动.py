from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains  # 事件链对象
import time

driver = webdriver.Chrome()

driver.get(r"D:/梁艺博のFiles/系统软件测试/python自动化测试/python自动化测试/day01/练习的html/滑动验证/mousedrag.html")

driver.maximize_window()

# 把driver交给ActionChians管理

ac = ActionChains(driver)

ele = driver.find_element_by_xpath('//*[@id="box"]/div[3]')  # 滑块元素
time.sleep(2)
ac.click_and_hold(ele).move_by_offset(300, 0).perform()  # 立即执行

ac.release()  # 释放鼠标
