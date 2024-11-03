# from selenium.webdriver.chrome.webdriver import WebDriver
# from selenium.webdriver.support.select import Select
# from time import sleep
from lib import SeleniumWrapper
from loginpage import Loginpage
from pytest import mark
from excel import read_data,read_headers
from homepage import Homepage
#mark -object of a class used to create parametrize using method in the class parametrize() 

# driver=WebDriver()
# driver.get("https://demowebshop.tricentis.com/")

headers=read_headers("test_login_positive","smoke")

data= read_data("test_login_positive","smoke")
print(data)
@mark.parametrize(headers,data) 
def test_login(setup_tear_down,_config,request,email,password):
    # s=SeleniumWrapper(setup_tear_down,request.config.option.time)
    h=Homepage(setup_tear_down)
    h.login()
    lpage=Loginpage(setup_tear_down)
    lpage.login(email,password)
    













# headers12="email","password"
# data12=[
#     ("vishnumenothil@gmail","vishnu7902"),
#     ("abcdefg@gmail.com","company123"),
#     ("abcdefg@gmail.com","company123"),
#       ]

# @mark.parametrize(headers12,data12)
# def test_login_negative(setup_tear_down,_config,request,email,password):
#     s=SeleniumWrapper(setup_tear_down,request.config.option.time)

#     s.click_element(("link text","Log in"))
#     s.enter_text(("id","Email"),value=email)
#     s.enter_text(("id","Password"),value=password)
