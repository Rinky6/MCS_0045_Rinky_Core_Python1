import calendar
cal=calendar.month(2022,11)
print(cal)

"""
  November 2022
Mo Tu We Th Fr Sa Su
    1  2  3  4  5  6
 7  8  9 10 11 12 13
14 15 16 17 18 19 20
21 22 23 24 25 26 27
28 29 30
"""

'''
y=10
#y += 2
#x = y += 2
print(y)  #invalid syntax
'''
i=2
for i in range(i<2):
    i=i+1
print("-----------",i) #2





x=[(3,2),(2,3)]
x.sort()
print(x)  #[(2, 3), (3, 2)]



x=y=[2,4,6]
y[2]=5
print(x) #[2, 4, 5]



'''for num in range(-2,-5,-1):
    print(num,end="") #-2-3-4

'''

#create calculator

x=input("Enter expression")
print("ouput", eval(x))


a,b=1>2,2>3

mylist=[a,b,a==b]
print(mylist)



def f1():
    x=100
    print(x) #100
x=+1
f1()

#generate password

import random
lower ="abcdefghijklmnopqrstuvwxyz"
upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
num ="123456789"
sym="~!@#$%^&*()_[]{}"
all=lower+upper+num+sym
length=16
#password ="".join(random.sample(all.length))
#print(password)


a=[]
x=a.append(4)
print(a) #[4]
print(x)  #None
y=a.append(60)
print(y) #None
print(a) #[4,60]
a.append(x)
print(a) #[4, 60, None]



x,y= 15,2
su= (x>>y)+(x<<y)
print(su) #63





