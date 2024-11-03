
# def add_greet(cls):
#     def greet(self):
#         print(f"good day {p1.name}")
#     cls.greet=greet   
#     return cls

# @add_greet
# class person:
#     def  __init__(self,name) -> None:
#         self.name=name

    
# p1=person("vishnu")
# p1.greet()


import time

def time_methods(cls):
    class TimedClass(cls):
        def __getattribute__(self, name):
            attr = super().__getattribute__(name)
            if callable(attr):
                def timed(*args, **kwargs):
                    start_time = time.time()
                    result = attr(*args, **kwargs)
                    end_time = time.time()
                    print(f"Method {name} took {end_time - start_time:.4f} seconds")
                    return result
                return timed
            return attr
    return TimedClass

@time_methods
class MyClass:
    def slow_method(self):
        time.sleep(1)
        return "Done"

    def fast_method(self):
        time.sleep(0.1)
        return "Quick Done"

# Usage
obj = MyClass()
obj.slow_method()  # Output: Method slow_method took 1.000x seconds
obj.fast_method()  # Output: Method fast_method took 0.100x seconds
