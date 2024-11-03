from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
driver=WebDriver()
driver.get("https://demowebshop.tricentis.com/")

driver.find_element("xpath","(//div[@class='block block-category-navigation']/div[@class='listbox']/ul/li/a)[1]").click()

time.sleep(5)
books={"Computing and Internet": 10.00,"Fiction":14.00,"Health Book":10.00}
for book,exp_price in books.items():

    prices=driver.find_element("xpath",f"//a[text()='{book}']/../..//span[@class='price actual-price']").text
    actual_price=(float(prices))

    if actual_price == exp_price:
        print("pass")
    else:
        print("fail")


input()


