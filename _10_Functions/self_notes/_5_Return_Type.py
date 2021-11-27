#Return Type

#Requirement: Add two nos
#Without return type
#State
x=30
y=40

def add(a,b): #Function Definition
  #Business Logic
  print("Addition of two no  : ", a+b)     #Responsibility

add(x,y)   # Function Calling

'''
Here  x= 30     
      y=40      #   x,y<==> variable;  30,40 <==> Value
     add(a,b) <===>  Parameter
     add(x,y)<===> Arguments
'''
#With return type
#State
x=30
y=40

def add(a,b): #Function Definition
  #Business Logic
   sum = a+b
   return sum

sum=add(x,y)   # Function Calling
print("Addition of two no using return type  : ", sum)


#Requirement: check given no is even or not


#With return type
#State
num=int(input("Enter a no"))

def check(n): #Function Definition
  #Business Logic
   if n%2==0:
    return n
   else:
     print("Enter no is not a even")

n1=check(num)   # Function Calling
print("Addition of two no using return type  : ", n1)   # Addition of two no using return type  :  44


'''
scenario 1
Enter a no 45
Enter no is not a even
Addition of two no using return type  :  None


scenario 2

Enter a no88
Addition of two no using return type  :  88

'''


#With return type
#State
num=int(input("Enter a no"))

def check(n): #Function Definition
  #Business Logic
   if n%2==0:
    return 1
   else:
     return 0

n1=check(num)   # Function Calling
print("Addition of two no using return type  : ", n1)

'''
Enter a no45
Addition of two no using return type  :  0


Enter a no44
Addition of two no using return type  :  1
'''

# Requirement : check the no is even or not,if even multiply with 4 otherwise multiply with 9

#With return type
#State
num=int(input("Enter a no   "))

def check(n): #Function Definition
  #Business Logic
   if n%2==0:
    return 1
   else:
     return 0

n1=check(num)   # Function Calling
if n1==1:
  multi=num*4
  print ("multiplication of even no =  ", multi)
else:
    multi1=num*9
    print("multiplication of odd no =  ", multi1)

'''
Enter a no 5 
Addition of two no using return type  :  0
multiplication of odd no =   45


Enter a no   4
multiplication of even no =   16

'''

# Requirement : Find the factorial and multiply with 10
#With return type
#State

def fact(i):
      f = 1
      while i > 1:
          f = f * i
          i -= 1
      print("Factorial of a no:", f)
      return f
f1=fact(num)
multi = f1*10
print("After multiplying with factorial  " , multi)

'''
Factorial of a no: 120
After multiplying with factorial   1200

'''
# with factorial() <===> without using return type & function
import math
n=int(input("enter a no"))
print("Factorial of no", math.factorial(n))


# with factorial() <===> with using return type function
#state
n=int(input("enter a no  "))
def fact(n):   #Function definition
    # function body
     f=math.factorial(n)
     return f
f=fact(n)   # function calling
print("factorial of a no  ", f)

# using for loop

n=int(input("enter a no  "))
def fact(n):   #Function definition
    # function body
    f=1
    for i in range(1,n+1):
     f= f*i
     i+=1
    print(f)
    return f
f=fact(n)   # function calling
print("factorial of a no  ", f)


