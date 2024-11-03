from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import  WebElement
from time import sleep
from selenium.webdriver.support.select import Select
from selenium.webdriver import Keys
driver= WebDriver()

driver.get("https://demowebshop.tricentis.com/books")
sleep(2)

# driver.find_element("id","user-name").send_keys("standard_user")
# driver.find_element("id","password").send_keys("secret_sauce")
# driver.find_element("id","login-button").click()
# driver.find_element("xpath",'//select[@class="product_sort_container"]')

# element=driver.find_element("xpath",'//select[@class="product_sort_container"]')
# sel=Select(element)
# sel.select_by_visible_text("Name (Z to A)")
# sleep(5)

elements=driver.find_element("xpath",'//select[@id="products-orderby"]')
print(elements.text)
# sel=Select(elements)
# opts=sel.options

# for  opt in opts:
#     print(opt.text)
print(elements.size)
print(elements.location)
input()