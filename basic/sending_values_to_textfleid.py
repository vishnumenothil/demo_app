from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.select import Select
from time import sleep

driver=WebDriver()

driver.get("file:///C:/Users/shibi/Downloads/demo-html-20240826T064905Z-001/demo-html/demo.html")
sleep(2)
details=["vishnu","menothil","tiur","malappuram","kerala",'india',7902859941,'vishnumenothil@gmail.com',676109]

elements=driver.find_elements("xpath","//input[@name='fname']")

for ele,det in  zip(elements,details):
    ele.send_keys(det)
    sleep(1)

# //td[text()='Perl']/..//input[@name='download']
driver.find_element("xpath","//td[text()='Java']/..//input[@name='download']").click()
input( )


