from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

zhihu = webdriver.Chrome()
zhihu.get("https://www.zhihu.com/signin?next=%2F")
zhihu.maximize_window()
time.sleep(1)

zhihu.find_element_by_xpath("//*[@class='SignFlow-tab']").click()
time.sleep(1)

zhihu.find_element_by_xpath('//*[@class="SignFlow-account"]/div/label/input').send_keys(17839987205)
time.sleep(1)
zhihu.find_element_by_xpath('//*[@class="SignFlow-password"]/div/label/input').send_keys("")
time.sleep(1)

zhihu.find_element_by_xpath("//*[@class='Button SignFlow-submitButton Button--primary Button--blue']").click()

# ac = ActionChains(zhihu)
# ele = zhihu.find_element_by_xpath("//*[@class='yidun_slider']")
#
# js = "document.getElementById('randomPosX').style.display='block'"
# zhihu.execute_script(js)
#
# dist = zhihu.find_element("id", "randomPosX").text
# print(dist)
#
# ac.click_and_hold(ele).perform()
# time.sleep(2)
#
# ac.drag_and_drop_by_offset(ele,int(dist),0).perform()
