# from selenium import webdriver
# import time
# from selenium.webdriver.common.action_chains import ActionChains
# browser=webdriver.Chrome()
# browser.get("https://ajio.com")
# browser.maximize_window()

# ActionChains(browser).move_to_element(browser.find_element("class name","alignTag") ).perform()


# time.sleep(3)
# print(dir(browser))



from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
import time
driver=WebDriver()
driver.maximize_window()
username="standard_user"
password="secret_sauce"
login_url="https://www.saucedemo.com/"
driver.get(login_url)
username_field=driver.find_element("id","user-name")

password_field=driver.find_element("id","password")
username_field.send_keys(username)

password_field.send_keys(password)

log=driver.find_element("id","login-button")
assert not log.get_attribute("disabled")
log.click()
time.sleep(2)
success_element=driver.find_element("class name","title")

print(success_element.text)
assert success_element.text == "Products"
    

