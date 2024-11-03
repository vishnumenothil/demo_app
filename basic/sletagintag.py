#selecting tags which is belongest to its parent tag only
# which could be immediate child or grand child
from selenium.webdriver.chrome.webdriver import WebDriver
import time
from re import  findall
from selenium.webdriver import Keys
driver= WebDriver()


driver.get("https://demowebshop.tricentis.com/Jewelry/")
time.sleep(2)
prices=driver.find_elements("xpath","//span[@class='price actual-price']")




time.sleep(2)
actual_price=[]
for price in prices:
    con_priice=price.text
    s=findall(r'[\d\.]',con_priice)
    actual_price.append(float("".join(s)))
print(actual_price)
product_title=driver.find_elements("xpath",'//h2[@class="product-title"]/a')
_product=[ i.text for i in product_title]


pair_price_product={product:price for product,price in zip( _product,actual_price)}

print(pair_price_product)

input("press enter")













# block_catagory=driver.find_elements("xpath",'//div[@class="block block-category-navigation"]//li')
# time.sleep(2)
# for cl in block_catagory:
#     print(cl.text)
#     time.sleep(10)




