from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException
from time import sleep

driver=WebDriver()
driver.get("                                                                                                                    /")
driver.maximize_window()
sleep(2)
def select_date(month,date,year):
    _xpath=f"//h2[text()='{month} {date}']/../..//div[text()={year}]"
    for _ in range(0,24):
        try:
           driver.find_element("xpath",_xpath).click()
           break
        except NoSuchElementException:
            driver.find_element("xpath","//button[@class='switch-month switch-right']").click()
            sleep(1)


select_date(input("enter the month").capitalize(),input("enter the year "),input("enter the date"))
input()