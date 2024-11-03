from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.select import Select
from time import sleep
from re import findall
from csv import DictWriter,reader


def read_csv():
    data={}
    with open('books_details.csv',"r") as f:
         rows=reader(f)
#         headers=next(rows) #to remve the headeres
#         for row in rows:
#             data[row[0]]=float(row[1])
    return rows

print(read_csv())
#     return data
# driver=WebDriver()
# driver.get("https://demowebshop.tricentis.com/")
# sleep(5)
# data=read_csv()
# for book,price in data.items():
#     _xpath="//a[text()='{book}']/../..//span[@class = 'price actual-price'"
#     b=driver.find_element("xpath",_xpath)
#     if b==price:
#         print("PASS")
#     else:
#         print("FAIL") 