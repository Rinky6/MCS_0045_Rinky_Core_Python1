"""
The third advantages of the dataclasses is whenever we create the object of the class in a simple class
and if we print object of that class it's print object of that class whereas using the dataclass
if we print the object of that that class it print class name with the attribute and value.

"""

from dataclasses import dataclass

@dataclass()
class Student:
    name : str
    sal : int
    eid : int
std = Student("Rinky",10000,45)

print(std)




class Student:
    def __init__(self , name,sal,eid):
        self.name= name
        self.sal = sal
        self.eid = eid

std = Student("Rinky",10000,45)

print(std)


