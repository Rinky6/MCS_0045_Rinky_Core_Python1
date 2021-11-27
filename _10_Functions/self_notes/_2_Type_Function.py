#Types
'''
1. Predefined Functions   : print() id() type()   int float str list tuple dict set
2. User defined Functions : Programmer defined functions


Predefined Functions
======================

x=10
x= Variable
10=value
= --> operator

Function definition syntax :

def <func_name> () :       # f(var)
# def sum(n1, n2):         # f(x)

n1,n2 are parameters not variables


# Requirement : Sum of 2 given numbers

# A. With out functions
        # I. STATE
num1 = 10
num2 = 20
        # II. BEHAVIOR
result = num1 + num2
print("Addition is : ", result)


print("-----------Using functions--------")
# B. With Functions
        # I. STATE
num1 = 10
num2 = 20
        # II. BEHAVIOR

# Function definition
def sum(n1, n2):       # function signature
    result = n1 + n2   # function body
    print("Addition is : ", result)

# Function calling
sum(num1, num2)
sum(10, 20)
--------------------------------------------------------------------------

# Requirement : factorial of given numbers

# A. With out functions
        # I. STATE
num = int(input("Enter a no"))
f = 1
# II. Behavior
while num>1:
 f = f * num

 num -= 1

print("factorial of a no", f)


# B. With  functions
num = int(input("Enter a no"))
# II. Behavior
# Function Definition
def fact(i):
 f = 1
 while i>1:
  f = f * i
  i-=1
 print("Factorial of a no:" ,f)

fact(num)

-----------------------------------------------------------------------------------------

# Requirement : Check greatest no of  given 3 numbers

# A. With out functions
# I. STATE
num1 = int(input("Enter a 1st no"))
num2 = int(input("Enter a 2nd no"))
num3 = int(input("Enter a 3rd no"))

# II. Behavior
if num1 > num2 and num1 > num3:
    print("Greatest no :",num1)

elif num2 > num3:
    print("Greatest no :",num2)
else:
 print("Greatest no :",num3)


# A. With  functions

# II. Behavior
# Function Definition
def greatest(n1,n2,n3):
    if n1 > n2 and n1 > n3:
        print("Greatest no :", n1)

    elif n2 > n3:
        print("Greatest no :", n2)
    else:
        print("Greatest no :", n3)


# I. STATE
num1 = int(input("Enter a 1st no"))
num2 = int(input("Enter a 2nd no"))
num3 = int(input("Enter a 3rd no"))
greatest(num1,num2,num3)






'''




