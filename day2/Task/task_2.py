from selenium import webdriver
import time

bilibili = webdriver.Chrome()
bilibili.get("https://passport.bilibili.com/login?from_spm_id=333.851.top_bar.login")
bilibili.maximize_window()
time.sleep(1)

bilibili.find_element_by_xpath("//*[@id='login-username']").send_keys(17839987205)
time.sleep(1)
bilibili.find_element_by_xpath("//*[@id='login-passwd']").send_keys("")
time.sleep(1)

bilibili.find_element_by_xpath("//*[@class='btn btn-login']").click()








