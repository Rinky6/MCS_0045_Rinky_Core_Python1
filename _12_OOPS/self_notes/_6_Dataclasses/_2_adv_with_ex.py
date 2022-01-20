"""
1st advantages of dataclasses module is we dont need to write the def __init__()
we can initialize the class variable(dunder methods) using @dataclass we no need to write the
self.var_name

"""

class Student:
    def __init__(self,name,eid,sal):
        self.name = name
        self.eid = eid
        self.sal = sal
        print(name,eid,sal)
obj = Student("Rinky", 45, 10000)
print(obj.name)
print(obj)
print(type(obj))





from dataclasses import dataclass
#using data class
@dataclass
class Student:
    name : str
    eid : int
    sal : int

obj = Student("Rinky" , 45, 10000)
print(obj.name)

