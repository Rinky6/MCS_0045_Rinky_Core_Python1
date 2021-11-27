'''
Instance variables
Instance methods
'''

def func1():
    print("Funciton1 body")

func1()

class Employee:
    # local variables   - eid, name, sal
    # instance variables - self.eid self.name self.sal - instance variables

    def __init__(self, eid, name, sal):
        print("Self address : ", self)
        self.eid = eid
        self.name = name
        self.sal = sal

    # instance methods
    def get_edata(self):
        print("Employee information : ", self.eid, self.name, self.sal)


infemp = Employee(100, 'Ramaya', 15000)
infemp.get_edata()
# Employee.get_edata(infemp)




li1 = [1, 2, 3]  # list1 is of type class list
li1.append(100)  # list.append(li1,100)
li1.pop()        # list.pop(li1)





class Student :
    college_name= "Shyama Mukharjee College Ranchi"
    num_students = int(input("Please enter number of students:"))
    def __init__(self,roll_no,sname,stream,):
        self.roll_no=roll_no
        self.sname = sname
        self.stream = stream

    def s_info(self):
        print("Details of Students:   ",self.roll_no,self.sname,self.stream,Student.college_name)


roll_no=int(input("Enter roll no of Students"))
sname=input("Enter name of students")
stream=input("Enter Stream of students")

student=Student(roll_no,sname,stream)
Student.s_info(student)
print("Student details")
