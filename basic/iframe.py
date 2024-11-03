from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.support.wait import WebDriverWait
from framework.lib import SeleniumWrapper

driver=WebDriver()
driver.get("file:///C:/Users/shibi/Downloads/demo-html-20240826T064905Z-001/demo-html/iframe.html")
driver.switch_to.frame("FR1")
s=SeleniumWrapper(driver)
w=WebDriverWait(driver,10)
v=visibility_of_element_located(("link text","Log in"))
w.until(v)
s.click_element(("link text","Log in"))
s.enter_text(("id","Email"),value="vishnumenothil@123.com")




driver.switch_to.default_content()
w1=WebDriverWait(driver,5)
v2=visibility_of_element_located(("link text","Google"))
w1.until(v2)
s.click_element(("link text","GoogleE"))


input()