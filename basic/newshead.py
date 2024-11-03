from selenium.webdriver.chrome.webdriver import WebDriver
from time import sleep
from re import findall


driver=WebDriver()

driver.get("https://news.google.com/home?hl=en-IN&gl=IN&ceid=IN:en")
sleep(2)


driver.find_element("xpath","//input[@id='nav-search-submit-button']").click()
sleep(5)