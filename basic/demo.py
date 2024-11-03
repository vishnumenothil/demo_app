# from selenium.webdriver.edge.webdriver import WebDriver
from selenium.webdriver.chrome.webdriver import WebDriver

import time


driver=WebDriver()
driver.get("https://demowebshop.tricentis.com/")
time.sleep(1)

driver.find_element("class name","ico-register").click()
time.sleep(1)

driver.find_element("id","gender-male").click()
time.sleep(1)

driver.find_element("name","FirstName").send_keys("azxc")
driver.find_element("name","LastName").send_keys("world")
driver.find_element("id","Email").send_keys("world123%^&@gmail.com")
driver.find_element("id","Password").send_keys("1234568")
time.sleep(1)
driver.find_element("id","ConfirmPassword").send_keys("1234568")
time.sleep(1)
driver.find_element("name","register-button").click()
time.sleep(1)
driver.find_element("class name","ico-login").click()
time.sleep(1)
driver.find_element("id","Email").send_keys("world123%^&@gmail.com")
time.sleep(1)
driver.find_element("id","Password").send_keys("1234568")
time.sleep(1)           
driver.find_element("class name","button-1").click()
time.sleep(5)
print(driver.title)








# driver.maximize_window()
# time.sleep(100)


# driver.get("https://www.shoppersstack.com/")
# time.sleep(10)
# driver.find_element("id","loginBtn").click()

# driver.find_element("id","Email").send_keys("vishnumenothil@gmail.com")

# driver.find_element("id","Password").send_keys("vishnu7902")


# driver.find_element("id","Login").click()
# print(driver.title)






