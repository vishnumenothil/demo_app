# from selenium.webdriver.chrome.webdriver import WebDriver
# from selenium.webdriver.support.select import Select
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions
# from time import sleep


# driver=WebDriver()
# driver.get("https://demowebshop.tricentis.com/")
# driver.implicitly_wait(10)

# driver.find_element("link text","_Log in").click()
# input()


# l=[1,2]
# d=[[1,2],3,4]
# g=()
# if l in d:
#     print("yes")
# else:
#     print("no")





















a="amasdmalayalamsdsmamgfdmadam"
i=0
pali=[]

while i <len(a):
    string = a[i]

    for j in range(i+1 , len(a)):
        string += a[j] 
        if string == string[::-1]:
            pali.append(string)
            i += len(string)
            break
    
    i+=1
print(pali)
