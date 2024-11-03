from selenium.webdriver.chrome.webdriver import WebDriver
import time
from selenium.webdriver import Keys
driver= WebDriver()


driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?153770296407")


items=driver.find_elements("xpath",'//input[@type="checkbox"]')


for element in items:
    element.send_keys(Keys.SPACE)
    time.sleep(0.2)


for ele in range(len(items)-1,-1,-1):
    items[ele].send_keys(Keys.SPACE)
    time.sleep(1)

input("press enter")