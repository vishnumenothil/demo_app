# def singleton(cls):
#     instances = {}
    
#     def get_instance(*args, **kwargs):
#         if cls not in instances:
#             instances[cls] = cls(*args, **kwargs)
#         return instances[cls]
#     setattr(cls,"get_instance",get_instance)
#     setattr(cls,"instances",instances)
#     return cls

# @singleton
# class MyClass:
#     a=10
#     def __init__(self, value):
#         self.value = value
#     def fun():
#         pass
# Usage
# obj1 = MyClass(10)
# obj2 = MyClass(20)
# obj3 = MyClass(20)
# print(MyClass.__dict__)
# print(obj1.__dict__)

# print(obj2.get_instance())
# print(obj3.get_instance())

# print(obj2.instances)


# print(obj1 is obj2)  # Output: True
# print(obj1.value)    # Output: 10

# def intercept(cls):
#     def __setattr__(self,name,value):
#         print("setattr")
#         if value<0:
#             raise ValueError(f"negative value of {name } is not allowed")
#         object.__setattr__(self,name,value)
#     setattr(cls,"__setattr__",__setattr__)
#     return cls

# @intercept
# class Point:
#     def __init__(self,a,b) -> None:
#         self.a=a
#         self.b=b

# p1=Point(1,1)
# p2=Point(10,78)
# p1.a=-5
# print(Point.__dict__)
