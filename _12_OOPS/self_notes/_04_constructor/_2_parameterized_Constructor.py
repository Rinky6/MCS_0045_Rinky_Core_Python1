#Parameterized Constructor
'''
            - Positional arguments
            - Default arguments
            - keyword arguments
'''

class  Trainee:
    def __init__(self,tno,tname,tjd):    #  Positional arguments
        self.tno=tno
        self.tname=tname
        self.tjd=tjd
    def info_trainee(self):
        print("Information about Trainees  " , self.tno,self.tname,self.tjd)
info=Trainee("t101","Ramaya","09/08/2011")
info.info_trainee()



class  Trainee:
    def __init__(self,tno,tname,tjd="14/Aug/21"):    #  default arguments
        self.tno=tno
        self.tname=tname
        self.tjd=tjd
    def info_trainee(self):
        print("Information about Trainees  " , self.tno,self.tname,self.tjd)
info=Trainee("t101","Ramaya")   #t101 Ramaya 14/Aug/21
info.info_trainee()
#info=Trainee("t101")    #__init__() missing 1 required positional argument: 'tname'
#info.info_trainee()
info=Trainee("t101","Ramaya","09/08/2011")
info.info_trainee()





class  Trainee:
    def __init__(self,tno,tname,tjd):    #  keyword arguments
        self.tno=tno
        self.tname=tname
        self.tjd=tjd
    def info_trainee(self):
        print("Information about Trainees  " , self.tno,self.tname,self.tjd)
info=Trainee(tjd="25/Apr/2021",tno=106,tname="Sanaya")
info.info_trainee()

info=Trainee(106,tjd="25/Apr/2021",tname="Sanaya")
info.info_trainee()

#info=Trainee(106,"25/Apr/2021",tname="Sanaya")      #__init__() got multiple values for argument 'tname'
#info.info_trainee()


info=Trainee(106,"Sanaya",tjd="25/Apr/2021")
info.info_trainee()

class  Trainee:
    def __init__(self,tno=None,tname=None,tjd=None):    # Constructor overloading
        self.tno=tno
        self.tname=tname
        self.tjd=tjd
    def info_trainee(self):
        print("Information about Trainees  " , self.tno,self.tname,self.tjd)
info=Trainee("t101","Ramaya")
info.info_trainee()

info=Trainee("Ramaya")
info.info_trainee()

info=Trainee("Ramaya","14/02/2021")
info.info_trainee()

info=Trainee(tname="Ramaya",tjd="15/06/2021")
info.info_trainee()

info=Trainee(tno=101,tname="Ramaya",tjd="15/06/2021")
info.info_trainee()

#info=Trainee(tno=101,tname="Ramaya","15/06/2021")  #SyntaxError: positional argument follows keyword argument

info.info_trainee()

class Student:

    # Constructor - parameterized  
    def _init_(self, name):  
        print("This is parametrized constructor")  
        self.name = name  
    def show(self):  
        print("Hello",self.name)  
student = Student("John")  
student.show()

# Positional arguments


class Employee:
    # Parameterized Constructor
    def __init__(self, eid, name, sal):
        self.eid = eid
        self.name = name
        self.sal = sal

    def getedata(self):
        pass

satish = Employee(200, 'satish', 10000)
"""

'''
# Defining Constructor
    - Default constructor
    - Parameterized constructor
            - Positional arguments
            - Default arguments
            - keyword arguments

'''
# Default arguments example
"""
class Employee:
    # parameterized constructors
    def _init_(self, eid=None, name=None, sal=None):  # Constructor overloading
        self.eid = eid
        self.name = name
        self.sal = sal

    def getedata(self):
        print("Employee info : ", self.eid, self.name, self.sal)


satish = Employee()
satish.getedata()

sam = Employee(201)
sam.getedata()

venkat = Employee(201, 'Chandra Sekhar')
venkat.getedata()

ravi = Employee(200, 'MadhuN', 10000)
ravi.getedata()

raju= Employee(name='Farooq', sal=20000)
raju.getedata()


class Student:
    def _init_(self):
        print("The First Constructor")

    def _init_(self):
        print("The second contructor")


st = Student()  
"""
"""
class Student:
    def _init_(self, name, id, age):  
        self.name = name  
        self.id = id  
        self.age = age  

    # creates the object of the class Student  
s = Student("John", 101, 22)  

# prints the attribute name of the object s  
print(getattr(s, 'name'))  

# reset the value of attribute age to 23  
setattr(s, "age", 23)  

# prints the modified value of age  
print(getattr(s, 'age'))  

# prints true if the student contains the attribute with name id  

print(hasattr(s, 'id'))  
# deletes the attribute age  
delattr(s, 'age')  

# this will give an error since the attribute age has been deleted  
print(s.age)  
"""

"""
class Student:    

    def _init_(self,name,id,age):    
        self.name = name;    
        self.id = id;    
        self.age = age    

    def display_details(self):    
        print("Name:%s, ID:%d, age:%d"%(self.name,self.id))

s = Student("John",101,22)    
print(s._doc_)    
print(s._dict_)    
print(s._module_)
















