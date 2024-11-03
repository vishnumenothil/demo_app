from selenium.webdriver.chrome.webdriver import WebDriver
from  selenium.webdriver.common.action_chains import ActionChains
# to do some mouse action we have to import a class called ActionChains wich is present in the action class 
#modeule in common

from selenium.webdriver.common.keys import Keys
from time import sleep

driver= WebDriver()
driver.maximize_window()
driver.get('https://crossbrowsertesting.github.io/drag-and-drop.html')

source_element=driver.find_element('id','draggable')

target=driver.find_element("id","droppable")

sleep(1)
action=ActionChains(driver)
action.drag_and_drop(source_element,target).perform()
















# driver.get("https://demowebshop.tricentis.com/")
# sleep(1)

# register_link=driver.find_element("link text","Register")
# action=ActionChains(driver)

# action.context_click(register_link).perform()























# driver.get("https://demowebshop.tricentis.com/")
# sleep(1)
# action=ActionChains(driver)
# action.send_keys(Keys.PAGE_DOWN).perform()
# action.send_keys(Keys.PAGE.UP).perform()
# action.send_keys(Keys.ARROW_UP).perform()
# action.send_keys(Keys.ARROW_DOWN).perform()
# action.send_keys(Keys.ENTER).perform()
# action.send_keys(Keys.TAB).perform()
# action.send_keys(Keys.ESCAPE).perform()





















# driver.get("file:///C:/Users/shibi/Downloads/demo-html-20240826T064905Z-001/demo-html/demo.html")
# sleep(3)

# dbl_click=driver.find_element('xpath',"//button[@id='double-click']")

# action=ActionChains(driver)

# action.double_click(dbl_click).perform()














#mouseaction hover anelement using move to element
# element=driver.find_element("xpath","//span[text()='Profile']")
#create object for action class by  passing driver as argument 
#when calling the action function we have to pass the webelemnt on which we have to do the action
# actions=ActionChains(driver)
# actions.move_to_element(element).perform()
#without calling perform it will not perform the action 
# element=driver.find_element("xpath","//a[text()='login / Signup']").click()

input()