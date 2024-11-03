def _log(fun):
    def wrapper(*args,**kwars):
        print(f"you are called {fun.__name__}")
        return fun(*args,**kwars)
    return wrapper


def log(cls):
    for key,value in cls.__dict__.items():# all the attribute which is belongest to a class present in the class dictionary 
        if callable(value):   
                                           #we access class dictionry  classname.__dict__ 
            setattr(cls,key,_log(value))   #in that dictionary function_name will be key  and corresponding value will be value of the dictionary
    return cls                             # using callable we can check whether value of a dictionary is function or not if it is a function 
                                           #setattr creating  new function in the class by name key of the old function name and  
                                           #passing values(function ) to _log to decarotor 
                                           #basically here decaroting all funtions in a class using class decarator and fnction decarotor
@log
class Arithmetic:
    def add(self,a,b):
        return a + b
    def sub(self,a,b):
        return a - b
    def mul(self,a,b):
        return a * b
    

a=Arithmetic()
print(a.add(10,20))
print(a.sub(10,20))
print(a.mul(10,20))
# print(Arithmetic.__dict__)