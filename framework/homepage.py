from lib import SeleniumWrapper
from excel import read_locator
class Homepage:
    _locator=read_locator("homepage")
    
    def __init__(self,driver) -> None:
        self.driver=driver

    def register(self):
        s=SeleniumWrapper(self.driver)
        s.click_element(self._locator["lnk_register"])
        

    def login(self):
        s=SeleniumWrapper(self.driver)
        s.click_element(self._locator["lnk_login"])
