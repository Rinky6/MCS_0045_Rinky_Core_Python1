from abc import ABC,abstractmethod
class Human(ABC):

    def eating(self):
        print("All humans are eating")


  # @abstractmethod
  #  def sleeping(self):          Can't instantiate abstract class Student with abstract method sleeping
     #   pass

class Employee(Human):
    def sal(self):
        print("Employee getting sal")
    def sweng(self):
        print("Employee designation are software eng")

class Student(Human):
    def study(self):
        print("Students are studing")

obj= Student()
obj.study()

obj.eating()