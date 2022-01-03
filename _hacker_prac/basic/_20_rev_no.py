
class A:

    def __init__(self):
        self.number=int(input("Enter a positive integer: "))


    def rev_nubr(self):
        rev = 0
        number=self.number
        while(number!=0):
            digit = number%10
            rev = (rev*10)+digit
            number = number//10
        print("The reversed number :",rev)


a=A()
a.rev_nubr()