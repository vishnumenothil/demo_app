import time
from selenium.webdriver.chrome.webdriver import WebDriver
driver= WebDriver()
driver.get("https://google.com/")
screen_size=[(1045,600),(500,320),(800,1025),(500,500),(100,10000)]
try:
    for width,height in screen_size :
        driver.set_window_size(width,height)
        time.sleep(3)
finally:
    
    driver.close()