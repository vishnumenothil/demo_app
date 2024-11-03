from selenium.webdriver.support.select import Select
from selenium.webdriver.support.expected_conditions import  visibility_of_element_located
from selenium.webdriver.support.wait import WebDriverWait

def  wait(func):
    def wrapper(*args,**kwargs,):
        # intance,locator=args
        intance,locator=args  #to pass time out time from the command prompt
        # print(f"waiting for locator{locator}")
        w=WebDriverWait(intance.driver,10)
        v=visibility_of_element_located(locator)
        w.until(v,message="element is not found ")
        return func(*args,**kwargs)
    
        
    return wrapper

def wait_cls(cls):
    for key , value in cls.__dict__.items():

        if callable(value)and key !=  "__init__" :
            setattr(cls,key,wait(value)) 
    return cls


@wait_cls
class SeleniumWrapper:
    def __init__(self,driver) -> None:
        self.driver=driver
        
    @wait    
    def click_element(self,locator):
        self.driver.find_element(*locator).click()
    @wait
    def enter_text(self,locator,*,value):
        # driver.find_element(*locator).clear()
        self.driver.find_element(*locator).send_keys(value)
    @wait
    def select_item(self,locator,*,item):
        element=self.driver.find_element(*locator)
        option=Select(element)
        option.select_by_visible_text(item)

