class Car:
    def __init__(self):
        print("super class")
    def engine(self):
      print("Engine is working")

class Bike(Car):
    def __init__(self):
        print("sub class")
    def fuel(self):
       print("petrol")

print("object creation of super class")
obj = Car()
obj.engine()
print("Object creation of sub  class")
obj1=Bike()
obj1.engine()
obj1.fuel()




'''
import keyword
keyword.kwlist
print(len(keyword.kwlist))'''


'''
class BaseClass:
    Body
    of
    base

    class


class DerivedClass(BaseClass):
    Body
    of
        derived

    class


"""
"""


class Polygon:
    def _init_(self, no_of_sides):
        self.n = no_of_sides
        self.sides = [0 for i in range(no_of_sides)]

    def inputSides(self):
        self.sides = [float(input("Enter side " + str(i + 1) + " : ")) for i in range(self.n)]

    def dispSides(self):
        for i in range(self.n):
            print("Side", i + 1, "is", self.sides[i])


"""
"""


# parent class
class Bird:

    def _init_(self):
        print("Bird is ready")

    def whoisThis(self):
        print("Bird")

    def swim(self):
        print("Swim faster")


# child class
class Penguin(Bird):

    def _init_(self):
        # call super() function
        super()._init_()
        print("Penguin is ready")

    def whoisThis(self):
        print("Penguin")

    def run(self):
        print("Run faster")


peggy = Penguin()
peggy.whoisThis()
peggy.swim()
peggy.run()
"""
"""


class Triangle(Polygon):
    def _init_(self):
        Polygon._init_(self, 3)

    def findArea(self):
        a, b, c = self.sides
        # calculate the semi-perimeter
        s = (a + b + c) / 2
        area = (s * (s - a)(s - b)(s - c)) ** 0.5
        print('The area of the triangle is %0.2f' % area)
        """
"""


class Person:
    def _init_(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


# Use the Person class to create an object, and then execute the printname method:

x = Person("satish", "babu")
x.printnam
"""
"""


class Person:
    def _init_(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


class Student(Person):
    def _init_(self, fname, lname):
        super()._init_(fname, lname)


x = Student("satish", "babu")
x.printname()
"""
"""


class Person:
    def _init_(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


class Student(Person):
    def _init_(self, fname, lname):
        super()._init_(fname, lname)
        self.graduationyear = 2019


x = Student("satish", "babu")
print(x.graduationyear)
"""

"""


class Person:
    def _init_(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


class Student(Person):
    def _init_(self, fname, lname, year):
        super()._init_(fname, lname)
        self.graduationyear = year

    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)


x = Student("satish", "babu", 2019)
x.welcome()
"""
"""


class Robot:
    def _init_(self, name):
        self.name = name

    def say_hi(self):
        print("Hi, I am " + self.name)


class PhysicianRobot(Robot):
    pass


x = Robot("satish")
y = PhysicianRobot("babu")
print(x, type(x))
print(y, type(y))
y.say_hi()
"""
"""


class Robot:
    def _init_(self, name):
        self.name = name

    def say_hi(self):
        print("Hi, I am " + self.name)


class PhysicianRobot(Robot):
    def say_hi(self):
        print("well come to satish")
        print(self.name + " katta")


y = PhysicianRobot("babu")
y.say_hi()
"""
"""


class Employee:
    # 1.state
    def _init_(self, employeeid, employee_name, employee_email):
        self.employeeid = employeeid
        self.employee_name = employee_name
        self.employee_email = employee_email

    # 2 behaviour
    def get_venkat(self):
        print("Enter the employee details :", self.employeeid, self.employee_name,
              self.employee_email)


rinky = Employee(101, "venkat", "venkat147@gmail.com")
rinky.get_venkat()
"""
"""


class Student:

    # 1. STATE
    def _init_(self, r_no, name, marks):
        self.r_no = r_no
        self.name = name
        self.marks = marks

    # 2. BEHAVIOR
    def get_sinfo(self):
        print("Student details are ", self.r_no, self.name, self.marks)


info = Student(23, 'satish', 75)
info.get_sinfo()
"""
"""


class Student:

    # 1. STATE
    def _init_(self, r_no, name, marks):
        self.r_no = r_no
        self.name = name
        self.marks = marks

    # 2. BEHAVIOR
    def get_sinfo(self):
        print("Student details are ", self.r_no, self.name, self.marks)


info = Student(23, 'rinky', 98)
info.get_sinfo()

'''