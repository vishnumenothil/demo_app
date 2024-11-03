from selenium.webdriver.chrome.webdriver import WebDriver
from time import sleep
from re import findall


driver=WebDriver()

driver.get("https://www.amazon.in/")
driver.find_element("id","twotabsearchtextbox").send_keys("samsungs23")
sleep(2)
driver.find_element("xpath","//input[@id='nav-search-submit-button']").click()
sleep(5)

text_name=driver.find_elements("xpath","//div[@data-cy='title-recipe']//span[@class='a-size-medium a-color-base a-text-normal']")
product_name=[t.text for t in text_name]
print(product_name)
product_xpath=driver.find_elements("xpath",'//span[@class="a-price"]//span[@class="a-price-whole"]')
product=[p.text for p in product_xpath]
_product=[rem_com.replace(",","") for rem_com in product]

print(_product)
pair_pr_pri={product : float(price) for product,price in  zip(product_name,_product)}


print(pair_pr_pri)

sorted_dic=sorted(pair_pr_pri.items(),key=lambda s:s[-1])
print(sorted_dic)
print("*"*150)
print(f"cheapest item in  list is : {sorted_dic[0][0]} price is {sorted_dic[0][1]}")

input("press enter ")
