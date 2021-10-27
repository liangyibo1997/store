'''
    跳转框架页：
        driver.switch_to.
            frame()
            windows()
            alert()

'''

from selenium import webdriver

driver = webdriver.Chrome()

driver.get(r"D:/梁艺博のFiles/系统软件测试/python自动化测试/python自动化测试/day01/练习的html/main.html")

driver.maximize_window()

# 跳转
driver.switch_to.frame("frame")

driver.find_element_by_xpath("//*[@id='input1']").send_keys("jason")
