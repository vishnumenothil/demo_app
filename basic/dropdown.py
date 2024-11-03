from selenium.webdriver.chrome.webdriver import WebDriver
from time import sleep
from selenium.webdriver.support.select import Select
from selenium.webdriver import Keys
driver= WebDriver()

# driver.get("https://demowebshop.tricentis.com/")

# driver.find_element("link text","Register").click()

# lisst=driver.find_elements("xpath",'//input[@type="text"]')

# items=["s","suresh","gopi","sureshgopi@gmail.com","gmail",]

# for li,it in zip(lisst,items):
#     li.send_keys(it) 
#     sleep(2)

# elements=driver.find_elements("xpath","//a")
# for element in elements :
#     print(element.text,element.get_attribute("href"))








driver.get("https://the-internet.herokuapp.com/dropdown")
driver.maximize_window()
dropdown_element=driver.find_element("xpath","//select[@id='dropdown']")
select=Select(dropdown_element)
select.select_by_index("2")

sleep(5)
first_selected=select.first_selected_option
print(first_selected.text)
input("press enter")