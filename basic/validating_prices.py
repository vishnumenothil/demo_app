from selenium.webdriver.chrome.webdriver import WebDriver
from time import sleep


driver= WebDriver()

books={
    "Computing and Internet":10.00,
    "Fiction":24.00,
    "Health Book":24.00
}

driver.get("https://demowebshop.tricentis.com/books")
sleep(3)
for book,expected_price in books.items():
    _xpath=f'//a[text()="{book}"]/../..//span[@class = "price actual-price"]'
    actual_price=driver.find_element("xpath",_xpath).text
    sleep(1)

    if expected_price == float(actual_price):
        print("pass")
    else:
        print(f"validation is fail, actual price {actual_price} is not maching  expected prices  {expected_price}")


input("press enter")