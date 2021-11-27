class Pclass:
    def __init__(self,name,address,sal):
        self.name=name
        self.address=address
        self.sal=sal
    def pm1(self):
        print("name and address :", self.name,self.address)
    def pm2(self):
        sal=self.sal+self.sal+25/100
        print("sal is : ", sal)


class Cclass(Pclass)      :
    def m1(self):
        Pclass.pm1(self)
        print("child method1")
    def m2(self):
        print("child method 2")
        Pclass.pm2(self)
obj=Cclass("Ram","Ranchi",10000)
obj.m1()
obj.m2()





class Calculator:
    c=0

    def __init__(self,a,b):
        self.a=a
        self.b=b
    def sum(self):
        c=self.a+self.b
        print("sum of two no : ", c)
    def subs(self):
        c=self.a-self.b
        print("subtraction of two no : ", c)
    def multi(self):
        c=self.a*self.b
        print("multiplication of two no : ", c)
    def modu(self):
        c=self.a % self.b
        print("modulus of two no : ", c)
    def div(self):
        c = self.a / self.b
        print("Division of two no : ", c)


class Operations(Calculator)  :
    def action(self):
       Calculator.sum(self)
       print("child method")
       Calculator.subs(self)
       Calculator.multi(self)
       Calculator.modu(self)
       Calculator.div(self)
x=int(input("Enter value of x"))
y=int(input("Enter value of y"))
obj1= Operations(x,y)
obj1.action()








