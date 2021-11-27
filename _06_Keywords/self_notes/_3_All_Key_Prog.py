# The True & False Keywords
print("------------true & false keywords------------")

print( 15>20)    #False
print(15<20)     #True
print("-----------------------------------")

a='Rama'
b='Rama'
c="rama"
d="Rama"
print(a == b)     #True
print(c == b)     #False
print(d==a)       #True
print(a>b)        #False
print("----------------------------------")

lst=['Ram', 'Shyama','Geeta' ,'Seeta']
lst1=['Ram', 'Shyama','Geeta' ,'Seeta']
print(lst==lst1)    #True
print(lst is lst1)  #False

lst=['Ram', 'Shyama','Geeta' ,'Seeta']
lst1=['Rama', 'Shyama','Geeta' ,'Seeta']
print(lst==lst1)     # False

print("----------------------------------")

tpl =('Ram', 'Shyama','Geeta' ,'Seeta',)
tpl1 =('Rama', 'Shyama','Geeta' ,'Seeta','Rama',)
print(tpl1)  # ('Rama', 'Shyama', 'Geeta', 'Seeta', 'Rama')
tpl3 =('Ram', 'Shyama','Geeta' ,'Seeta')
print(tpl==tpl1)     #False
print(tpl<tpl1)      #True
print(tpl==tpl3)     #True
print(tpl is tpl3)   #True

print("----------------------------------")

set ={'Rama', 'Shyama','Geeta' ,'Seeta',}
set1 ={'Rama', 'Shyama','Geeta' ,'Seeta','Rama'}
print(set1) # {'Shyama', 'Rama', 'Seeta', 'Geeta'}
set3 ={'Rama', 'Shyama','Geeta' ,'Seeta'}
print(set==set1)     #True
print(set<set1)      #False
print(set==set3)     #True
print(set is set3)   #False

print("-----------------***********************************-----------------")

print("----------------The class, def, return Keywords-------------")
# class

class Person:
    "This is a person class"
    age = 10
    def greet(self):
        print('Hello')
print(Person.age)         #10
print(Person.greet)      #<function Person.greet at 0x00000207B973DEE0>
print(Person.__doc__)    #This is a person class
print("------------------------------------")
class Person:
    age = 10
    def greet(self):
        print('Hello')
print(Person.age)         #10
print(Person.greet)      #<function Person.greet at 0x00000207B973DEE0>
print(Person.__doc__)    # None

print("-------------------------------------------------------------")
# def
def info(fname,lname):
    print("First name: " + fname + " " + "Last name : " +  lname ) #First name: Paul Last name : Sahu
info('Paul', 'Sahu')
print("-------------------------------------")
def list(lst):
  for inx in lst:
    print("List of Fruits : " + inx)

fruits=["Apple", "Banana","cherry","Mango"]
print(fruits)
list(fruits)
print("-------------------------------------")
def tpl(lst):
  for inx in lst:
    print("List of Fruits : " + inx)
fruits=("Apple", "Banana","cherry","Mango","Mango")
print(fruits)
tpl(fruits)
print("-------------------------------------")
def set(st):
  for inx in st:
    print("List of Fruits : " + inx)

fruits={"Apple", "Banana","cherry","Mango","Mango"}
print(fruits)
set(fruits)
print("----------------*****************************---------------------")
#return

def add(x,y):
    return x+y
c=add(2,5)
print("Addition of two no :",  +c)

print("---------------------------------------------------------------------")
def list(lst):
    print(lst)
    lst1 = []
    for inx in lst:
        print(inx)
    lst1=inx
    lst.append("rasnami")
    print(lst)
    return lst

fruits = ['Apple','Mango','Banana', 'Cherry']

lfruits =list(fruits)
print("final list: ",lfruits)

for flst in lfruits:
  print("List of fruits : ", flst)

print("-----------------------------------------------")
def dict(dic):
    print("data :", dic)
    dict1 = {}
    key={}
    for key in dic.items():
     print("datas", key)
    dict1=key
    print(dict1)
     #dict1.append('marks':80)
    return dict1

data = {'Name':'Ram','Roll No':1, 'class':'IV'}

lfruits =dict(data)
print("final list: ",lfruits)

for flst in lfruits:
  print("List of fruits : ", flst)

print("------------------The if, elif, else Keywords-----------------")

#if
a=20
b=30
if a<b:
    print("a is less than b")
print("----------------------------------------------------------")
str="Rama"
str1="rama"
if str is not str1:
    print("String value u assigned")
print("----------------------------------------------------------")

list1 = [58, 21, 3, 45, 6, 91,85,45,78]
for num in list1:
  if num % 2 == 0:
   print("even no", num)
print("------------------------------------------")
#if & else
list1 = [58, 21, 3, 45, 6, 91,85,45,78]
for num in list1:
 if num % 2 == 0:
    print("even no", num)
 else:
  print("odd no ", num)
print("------------------------------------------")

num=int(input("enter any no"))
if num%2==0:
    print(num ,"Given no is even")
else:
    print(num ,"Given no is odd")


















