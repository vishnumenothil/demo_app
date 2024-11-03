from selenium.webdriver.chrome.webdriver import WebDriver
from time import sleep

driver=WebDriver()
driver.get("https://ticker.finology.in/market/index/nse/niftyjr")

sleep(2)


input()