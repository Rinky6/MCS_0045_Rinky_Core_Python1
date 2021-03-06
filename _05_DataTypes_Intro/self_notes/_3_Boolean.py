
# Boolean DataType
"""
Booleans represent one of two values: True or False.
Boolean Values

WE can evaluate any expression in Python, and get one of two answers, True or False.
When we compare two values, the expression is evaluated and Python returns the Boolean answer:
print(10 > 9)   #True
print(10 == 9)  #False
print(10 < 9)   #false

When we run a condition in an if statement, Python returns True or False:
a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

  *******Evaluate Values and Variables**********

The bool() function allows we to evaluate any value, and give us True or False in return,
1. Evaluate string and no

print(bool("Hello"))     # True
print(bool(15))          # True

2. Evaluate two variables:

x = "Hello"
y = 15

print(bool(x))
print(bool(y))
Most Values are True

****************Almost any value is evaluated to True if it has some sort of content.****************

Any string is True, except empty strings.

Any number is True, except 0.

Any list, tuple, set, and dictionary are True, except empty ones.

Example
The following will return True:

bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])

Some Values are False
In fact, there are not many values that evaluate to False, except empty values, such as (), [], {}, "", the number 0, and the value None. And of course the value False evaluates to False.

Example
The following will return False:

bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

One more value, or object in this case, evaluates to False, and that is if you have an object that is made from a class with a __len__ function that returns 0 or False:

Example
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

Python also has many built-in functions that return a boolean value, like the isinstance() function, which can be used to determine if an object is of a certain data type:

Example
Check if an object is an integer or not:

x = 200
print(isinstance(x, int))








"""
