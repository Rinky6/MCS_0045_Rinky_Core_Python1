"""Polymorphism : Ability to exists in multiple forms
2 types : Static polymorphism - compile time - Ex => Method Overloading
          Dynamic polymorphism - run time    - Ex => Method Overriding
"""

# Static polymorphism


'''Method overloading in other languages:
---------------------------------------
'''

'''
class Movrld:
    def getdata(x=None,y=None):

        z=x+y
        print("Sum of two no : " , z)

    def getdata(x=None):
        z=x*x*x
        print("multiply : " , z)


    def getdata(x=None,y=None,z=None):
        z=x*y+z
        print("Arithmetic operation : " , z)
obj=Movrld(10)
obj.getdata()
obj=Movrld(20,40)
obj.getdata()
obj=Movrld(10.20,30)
obj.getdata()


#TypeError: Movrld() takes no arguments
'''

class MethodOverloading :
    def greeting(self, name=None):
     if name is not None:
        print("Welcome  " + name)
     else:
        print("Welcome")

# Create an object referencing by variable ob
ob = MethodOverloading()
# call the method greeting without parameter
ob.greeting()
# call the method with parameter
ob.greeting("MCS")


#(********************@staticmethod(overload)************************)

class Test:
    @staticmethod
    def sum_1(a=None, b=None, c=None):
        if a is not None and b is not None and c is not None:
            print('The Sum of 3 Numbers:', a + b + c)
        elif a is not None and b is not None:
            print('The Sum of 2 Numbers:', a + b)
        else:
            print('Please provide 2 or 3 arguments')


t = Test()
t.sum_1(10, 20)
t.sum_1(10, 20, 30)
t.sum_1(10)









class Movrld:
    def getdata(self,x=None,y=None,z=None):
        if x is  not None:
            print("value of x : " , x)
        elif  y is not None:


         print("value of y : " , y)
        else:

         print("value of  y : ", z)
obj=Movrld()
obj.getdata(10)
obj.getdata(y= 10)

obj.getdata(y=30,z=20)
obj.getdata(z=40)


def getdata(id=None, name=None, sal=None):  # Ex for static poly...
    print("Data : ", id, name, sal)


getdata()  # getdata(id=None,name=None,sal=None)
getdata(45)  # getdata(id=10,name=None,sal=None)
getdata(45, 'Rinky')  # getdata(id=10,name='ali',sal=None)
getdata(45, 'Rinky', 10000)  # getdata(id=10,name='ali',sal=1000)


class Sply:
    def __init__(self,id=None,name=None,sal=None):
        self.id = id
        self.name=name
        self.sal=sal
        print(self.id,self.name,self.sal)

    def getdata(self):
      sal =self.sal+self.sal*25/100
      print("1st method : " , self.id,sal)
    def getdata(self):
        print("id and name of employee  : " , self.name)



obj=Sply(10,sal=89742)
obj.getdata()
obj.getdata()






#Operator Overloading
#TypeError: sum() takes at least 1 positional argument (0 given)
'''
class Add:

    def __init__(self,x):
        self.x=x
    def sum(self,y):
        z=self.x+y
        print("Sum of two no : " , z)
    def con(self,z):
        print("Concatinate two string : " , self.x+z)
obj=Add(4)
obj,sum()
obj.con()


'''
 

class Oprtrovrld:
    def __init__(self,i,j):
        self.i=i
        self.j=j
    def __add__(self, o):
     print("Adding of two no : ", self.i+o.j,self.j+o.j)
    def __sub__(self, o):
     print("Subtraction  of two no : ", self.i+o.j,self.j+o.j)
obj= Oprtrovrld(4,9)
obj2=Oprtrovrld(5,7)
obj3=obj+obj2
#print(obj3)



# Solution is use one single method with default arguments for parameters


def getdata(id=None, name=None, sal=None):  # Ex for static poly...
    print("Data : ", id, name, sal)


getdata()  # getdata(id=None,name=None,sal=None)
getdata(10)  # getdata(id=10,name=None,sal=None)
getdata(10, 'Rinky')  # getdata(id=10,name='Rinky',sal=None)
getdata(10, 'Rinky', 1000)  # getdata(id=10,name='Rinky',sal=1000)
getdata(name='Rinky',sal=12000)
getdata(10,sal=50000)
getdata(sal=40000)
getdata(name='Rinky')

#This method will exhibit Static polymorphism'''

# *args  **kwargs : Will see in decorator concept



def getdata(*args):
    print("Data : ", id, name, sal)


getdata()
getdata(10)
getdata(10, 'Rinky')
getdata(10, 'Rinky', 1000)
getdata(name='Rinky',sal=12000)
getdata(10,sal=50000)
getdata(sal=40000)
getdata(name='Rinky')






"""
print('Program to overload + operator for Book class objects:')


class Book:
    def _init_(self, pages):
        self.pages = pages

    def _add_(self, other):
        return self.pages + other.pages


b1 = Book(100)
b2 = Book(200)
print('The Total Number of Pages:', b1 + b2)


Overloading > and <= operators for Student class objects


class Student:
    def _init_(self, name, marks):
        self.name = name
        self.marks = marks

    def _gt_(self, other):
        return self.marks > other.marks

    def _le_(self, other):
        return self.marks <= other.marks


print("10>20 =", 10 > 20)
s1 = Student("Ali", 100)
s2 = Student("Hussain", 200)
print("s1>s2=", s1 > s2)
print("s1<s2=", s1 < s2)
print("s1<=s2=", s1 <= s2)
print("s1>=s2=", s1 >= s2)


class ClassA:
    def method1(self):
        print('this method belongs to class classA')


class ClassB:
    def method1(self, a):
        print('this method belongs to class classB')


ObjB = ClassB()
ObjB.method1(10)

ObjB.method1()  

# ObjB.method1()  # it will return error so overloading will not support
#TypeError: method1() missing 1 required positional argument: 'a'

print('.......................................................')
print("Constructor overloading")


class Test:
    def _init_(self, a=None, b=None, c=None):
        self.a = a
        self.b = b
        self.c = c
        print('Constructor with 0|1|2|3 number of arguments')


t1 = Test()
t2 = Test(10)
t3 = Test(10, 20)
t4 = Test(10, 20, 30)

print('...........................................................')


class Test:
    @staticmethod
    def sum_1(a=None, b=None, c=None):
        if a is not None and b is not None and c is not None:
            print('The Sum of 3 Numbers:', a + b + c)
        elif a is not None and b is not None:
            print('The Sum of 2 Numbers:', a + b)
        else:
            print('Please provide 2 or 3 arguments')


t = Test()
t.sum_1(10, 20)
t.sum_1(10, 20, 30)
t.sum_1(10)



class Employee:
    # STATE --> data members  *  logical
    def _init_(self, eid, name, sal):
        self.eid = eid
        self.name = name
        self.sal = sal

    # BEHAVIOR --> member methods   * physical

    @staticmethod
    def get_details():
        print("Employee details")


# Employee.get_details()
obj = Employee(1001, 'Rinky', 10000)  # data physical methods logical
obj.get_details()

#Class   - Variables - Logical    <===>  Methods  - Physical
#@Object  - Variables - Physical    <===>  Methods  - Logical




class University:
    # State
    def _init_(self, u_id, u_name, u_loc):
        self.u_id = u_id
        self.u_name = u_name
        self.u_loc = u_loc

    # Behaviour

    def u_data(self):
        print("Instance method ..........")
        print("University Data :", self.u_id, self.u_name, self.u_loc)

    @staticmethod
    def dep_data():
        dep = 'Electronics'
        print("Static method ...........")
        print("Department :", dep)

    @classmethod
    def branch_data(cls, branch):

        print("Class method ..............")
        print("Branch :", branch)


u = University(5784263, "Ranchi Uni", 'Ranchi')
u.u_data()
u.dep_data()
u.branch_data('CS')
"""