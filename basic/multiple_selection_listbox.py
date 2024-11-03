from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.select import Select
from time import sleep

driver=WebDriver()

driver.get("file:///C:/Users/shibi/Downloads/demo-html-20240826T064905Z-001/demo-html/demo.html")
sleep(5)
select=driver.find_element("id","multiple_cars")
opt= Select(select)
p=opt.options
for i in p:
   i.click()
sleep(10)
opt.deselect_all()
opt.select_by_visible_text("Ford")
opt.select_by_visible_text("Honda")
ap=opt.all_selected_options
newap=[i.text for i in ap]
print(newap)

input("click enter to close the browser")