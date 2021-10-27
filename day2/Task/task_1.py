from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

taobao = webdriver.Chrome()
taobao.get(
    "https://login.taobao.com/member/login.jhtml?spm=a21bo.jianhua.754894437.1.5af911d9ARx8u2&f=top&redirectURL=https%3A%2F%2Fwww.taobao.com%2F")
taobao.maximize_window()
time.sleep(1)

taobao.find_element_by_xpath("//*[@id='fm-login-id']").send_keys(17839987205)
time.sleep(1)
taobao.find_element_by_xpath("//*[@id='fm-login-password']").send_keys("")
time.sleep(1)

ac = ActionChains(taobao)
ele = taobao.find_element_by_xpath('//*[@id="nocaptcha" and class="nc-container"]/div/div/span')
ac.click_and_hold(ele).move_by_offset(300, 0).perform()
ac.release()
time.sleep(1)

taobao.find_element_by_xpath("//*[@class='fm-button fm-submit password-login fm-button-disabled']").click()
