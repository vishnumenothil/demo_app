from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
driver=WebDriver()
driver.get("https://demowebshop.tricentis.com/")
driver.find_element("link text","Register").click()
# general syntax for css selector
# htmltag[property="value"]
driver.find_element("css selector",'input[id="gender-male"]').send_keys(Keys.SPACE)
driver.find_element("css selector",'input[id="FirstName"]').send_keys("mohan")
driver.find_element("css selector",'input[id="LastName"]').send_keys("lal")
driver.find_element("css selector",'input[id="Email"]').send_keys("mohanlal@gmail1223.com")
driver.find_element("css selector",'input[id="Password"]').send_keys("lal1234")
driver.find_element("css selector",'input[id="ConfirmPassword"]').send_keys("lal1234")
driver.find_element("css selector",'input[id="register-button"]').click()
# driver.find_element("xpath",'//input[@class="register-continue-button"]').click()
driver.maximize_window()
driver.find_element("link text",'Log in').click()
# time.sleep(2)
driver.find_element("css selector",'input[id="Email"]').send_keys("sureshgopi@gmail.com")
time.sleep(1)
driver.find_element("css selector",'input[id="Password"]').send_keys("sureshgopi")
time.sleep(1)
driver.find_element("xpath",'//input[@class="button-1 login-button"]').click()
time.sleep(1)
logout =driver.find_element("link text","Log out")
time.sleep(1)
driver.find_element("link text",'Books').click()
time.sleep(1)
driver.find_element("xpath",'//img[@alt="Picture of Computing and Internet"]').click() 
driver.find_element("xpath",'//img[@id="main-product-img-13"]').click()




driver.find_element("xpath",'(//a[@href="/books"])[3]').click()
booknames=["Computing and Internet"  ,'Fiction' ,"Health Book",'Fiction']
book_count={}
for bookname in booknames:
    driver.find_element("xpath",f'//a[text()="{bookname}"]/../..//input[@value="Add to cart"]').click()
    time.sleep(5)
driver.find_element("partial link text","Shopping cart").click()
input("press enter to close te browser")
   

    








