# Function categories
'''
1. Function with parameters, with return type
2. Function with parameters, without return type
3. Function without parameters, with return type
4. Function without parameters, without return type
'''

# 1. Function with parameters, with return type
#Requirment : Addition of two no
#state
x=10
y=20

def add(n1,n2):   #Function definition
 return n1+n2   # Returning a value

num=add(x,y) # function calling
print("Addition of two no  ", num)
'''
Here  x=10  
      y=20
      # x,y <==> variable ;; 10 ,20 <==> value
      def add(n1,n2)     # Parameter
      num=add(x,y)       # Argument
'''



#Requirment : check greatest no between three no
#state
x=10
y=20

def check(n1,n2,n3=40):   #Function definition
    if n1>n2 and n1>n3:
      return n1
    elif n2>n3:
     return n2
    else:
     return n3

num=check(x,y) #function calling
print("Biggest no is  ", num)     #Biggest no is   40


#Requirment : check greatest no between three no
#state
x=10
y=20

def check(n1,n2,n3=40):   #Function definition
    if n1>n2 and n1>n3:
      return n1
    elif n2>n3:
     return n2
    else:
     return n3

num=check(x,y,30) #function calling
print("Biggest no is  ", num)     # Biggest no is   30





#Requirment : check greatest no between three no
#state
x=10
y=20
z=58.2

def check(n1,n2,n3=40):   #Function definition
    if n1>n2 and n1>n3:
      return n1
    elif n2>n3:
     return n2
    else:
     return n3

num=check(x,z,y) #function calling
print("Biggest no is  ", num)     # Biggest no is   58.2




#Requirment : check greatest no between three no
#state
x=30
y=10
z=10

def check(n1,n2,n3=40):   #Function definition
    if n1>n2 and n1>n3:
      return n1
    elif n2>n3:
     return n2
    else:
     return n3

num=check(n1=z,n2=y) #function calling
print("Biggest no is  ", num)     # Biggest no is   40





#Requirment : check greatest no between three no
#state
x=30
y=10
z=10

def check(n1,n2,n3=40):   #Function definition
    if n1>n2 and n1>n3:
      return n1
    elif n2>n3:
     return n2
    else:
     return n3

num=check(n3=x,n1=z,n2=y) #function calling
print("Biggest no is  ", num)     # Biggest no is   30


# 2. Function with parameters, without return type



#req: Add new data in given list
#State

list=["Rama", "Seeta ", "Laxmana" ,"Vibhishana"]

def add(lst):     #Function Definition
    # Business calll

    lst.append("Shyama")
    print("List of candidates   : " ,lst)     # Responsibility      List of candidates   :  ['Rama', 'Seeta ', 'Laxmana', 'Vibhishana', 'Shyama']
add(list)     #Function Calling



#State
list=["Rama", "Seeta ", "Laxmana" ,"Vibhishana"]
tpl=(1,2,3,4,5,6)
def add(lst,tp):     #Function Definition
    # Business calll
    lst.append("Shyama")
    lst.append(tp)
    print("List of candidates   : " ,lst)     # Responsibility
#List of candidates   :  ['Rama', 'Seeta ', 'Laxmana', 'Vibhishana', 'Shyama', (1, 2, 3, 4, 5, 6)]
add(list,tpl)     #Function Calling



#State

list=["Rama", "Seeta ", "Laxmana" ,"Vibhishana"]
def add(lst,tpl=(1,2,3,4,5,6)):     #Function Definition
    # Business calll
    lst.append("Shyama")
    lst.append(tpl)
    print("List of candidates   : " ,lst)     # Responsibility
#List of candidates   :  ['Rama', 'Seeta ', 'Laxmana', 'Vibhishana', 'Shyama', (1, 2, 3, 4, 5, 6)]
add(list)     #Function Calling



#State

list=["Rama", "Seeta ", "Laxmana" ,"Vibhishana"]
def add(lst,tp):     #Function Definition
    # Business calll
    lst.append("Shyama")
    lst.append(tp)
    print("List of candidates   : " ,lst)     # Responsibility
#List of candidates   :  ['Rama', 'Seeta ', 'Laxmana', 'Vibhishana', 'Shyama', (1, 2, 3, 4, 5, 6)]
add(list,(1,2,3,4,5,6))



#Req: List & set
#State

list=["Rama", "Seeta ", "Laxmana" ,"Vibhishana"]
def add(lst,set):     #Function Definition
    # Business calll
    lst.append("Shyama")
    lst.append(set)
    set.add("Manager")
    print("List of candidates   : " ,lst)     # Responsibility
#List of candidates   :  ['Rama', 'Seeta ', 'Laxmana', 'Vibhishana', 'Shyama', {'DS', 'HR', 'DA', 'Manager', 'S/W Eng'}]
add(list,{"HR","S/W Eng","DS","DA"})



#Req: List & dictionary

#State
list=["Rama", "Seeta ", "Laxmana" ,"Vibhishana"]
def add(lst,dic):     #Function Definition
    # Business calll
    lst.append("Shyama")
    lst.append(dic)
    print("List of candidates   : " ,lst)     # Responsibility
#List of candidates   :  ['Rama', 'Seeta ', 'Laxmana', 'Vibhishana', 'Shyama', {'1': 'HR', '2': 'S/W Eng', '3': 'DS', '4': 'DA'}]
add(list,{"1": "HR","2": "S/W Eng","3": "DS","4" : "DA"})






#3. Function without parameters, with return type
#req: add data in existing list and return
#State
def list():
    list = ["Rama", "Seeta ", "Laxmana", "Vibhishana"]
    list.append("Shayama")
    return list

lst=list()
print("list of candidates  ", lst)   #list of candidates   ['Rama', 'Seeta ', 'Laxmana', 'Vibhishana', 'Shayama']



#req: add data in existing set and return
#State
def set():
    set = {"Rama", "Seeta ", "Laxmana", "Vibhishana"}
    set.add("Shayama")
    return set

st=set()
print("list of candidates   ", st)   #list of candidates h  {'Shayama', 'Laxmana', 'Seeta ', 'Rama', 'Vibhishana'}


#4. Function without parameters, without return type

#req: add data in existing list and return
#State
def list():  #Without Parameter
    list = ["Rama", "Seeta ", "Laxmana", "Vibhishana"]
    list.append("Shayama")
    print("list of candidate : ", list )   #Responsibility

list()



#State
def set():  #Without Parameter
    st = {"Rama", "Seeta ", "Laxmana", "Vibhishana"}
    st.add("Shayama")
    print("list of candidate : ", st )   #Responsibility
    #list of candidate :  {'Vibhishana', 'Rama', 'Seeta ', 'Laxmana', 'Shayama'}

set()

















