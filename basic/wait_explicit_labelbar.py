from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from time import sleep

driver=WebDriver()

driver.get("file:///C:/Users/shibi/Downloads/demo-html-20240826T064905Z-001/demo-html/ajaxy_page.html")

driver.find_element("xpath","//input[@name='typer']").send_keys("managing chrome elemen")
driver.find_element("id","red").click()
driver.find_element("xpath","//input[@name='submit']").click()
wait=WebDriverWait(driver,10)
v=expected_conditions.visibility_of_element_located(("xpath","//div[text()='managing chrome element']"))
wait.until(v)
print("success")
input()