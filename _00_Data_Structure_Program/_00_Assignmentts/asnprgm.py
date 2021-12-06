#1.) Write a Python program to convert degree to radian.formula - degree*(pi/180)
d=int(input("enter degree"))
r=d*3.14/180
print("After convert degree to radian : ", r)

#2.) Write a Python program to calculate the area of a trapezoid.  formula - ((base_1 + base_2) / 2) * height

b1=float(input("enter first side of trapezoid")   )
b2=float(input("enter first side of trapezoid"))
h=float(input("enter height of trapezoid"))
area=h*(b1+b2)/100
print("After convert degree to radian : ",area)


'''
3.) Write a program that asks the user to enter two integers. 
	Have the program output the two integers and the result when the first number entered is raised 
	to the power of the second number entered.

'''
fno=int(input("Enter first no"))
sno=int(input("Enter second no"))
result=fno**sno
print("After calculation result is : ", result)



'''
4.) Write a computer program that asks the user to enter an integer (odd or even) and have it report
    whether the integer entered is odd. 
	You are required to implement this program using the modulus operator and an if ... Selection construct.

'''

n=int(input("Enter a no"))
if n%2==0:
    print(n ,  "Enter no is even")
else:
    print(n, "enetr no is odd")

'''
5.) Write a Python program to calculate the area of a parallelogram.
	formula - base * height
'''
base=float(input("Enter base of parallelogram"))
height=float(input("Enter height of parallelogram"))
area=base*height
print("Area of parallelogram : " ,area)