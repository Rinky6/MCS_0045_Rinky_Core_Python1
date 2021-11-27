'''We come across different kinds of arithmetic operations in which multiple data types are involved and then results are obtained accordingly.

Here we will discuss both,

    Implicit type conversion
    Explicit type conversion'''

#Implicit type conversion

a=20
print("value of a : " , a)
print("value of a after typcasting", float(a))

a="Ram"
print("value of a : " , a)
#print("value of a after typcasting", float(a))   #could not convert string to float: 'Ram'

class Person:

  def eating(self):
      print("persons are eating")


class Student(Person):
    def study(self):
        print("Students are studying")

obj = Person()
obj.eating()
#obj.study()   #'Person' object has no attribute 'study'
obj1= Student()
obj.eating()
obj1.study()







