'''
 Mailing Address
Create a program that displays your name and complete mailing address formatted in the manner that
you would usually see it on the outside of an envelope. Your program does not need to read any input
from the user.






'''
name = "Rinky Kumari"
hs_no= 201
building_no='building no - T2'
cross ='3 Cross'
dst='Gumla'
state='Jharkhand'
print(name)
print(hs_no , building_no)
print(cross)
print(dst  , state)

name = input("Enter your name")
hs_no= int(input("Enter your house no"))
building_no=input("Enter your building  no")
cross = input("Enter your cross name")
dst=input("Enter your dist name")
state=input("Enter your state name")
print(name)
print(hs_no , building_no)
print(cross)
print(dst  , state)

'''
Exercise 2: Hello
Write a program that asks the user to enter his or her name. The program should respond with a 
message that says hello to the user, using his or her name


'''

name = input("Enter your name")
print("Hello", name)



def call (n):
 print("Hello", n)

name = input("Enter your name")
call(name)

'''

Exercise 3: Area of a Room
Write a program that asks the user to enter the width and length of a room. Once the values have 
been read, your program should compute and display the area of the room. The length and the width 
will be entered as floating point numbers. Include units in your prompt and output message; either 
feet or meters, depending on which unit you are more comfortable working with.

'''

height = float(input("Enter height of room"))
width = float(input("Enter width of room"))
area = height * width
print("Area of room = ", area, "meter")



def rarea(lg,wd):
 a = lg * wd
 area = round(a, 2)
 print("The area of the room is ", area, " square feet")
l = float(input("Enter height of room"))
w = float(input("Enter width of room"))
rarea(l,w)


''''

Exercise 4: Area of a Field
Create a program that reads the length and width of a farmer’s field from the user in feet.
Display the area of the field in acres.

'''
length = float(input("Enter length of field"))
width = float(input("Enter width of field"))
a = length * width / 43560

area = round(a, 2)
print("The area of the field is ", area, " acres")



def afield(l,w):
 a = l * w / 43560
 area = round(a, 2)
 print("The area of the field is ", area, " acres")

length = float(input("Enter length of field"))
width = float(input("Enter width of field"))
afield(length,width)
'''
Exercise 5: Bottle Deposits
In many jurisdictions a small deposit is added to drink containers to encourage people to recycle 
them. In one particular jurisdiction, drink containers holding one liter or less have a $0.10 deposit,
and drink containers holding more than one liter have a
$0.25 deposit.Write a program that reads the number of containers of each size from the user. Your
program should continue by computing and displaying the refund that will be received for returning
those containers. Format the output so that it includes a dollar sign and always displays exactly 
two decimal places.


'''
numc = int(input("Enter no of container"))
numc1 = int(input("Enter no of container"))
refund=0
refund1=0
if numc<=1:
 rfd=numc*0.10
 refund=round(rfd,2)
 print("The refund that will be received for one litter or less  containers $", refund )
else:
 refund1=numc1*0.25
 print("The refund that will be received for more than one litter  containers  $", refund1)

total_refund=refund+refund1
print("The total refund of the bottles is $" ,total_refund)



ls = 0.10
mr = 0.25
less_cntnrs = int(input("How many less containers did you recycle?"))
more_cntnrs = int(input("How many more containers did you recycle?"))

total_refund = ls * less_cntnrs + mr * more_cntnrs
print("The total refund of the bottles is $" ,total_refund)





'''
Exercise 6: Tax and Tip
The program that you create for this exercise will begin by reading the cost of a meal ordered at a
restaurant from the user. Then your program will compute the tax and tip for the meal. Use your local
tax rate when computing the amount of tax owing. Compute the tip as 18 percent of the meal amount
(without the tax). The output from your program should include the tax amount, the tip amount, and the
grand total for the meal including both the tax and the tip. Format the output so that all of the values 
are displayed using two decimal places.

'''
meal_cost = float(input("Enter cost of the meal"))
meal_tip = meal_cost * 18 / 100
meal_tax = meal_cost * 4/ 100
tmcost = meal_cost + (meal_tip + meal_tax)
total_meal_cost = round(tmcost, 2)

print("The grand total for the meal including both the tax and the tip : ", total_meal_cost)


def order(m_cost):
 meal_tip = m_cost * 18 / 100
 meal_tax = m_cost * 4 / 100
 tmcost = meal_cost + (meal_tip + meal_tax)
 total_meal_cost = round(tmcost, 2)
 print("The grand total for the meal including both the tax and the tip : ", total_meal_cost)


meal_cost = float(input("Enter cost of the meal"))
order(meal_cost)

'''

Exercise 7: Sum of the First n Positive Integers
(Solved—12 Lines) Write a program that reads a positive integer, n, from the user and then displays
 the sum of all of the integers from 1 to n. The sum of the first n positive integers can be computed 
 using the formula:
sum = (n)(n + 1)/2

'''

n = int(input("Input an integer: "))
result = sum(range(n + 1))
print("Sum of the first", n, "positive integers:", result)

num = int(input("Input a number: "))
sum = (num * (num + 1)) / 2
print("Sum of the first", n, "positive integers:", sum)

'''
Exercise 8: Widgets and Gizmos
An online retailer sells two products: widgets and gizmos. Each widget weighs 75 grams. Each gizmo 
weighs 112 grams. Write a program that reads the number of widgets and the number of gizmos in an 
order from the user. Then your program should compute and display the total weight of the order.


'''

noOfWidgets = int(input ("Enter  number of widgets: "))
noofGizmos = int(input("Enter number of Gizmos: "))
weightOfWidgets = noOfWidgets * 75
weightOfGizmos = noofGizmos * 112
total_weight = weightOfGizmos + weightOfWidgets
print ("The total weight of the order is " , total_weight )


def retailer_sell(n_of_wd,n_of_giz):
 weight_of_widgets = n_of_wd * 75
 weight_of_gizmos = n_of_giz * 112
 total_weight = weight_of_widgets + weight_of_gizmos
 print("The total weight of the order is ", total_weight)
no_of_widgets = int(input ("Enter  number of widgets: "))
no_of_gizmos = int(input("Enter number of Gizmos: "))
retailer_sell(no_of_widgets,no_of_gizmos)




'''

Exercise 9: Compound Interest
Pretend that you have just opened a new savings account that earns 4 percent interest per year.
The interest that you earn is paid at the end of the year, and is added to the balance of the savings 
account. Write a program that begins by reading the amount of money deposited into the account 
from the user. Then your program should compute and display the amount in the savings account after
 1, 2, and 3 years. Display each amount so that it is rounded to 2 decimal places.

'''
amt = float(input("Enter Amount"))
r = 0.04

for  i in range(1,4):
  total_amt = amt+amt*0.04
  total_amt1 = amt+total_amt *0.04
  total_amt2 = amt+total_amt1*0.04
print("Total amount in account after adding interest after 1 year ", round(total_amt, 2))
print("Total amount in account after adding interest after 2 years ", round(total_amt1, 2))
print("Total amount in account after adding interest after 3 years ", round(total_amt2, 2))



amt = float(input("Enter Amount"))
r = 0.04
yr=[1,2,3]

for  i in yr:
  total_amt = amt+amt*0.04
  total_amt1 = amt+total_amt *0.04
  total_amt2 = amt+total_amt1*0.04
print("Total amount in account after adding interest after 1 year ", round(total_amt, 2))
print("Total amount in account after adding interest after 2 years ", round(total_amt1, 2))
print("Total amount in account after adding interest after 3 years ", round(total_amt2, 2))





'''
Exercise 10: Arithmetic
Create a program that reads two integers, a and b, from the user. Your program should compute and display:

•	The sum of a and b
•	The difference when b is subtracted from a
•	The product of a and b
•	The quotient when a is divided by b
•	The remainder when a is divided by b
•	The result of log10 a
•	The result of ab


'''
import math

a = int(input("Enter value of a"))
b = int(input("Enter value of b"))
sum = a + b
print("The sum of a and b = ", sum)
sub = a - b
print("The subtraction of a and b = ", sub)
product = a * b
print("The product of a and b = ", product)
qu = a / b
print("The quotient when a is divided by b = ", qu)
rm = a % b
print("The remainde when a is divided by b = ", rm)

rslt = math.log10((a))
print("The result of log10 a = ", rslt)

result = a ** b
print("The result of ab= ", result)
