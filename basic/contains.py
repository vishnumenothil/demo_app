# from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.select import Select
from selenium import webdriver

from time import sleep
opt=webdriver.ChromeOptions()
opt.add_experimental_option('detach',True)

driver=webdriver.Chrome(options=opt)

driver.get("file:///C:/Users/shibi/Downloads/demo-html-20240826T064905Z-001/demo-html/demo.html")
sleep(2)
elements=driver.find_elements("xpath","//*[contains(text(),'Shopping')]")
for element in elements:
    print(element.text)
print(len(elements))