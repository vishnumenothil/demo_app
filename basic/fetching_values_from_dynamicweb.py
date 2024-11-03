from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.select import Select
from time import sleep

driver=WebDriver()

driver.get("file:///C:/Users/shibi/Downloads/demo-html-20240826T064905Z-001/demo-html/demo.html")
sleep(2)
# f=open("price.txt","w")

# while True:
#     prices=driver.find_element("xpath","//td[text()='FB']/..//td[3]").text
#     print(prices,file=f,flush=True)
#     sleep(5)


# driver.get("https://ticker.finology.in/market/index/nse/niftyjr")
# sleep(2)


# while True:
#     prices=driver.find_element("xpath","//table[@class='table table-sm table-hover screenertable']//a[text()='Canara Bank']/../..//td[2]").text
#     print(prices)
#     sleep(5)







companies=["MSFT","AA","FB"]
 
for company in companies:
    print(f"{company} \t\t ",end='')

print()
while True:
    for company in companies:

        prices=driver.find_element("xpath",f"//td[text()='{company}']/..//td[3]").text
        print(f"{prices}\t\t",end='')
        sleep(5)
    print() 