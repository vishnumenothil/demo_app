from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.select import Select
from time import sleep
from lib import SeleniumWrapper
from pytest import mark
from excel import read_data,read_headers
from homepage import Homepage
from registrationpage import Registration

headers=read_headers("test_registration","smoke")
data=read_data("test_registration","smoke")




@mark.parametrize(headers,data)
def test_register(setup_tear_down,_config,request,gender,fname,lname,email,password,confirmpassword):
    s=SeleniumWrapper(setup_tear_down)
    hp=Homepage(setup_tear_down)
    hp.register()
    reg=Registration(setup_tear_down)
    reg.regsiter(gender,fname,lname,email,password,confirmpassword)










    
    #using parametrize
    # s.click_element(("link text","Register"))
    # if gender.upper()=="MALE":
    #     s.click_element(("id","gender-male"))
    # elif gender.upper() == "FEMALE":
    #     s.click_element(("id","gender-female"))

    # else:
    #     raise Exception("unknown gender")
    
    # s.enter_text(("id","FirstName"),value=fname)
    # s.enter_text(("id","LastName"),value=lname)
    # s.enter_text(("id","Email"),value=email)
    # s.enter_text(("id","Password"),value=password)
    # s.enter_text(("id","ConfirmPassword"),value=password)
    # s.click_element(("id","register-button")) 


