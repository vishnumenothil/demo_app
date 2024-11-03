from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located,element_to_be_clickable
from time import sleep
from selenium.webdriver.support.select import Select

driver= WebDriver()

driver.get("file:///C:/Users/shibi/Downloads/demo-html-20240826T064905Z-001/demo-html/dynamic.html")
# An expectation for checking that an element is present on the DOM of a page and visible.
#  Visibility means that the element is not only displayed but also has a height and width that is greater than 0.
# locator - used to find the element returns the WebElement once it is located and visible





# driver.find_element("id","adder1").click()
# w=WebDriverWait(driver,10)
# v=visibility_of_element_located(("id","cars1"))
# w.until(v)
# ele=driver.find_element("id","cars1")
# print("Done")
# select=Select(ele)
# select.select_by_visible_text("Honda")

driver.find_element("id","adder2").click()
w=WebDriverWait(driver,10)
# v=visibility_of_element_located(("id","cars2"))
v=element_to_be_clickable(("id","cars2")) #An Expectation for checking an element is visible and enabled such that you can click it.
w.until(v)
ele=driver.find_element("id","cars2")
print("Done")
select=Select(ele)                    #can not select a option select element is disebled
select.select_by_visible_text("Honda")


# driver.find_element("id","adder3").click()
# w=WebDriverWait(driver,10)
# v=visibility_of_element_located(("id","cars3"))
                                        #    TimeoutError 
# w.until(v)                                 #element is not visible with in the given time
# ele=driver.find_element("id","cars3")
# print("Done")
# select=Select(ele)
# select.select_by_visible_text("Honda")






input()