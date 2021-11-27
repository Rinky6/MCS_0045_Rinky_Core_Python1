#Calling a Function

'''
To call a function, use the function name followed by parenthesis:
Requirement: Add two no
#function defination

def add(n1,n2):    # function signature
  "#function body"
  n3= n1+n2
  print("sum of a no", n3)
add(87,52)   # Function calling
------------------------------------------------

#Requirement :  check Enter no is +ve or -ve
#State
num=int(input("Enter a no"))
# Behavior

def check(num): #Function Definition
# Function body
 if num>0:
  print(num,"is +ve no")
 else:
  print(num,"is -ve no")

check(num)     # calling function
------------------------------------------
#Requirement :  print table
# Behavior
def multi(n): #Function Definition
 print(n)
 i=1
 while i<11:
  result=i*n
  i += 1
  print("Table of",n, "is =",result)
#State
num = int(input("Enter a no"))
multi(num)     # calling function

-------------------------------------------------

#Requirement :  print table
# Behavior
def multi(n): #Function Definition
 print("Table of ", n ,"is")
 i=1
 while i<11:
  result=i*n
  i += 1
  print(result)
#State
num = int(input("Enter a no"))
multi(num)     # calling function
-------------------------------------------------
#Requirement :  Concatinate name enter name
# Behavior
def multi(fn,ln): #Function Definition
 full_name = fn +" "+ ln
 print("Full Name of student",full_name)
#State
fname= input("Enter first name of Student")
lname= input("Enter last name of Student")
multi(fname,lname)     # calling function

-------------------------------------------------
#Requirement :  Concatinate enter name and marks
# Behavior
def multi(fn,ln,m): #Function Definition
 details = fn +" "+ ln + "    Marks =", m
 print("Full Name of student",details)

#State
fname= input("Enter first name of Student")
lname= input("Enter last name of Student")
marks = int(input("Enter marks of student"))
multi(fname,lname,marks)     # calling function
'''










