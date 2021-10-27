'''
    京东的登陆、淘宝登陆、苏宁的登陆脚本
    bilibili登陆脚本，搜索一个鬼畜视频并播放脚本写出来。
    做知乎的官网，并登陆，和发表一篇文章。
    企查查的官网登陆。
'''

from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get("http://www.jd.com")
driver.maximize_window()

driver.find_element_by_xpath("//*[@id='key']").send_keys("Thinkpad E580")
driver.find_element_by_xpath('//*[@id="search"]/div/div[2]/button').click()

time.sleep(2)

# 提取这个元素里里面的文字
try:
    driver.find_element_by_xpath('//*[@id="J_searchWrap"]/div[2]/div/div[3]')
    print("搜索成功！")
except Exception:
    driver.save_screenshot("a.jpg")
