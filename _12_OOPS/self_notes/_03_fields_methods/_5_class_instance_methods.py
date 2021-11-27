# class method


class Employee:
    e_count = 0
    office = 'ORACLE'

    @classmethod
    def get_edata(cls):
        #print("Employees info : ",Employee.e_count,Employee.office)
        print("Employees info : ", cls.e_count, cls.office)
    '''
    def __init__(self):
        pass
    '''
# no need to create object to call class methods
Employee.get_edata()  # Employee.get_edata(Employee)

#2 way - Don't do it
obj = Employee()
print("Object address : ",obj)
obj.get_edata()  # ==> Employee.get_edata(obj)


'''
class Student:
    cname="Marwari College Ranchi"
    pname = "Nirmala Lucus"
   # @classmethod
    def info_std(std):
        print("info of students  : " , std.cname,std.pname)   
    ***********info_std() missing 1 required positional argument: 'std'
Student.info_std()
'''




class Student:
    cname="Marwari College Ranchi"
    pname = "Nirmala Lucus"
    @classmethod
    def info_std(std):
        print("info of students  : " , std.cname,std.pname)
Student.info_std()




print("------All methods---------")
class Employee:
    e_count = 0
    office = 'ORACLE'

    def __init__(self, eid, name, sal):
        self.eid = eid
        self.name = name
        self.sal = sal
        Employee.e_count += 1

    @classmethod
    def get_edata(cls):
        print("Employees info : ",Employee.e_count,Employee.office)
        print("Employees info : ", cls.e_count, cls.office)


    def get_empinfo(self):
        print("Employee details : ", self.eid, self.name, self.sal)
        Employee.get_edata()
        # self.get_edata()




# to call class method
Employee.get_edata()
# to call instance method
madhu = Employee(101, 'Madhu Nettem', 15000)
madhu.get_empinfo()
madhu.get_edata()
Employee.get_edata()



class Student:
    cname="Marwari College Ranchi"
    pname="Nirmala Lucas"


    def __init__(self ,roll_no, sname):
      self.roll_no=roll_no
      self.sname=sname
    def sinfo(self) :
      print("Student info : ", self.roll_no,self.sname,Student.cname,Student.pname)

    @classmethod
    def get_info(std):
     print("info of student : ", std.cname,std.pname)

Student.get_info()
obj= Student(11,"Ramaya")
obj.sinfo()
obj.get_info()

print("-----static method--------")

# i want a behavior which neither deals with class variables nor instance variables

class Employee:
    @staticmethod
    def getinfo():
        print("Static method implementation")

Employee.getinfo()
