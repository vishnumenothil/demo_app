from selenium.webdriver.chrome.webdriver import WebDriver
import time
from selenium.webdriver import Keys
driver= WebDriver()


# driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?153770296407")
# driver.maximize_window()
# driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

# checkboxes=driver.find_elements("xpath","//input[@type='checkbox']")
# checked_count=0
# for check in checkboxes:
    
#     check.send_keys(Keys.SPACE)
#     time.sleep(1)
    
    


# for checkbox in checkboxes:
#     if checkbox.is_selected():
#         checked_count+=1

# expected_check_count=7
# if checked_count==expected_check_count:
#     print("check box count verified")
# else:
#     print("check box count mix match")



# text_name=driver.find_elements("xpath","//div/div/label[@class='question top_question']")
# for i in text_name:
#     print(i.text)
# input("press enter")


# next example

driver.get("file:///C:/Users/shibi/Downloads/demo-html-20240826T064905Z-001/demo-html/demo.html")
time.sleep(1)

checkboxs=driver.find_elements("xpath","//input[@name='download']")
for checkbox in checkboxs:
    checkbox.click()
    time.sleep(5)


for i in range(len(checkboxs)-1,-1,-1):
    checkboxs[i].click()
    time.sleep(1)

