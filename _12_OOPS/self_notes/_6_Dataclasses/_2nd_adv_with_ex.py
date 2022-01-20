"""
The main second advantages of dataclasses is whenever we create the object of class with same
attribute value in diff object in normal class if we compare these object we get false but using data
classes its true
Because in dataclasses there is @dataclass autocheck the dunder method and check the values of it with eq

"""
from dataclasses import dataclass

@dataclass()
class Student:
    name : str
    sal : int
    eid : int
std = Student("Rinky",10000,45)
std1 =  Student("Rinky",10000,45)
print(std)
print(std1)
print(std==std1)



class Student:
    def __init__(self , name,sal,eid):
        self.name= name
        self.sal = sal
        self.eid = eid

std = Student("Rinky",10000,45)
std1 =  Student("Rinky",10000,45)
print(std)
print(std1)
print(std==std1)



