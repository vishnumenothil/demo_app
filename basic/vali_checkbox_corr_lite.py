from selenium.webdriver.chrome.webdriver import WebDriver
from time import sleep


driver= WebDriver()
driver.get("https://demowebshop.tricentis.com/books")



books=[ "Computing and Internet",  "Fiction","Health Book"]

for book in books:
     _xpath=f'//a[text()="{book}"]/../..//input[@value = "Add to cart"]'
     element=driver.find_element("xpath",_xpath).click()
     sleep(5)

driver.find_element("partial link text","Shopping cart").click()


driver.find_element("xpath",f'(//a[text()="Health Book"])[2]/../..//input[@type="checkbox"]').click()
sleep(1)
driver.find_element("xpath",'//input[@class = "button-2 update-cart-button"]').click()

sleep(5)
driver.find_element("xpath",'(//a[text()="Fiction"])[2]/../..//input[@type="text"]').clear()
sleep(1)
driver.find_element("xpath",'(//a[text()="Fiction"])[2]/../..//input[@type="text"]').send_keys("5")
driver.find_element("xpath",'//input[@class = "button-2 update-cart-button"]').click()
input("press enter to close the browser")








