#requirement : Add two no
#Behavior

def add(n1,n2):   # Parameter
# Function body
 result= n1+n2
 print("Sum of a no = " ,result)    # Responsibility

 #State
add(10,75)     # Argument



#Behavior
def add(n1,n2):   # Parameter
# Function body
 result= n1+n2
 print("Sum of a no = " ,result)    # Responsibility

 #State
add(10+60,75)     # Argument




#Behavior
def add(n1,n2):   # Parameter
# Function body
 result= n1+n2
 print("Sum of a no = " ,result)    # Responsibility

 #State
add(10+60,75-85)     # Argument




#Behavior
def add(n1,n2):   # Parameter
# Function body
 result= n1+n2
 print("Sum of a no = " ,result)    # Responsibility

 #State
n=int(input("Enter a no"))
add(n,75-85)     # Argument


#Behavior
def add(n1,n2):   # Parameter
# Function body
 result= n1+n2
 print("Sum of a no = " ,result)    # Responsibility

 #State
n=int(input("Enter a no"))
add(n,0)     # Argument


#Behavior
def add(n1,n2):   # Parameter
# Function body
 result= n1+n2
 print("Sum of a no = " ,result)    # Responsibility

 #State
#n=int(input("Enter a no"))
print("zero")
add(0,0)     # Argument



#Behavior
def add(n1,n2):   # Parameter
# Function body
 result= n1+n2
 print("Sum of a no = " ,result)    # Responsibility

 #State
n=int(input("Enter a no"))
print("zero")
add(0,0)     # Argument




#requirment : Increase 30% from current salary
#Behavior
def hike(sal=30000):     # Function defination
 fsal=sal+sal*30/100
 print("After hike sal =  ", fsal)        # Responsibility
 #State
hike()    # function calling without argument



#requirment : Deduct 10% from current salary
#Behavior
def deduct(sal):   #Function Calling
 fsal=sal-sal*10/100
 print("After deduction sal is =  " , fsal)    # Responsibility
#State
esal=int(input("Enter sal of employee"))
deduct(esal)     # function calling with argument

#requirment : Add new data in exist list
#Behavior

def list(lst):    #Function definition
  print(lst)
  lst1 = []
  lst.append("rasnami")
  print(lst)
  # State
fruits = ['Apple', 'Mango', 'Banana', 'Cherry']
list(fruits)       #Function Calling


#requirment : Add set in exist list
#Behavior

def list(lst,sn):     ##Function definition
  print(lst)
  lst1 = []
  lst.append("rasnami")
  lst.append(sn)
  print(lst)      #['Apple', 'Mango', 'Banana', 'Cherry', 'rasnami', {1, 2, 3, 4}]
fruits = ['Apple', 'Mango', 'Banana', 'Cherry']
sl={1,2,3,4}
list(fruits,sl) # Function calling


#requirment : Add set in exist list
#Behavior

def list(lst,sn):     ##Function definition
  print(lst)
  lst1 = []
  lst.append("rasnami")
  lst.append(sn)
  print(lst)      #['Apple', 'Mango', 'Banana', 'Cherry', 'rasnami', {1, 2, 3, 4}]
fruits = ['Apple', 'Mango', 'Banana', 'Cherry']
sl={1,2,3,4}
list(fruits,sl) # Function calling













