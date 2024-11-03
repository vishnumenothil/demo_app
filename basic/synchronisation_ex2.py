from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located,title_is
from time import sleep
from selenium.webdriver.support.select import Select


driver =WebDriver()
driver.get("https://demowebshop.tricentis.com/")

driver.find_element("link text","Log in").click()

wait=WebDriverWait(driver,10)
a=title_is("Demo Web Shop. Login")
wait.until(a)
print("Done")
input()