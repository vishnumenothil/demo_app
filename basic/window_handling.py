from selenium.webdriver.chrome.webdriver import WebDriver
from time import sleep

driver=WebDriver()
driver.get("https://demowebshop.tricentis.com/computing-and-internet")
 
sleep(2)

driver.find_element("link text","Facebook").click()
sleep(3)

input()






















# driver.find_element("xpath","//a[text()='Google+']").click()
# sleep(5)
# handles=driver.window_handles
# driver.switch_to.window(handles[1])
# sleep(6)
# driver.find_element("xpath","//a[text()='see this post']").click()

# sleep(3)
# driver.switch_to.window(handles[0])
# sleep(3)
# driver.find_element('link text','Register').click()
# input()

# sleep(4)
# driver.find_element("xpath","//a[text()='Twitter']").click()

# handle=driver.window_handles

# print(handle)
# driver.switch_to.window(handle[1])
# sleep(4)
# # driver.close()
# driver.switch_to.window(handle[0])
# sleep(2)
# driver.find_element("link text","Register").click()

input()