from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.get("https://www.bilibili.com/")
driver.maximize_window()
time.sleep(1)

ac = ActionChains(driver)
ele = driver.find_element_by_xpath('//*[@id="primaryChannelMenu"]/span[2]')
ac.move_to_element(ele).perform()
ac.release()
