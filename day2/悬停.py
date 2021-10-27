from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains  # 事件链对象
import time

driver = webdriver.Chrome()

driver.get("http://www.jd.com")

driver.maximize_window()

# 把driver交给ActionChians管理

ac = ActionChains(driver)

ele = driver.find_element_by_link_text("我的京东")

ac.move_to_element(ele).perform()

ac.release()

# time.sleep(2)
#
# driver.quit()
