#to get a element and its perticular price from the webpage to the python

from selenium.webdriver.chrome.webdriver import WebDriver
from time import sleep
from re import findall


driver=WebDriver()

driver.get("https://www.saucedemo.com/")
driver.find_element("id","user-name").send_keys("standard_user")
sleep(1)
driver.find_element("id","password").send_keys("secret_sauce")
sleep(1)
driver.find_element("id","login-button").click()

#xpath to find text element
xpath_product=driver.find_elements("xpath",'//div[@class="inventory_item_name "]')
products=[product.text for product in xpath_product]
print(products)

#xpath to find prices

xpath_price=driver.find_elements("xpath",'//div[@class="inventory_item_price"]')
prices=[price.text for price in xpath_price]

actual_price=[]
for item in prices:
    s=findall(r'[\d\.]+',item)
    actual_price.append(float("".join(s)))
    
print(actual_price)

product_price_pairs={product : price for product,price in zip(products,actual_price)}
print(product_price_pairs)

by_price=sorted(product_price_pairs.items(),key=lambda s:s[-1])
print(by_price)


input("press enter to close browser")