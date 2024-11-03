from selenium.webdriver.chrome.webdriver import WebDriver
from time import sleep
from re import findall


driver =WebDriver()

driver.get("https:/www.google.com/")
sleep(2)
driver.find_element("xpath",'//textarea[@name="q"]').send_keys("python")
sleep(2)
driver.find_element("class name",'gNO89b').click()
sleep(5)
python_list=driver.find_elements("xpath","//*[contains(text(),'Python')]")
print(len(python_list))
for i in python_list:
    print(i.text)
input("press enter")