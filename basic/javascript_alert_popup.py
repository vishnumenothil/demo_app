from selenium.webdriver.chrome.webdriver import WebDriver

from time import sleep

driver=WebDriver()


driver.get("file:///C:/Users/shibi/Downloads/demo-html-20240826T064905Z-001/demo-html/demo.html")
sleep(4)
driver.find_element("xpath", "//input[@type='file']").send_keys("C:/Users/shibi/OneDrive/Desktop/new resume.docx")

"C:\Users\shibi\OneDrive\Desktop\new resume.docx"

# driver.find_element("id", "delete").click()

# print(driver.switch_to.alert.text)
# driver.switch_to.alert.dismiss()





# driver.get("https://demowebshop.tricentis.com/")
# sleep(4)
# driver.find_element("xpath", "//input[@value='Search']").click()

# sleep(2)
# print(driver.switch_to.alert.text)
# driver.switch_to.alert.accept()

input()