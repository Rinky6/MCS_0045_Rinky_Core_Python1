## Find the value of X2+2x+1 when x is 10

x=10
result=x**2+2*x+1
print("After calculation   : ",result )


''''
Req:   Enter rate of employee check rating if rating 5 print good employee
       if rating between 3 and equal and less than 5 print average employee
       if rating less than 3 and greater than 2 print poor employee
       if rating less than 2 print very poor employee

'''
print("------------Nested If-----------")
# state

for i in range(1,3):
 rate=int(input("Enter rating of employee"))
 #Behavior
 if rate == 5:
    print("good employee")
 if  3<=rate <5:
    print("Average Employee")
 if 2<=rate<3:
    print("poor employee")
 if rate<2:
    print("We can terminate")






print("------------If elif-----------")
# state

for i in range(1,3):
 rate=int(input("Enter rating of employee"))
 #Behavior
 if rate == 5:
    print("good employee")
 elif 3<=rate <5:
    print("Average Employee")
 elif 2<=rate<3:
    print("poor employee")
 elif rate<2:
    print("We can terminate")




print("------------If elif else-----------")
# state

for i in range(1,3):
 rate=int(input("Enter rating of employee"))
 #Behavior
 if rate == 5:
    print("good employee")
 elif 3<=rate <5:
    print("Average Employee")
 elif 2<=rate<3:
    print("poor employee")
 elif rate<2:
    print("We can terminate")
 else:
     print("rating isnt given yet")