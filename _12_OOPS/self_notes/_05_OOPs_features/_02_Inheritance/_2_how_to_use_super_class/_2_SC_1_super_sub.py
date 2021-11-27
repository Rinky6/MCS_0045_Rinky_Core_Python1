'''  REUSE*
I: All sub classes required
                method signature -  common
                method body      -  common** implementation
'''

"""
Electronic gadget
   Fan                    AC                   laptop               laptop                    
(electricity)        (electricity)           (electricity)        (electricity)             
                                            
   
                                                        (Charge)
  """


class E_Gadget:
    def __init__(self):
        print("Super class")


    def electricity(self):
     print("Need electricity")


class Fan(E_Gadget):
    print("Fan is working")


class AC(E_Gadget):
    print("AC is working")


class Laptop(E_Gadget):
    print("laptop working")
    def charge(self):
        print("put in charge")
class Mobile(Laptop):
    print("mobile is working")
    def charge(self):
     pass
obj=E_Gadget()
obj.electricity()


obj1=Laptop ()
obj1.charge()
obj1.electricity()

obj2 = Mobile()
obj2.electricity()


# Single Inheritance


class Fruits:
    def __init__(self):
        print ("Super class")
    def health(self):
        print("Fruits are good for health")

class Apple(Fruits):
    print("Inherit super class properties into sub class")
    def __init__(self):
        pass
obj=Fruits()
obj.health()


class Person():

    # Constructor
    def __init__(self, name):
        self.name = name

    # To get name
    def getName(self):
        return self.name

    # To check if this person is an employee
    def isEmployee(self):
        return False


# Inherited or Subclass (Note Person in bracket)
class Employee(Person):

    # Here we return true
    def isEmployee(self):
        return True


# Driver code
emp = Person("Rinky")  # An Object of Person
print(emp.getName(), emp.isEmployee())

emp = Employee("Manu")  # An Object of Employee
print(emp.getName(), emp.isEmployee())


class Person():

    # __init__ is known as the constructor
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber

    def display(self):
        print(self.name)
        print(self.idnumber)


# child class
class Employee(Person):
    def __init__(self, name, idnumber, salary, post):
        self.salary = salary
        self.post = post
        print("Details of emp :  ", self.salary,self.post)

        # invoking the __init__ of the parent class
        Person.__init__(self, name, idnumber)

    # creation of an object variable or an instance


a = Employee('Shyama', 886012478, 200000, "Trainee")

# calling a function of the class Person using its instance
a.display()






#Multiple Inheritance

class Parent1:
   pass

class Parent2:
   pass

class Child(Parent1, Parent2):
   pass

if issubclass(Child, (Parent1, Parent2)):
   print("Child is a subclass of Parent1 and Parent2")



class Parent1:

   def display1(self):
       print("In class Parent1")

class Parent2:

   def display2(self):
       print("In class Parent2")

class Child(Parent1, Parent2):
    print("Inherit properties from two diff class")

obj = Child()
obj.display1()
obj.display2()



class A:

   def display(self):
       print("Class A")

class X(A):

   def display(self):
       print("Class X")

class Y(A):

   def display(self):
       print("Class Y")

class Z(X, Y):
   pass

obj = Z()
obj.display()



class A:

   def display(self):
       print("Class A")

class X(A):

     print("working")

class Y(A):

   def display(self):
       print("Class Y")

class Z(X, Y):
   pass

obj = Z()
obj.display()







#multilevel Ingeritance



class Mobile:
    def __init__(self):
        print("Super class")
    def charge(self):
        print("put in charge")
class Samsung(Mobile) :
     print("Battary backup is working fine")

class Realme(Mobile):
    print("Camera is good")
obj=Mobile()
obj.charge()




class Grandfather:
    def __init__(self,name,padds):
     self.name=name
     self.padds=padds
    def get_nads(self):
     return self.name, self.padds

class Father(Grandfather)   :
    def __init__(self,name,padds,age):
        Grandfather.__init__(self, name, padds)
        self.age=age
    def get_Age(self):
     return self.age
class Son(Father):
    def __init__(self,name,padds,age,adds):
     Father.__init__(self, name, padds, age)
     self.adds=adds
     def get_A(self):
      return adds
obj =  Grandfather("Ramya","Ranchi",40, "Bangaluru" )
print(obj.get_nads,obj.get_age,obj.get_A)







