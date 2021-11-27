class Calculator:
    def __init__(self):
        print("super class")

    def operation(self):
     print("Start  calculating")
class Cal(Calculator):
    def __init__(self):
     print("First child class")
    def operations(self,
                   ):
     def operation(self,a,b):  # method overloading
      c=a+b
      print("Addition of two no", c)



obj =Cal()
obj.operation(8,2)




