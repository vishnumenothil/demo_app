from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.select import Select
from time import sleep

driver=WebDriver()

driver.get("file:///C:/Users/shibi/Downloads/demo-html-20240826T064905Z-001/demo-html/demo.html")
sleep(2)

first_names=driver.find_elements("xpath","//table[@name='customers']//td[2]")

actual_name=[name.text for name in first_names]

sorted_name=sorted(actual_name)
if sorted_name == actual_name:
    print("first names in sorted order")
else:
    print("fail")

second_names=driver.find_elements("xpath","//table[@name='customers']//td[3]")

actu_second_name=[name.text for name in second_names]

sorted_second_name=sorted(actual_name)
if sorted_second_name == actu_second_name:
    print("pass")
else:
    print("second namae is not in sorted order")