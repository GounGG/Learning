# -*- coding:utf-8 -*-

# 百度图片自动爬去


import time
from selenium import webdriver

profile = webdriver.FirefoxProfile()
profile.set_preference('browser.download.dir',"D:\\images")
profile.set_preference('browser.download.folderList', 2)
profile.set_preference('browser.download.manager.showWhenStarting', False)
profile.set_preference('browser.helperApps.neverAsk.saveToDisk','image/jpeg, image/png')

firfox = webdriver.Firefox(firefox_profile=profile)
firfox.get("http://www.baidu.com")
firfox.find_element_by_id("kw").clear()
firfox.find_element_by_id("kw").send_keys(u"美女")
time.sleep(2)
firfox.find_element_by_id("su").click()
time.sleep(5)
firfox.current_window_handle
#firfox.find_element_by_css_selector(a[])
firfox.find_element_by_xpath("//*[@id=\"s_tab\"]/a[5]").click()
time.sleep(3)
firfox.current_window_handle
firfox.find_element_by_xpath("//*[@id=\"imgid\"]/div/ul/li[1]/div[1]/a/img").click()
time.sleep(3)
firfox.switch_to_window(firfox.window_handles[1])
while True:
    #firfox.find_element_by_xpath("//html/body/div[1]/div[2]/div/div[2]/div/div[1]/span[7]").click()
    firfox.find_element_by_class_name(r"bar-btn.btn-download").click()
    time.sleep(10)
    firfox.find_element_by_xpath("//*[@id=\"container\"]/span[2]").click()
    time.sleep(10)
firfox.quit()



