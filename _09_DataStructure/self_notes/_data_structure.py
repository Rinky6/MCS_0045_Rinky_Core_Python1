"""
					                         Data Structures
											---------------

-->Python has primitive (or basic) data structures or data types such as floats, integers, strings, and Booleans. Python also has non-primitive data structures such as lists, tuples, dictionaries, and sets. Non-primitive data structures store a collection of values in various formats rather than a single value. The string is referred as the both data type and data structure, the reason is the string can handle both single character and multiple characters. Some can hold data structures within the data structure.

# DATA TYPES
numbers  - individual values
boolean  - individual value
string   - group of values  'A'  '1'  '100'  '193.4'

# DATA STRUCTURES
string
List **
Tuple
Dictionary **
Set

Collections module : NamedTuple OrderedDict DefaultDict FrozenSet Counter

numbers:
-------
int
float
complex : 3i+4j

boolean:
-------
True
False

what is mutability:
-------------------
-->Mutability means that the data in the data structure can be modified (added, deleted, or changed) after creation. Mutability is an important factor to consider when choosing your data structure. If you know that you won’t need to change the internal state, consider using an immutable object to ensure that it is thread-safe and that nothing can overwrite your data.

Sequences:
----------
-->Sequences allow you to store multiple values in an organized and efficient fashion. There are several sequence types: strings, Unicode strings, lists, tuples, bytearrays, and range objects.
Dictionaries and sets are containers for non-sequential data.

There are certain things you can do with all sequence types.
These Sequence operations include
1.  indexing
2.	slicing
3.	adding
4.	multiplying and
5.	checking for membership.

In addition, Python has built-in functions for
6.	len()        : finding the length of a sequence
7.	max()      : for finding its largest element
8.	min()       : for finding its smallest elements.


Generic Functions:
------------------
-->A generic function is composed of multiple functions implementing the same operation for different types. Which implementation should be used during a call is determined by the dispatch algorithm. When the implementation is chosen based on the type of a single argument, this is known as single dispatch.

print()  :  Prints the given value
input()  :  Receives input from end user keyboard
type()   :  Gives type of variable/value
id()     :  Gives address of the variable/value

Type conversions
----------------
int()
float()
complex()
bool()
--------
str()
list()
tuple()
dict()
set()

-------------------------------------------------------------------------------------------------------------

												Integers
												--------

Integers:
---------
-->An integer is a whole number with no decimal places. For example, 1 is an integer, but 1.0 isn’t. The name for the integer data type is int, which you can see with type():

>>> type(1)
<class 'int'>

-->You can create an integer by typing the desired number. For instance, the following assigns the integer 25 to the variable num:

>>> num = 25

-->When you create an integer like this, the value 25 is called an integer literal because the integer is literally typed into the code.

-->You may already be familiar with how to convert a string containing an integer to a number using int(). For example, the following converts the string "25" to the integer 25:

>>> int("25")
25

-->int("25") is not an integer literal because the integer value is created from a string.

-->There’s no limit to how large an integer can be, which might be surprising considering that computers have a finite amount of memory. Try typing the largest number you can think of into IDLE’s interactive window. Python can handle it with no problem!

x = 10
print(x)   # f(x)
print("Value is :", x)

x = 10 + 20
# LHS = RHS


# Naming conventions
# variables always small letter

# REQ: Receive employee id and print it.

'''
Step 1: Receive employee id
Step 2: Print it
'''
     # Hard coding the value :: Static way
e_id = 4325  # emp_id empid eid e_id   st_rno strno prod_id
print("Employee id : ",e_id)

     # Receive the value dynamically
e_id = input("Enter your employee id :")
print("Employee id : ",e_id)

'''
f(x) = 2x + 1  # Mathematics

Python function
def f(x):
    val = 2x + 1
    print(val)
'''

print("--------------------type--------------")
print("Type of 10 :",type(10))
eid = 100
print("Employee details : ",eid, type(eid))

eid = input("Enter employee id :")
print("Employee details : ",eid, type(eid))

eid = int(input("Enter employee id :"))
print("Employee details : ",eid, type(eid))

e_sal = float(input("Enter employee salary :"))
print("Employee details : ",e_sal, type(e_sal))

eid = 100
print("Employee id and it address : ",eid, id(eid))
msg = 'Hello World'
print("Message is : ",msg, type(msg), id(msg))

-------------------------------------------------------------------------------------------------------------

												Float
												-----

Floating-Point Numbers:
-----------------------
A floating-point number, or float for short, is a number with a decimal place. 1.0 is a floating-point number, as is -2.75. The name of the floating-point data type is float:

>>> type(1.0)
<class 'float'>
Like integers, floats can be created from floating-point literals or by converting a string to a float with float():

>>> float("1.25")
1.25

>>> 1e6
1000000.0
The first two ways are similar to the two techniques for creating integer literals. The third approach uses E notation to create a float literal.

Note: E notation is short for exponential notation. You may have seen this notation used by calculators to represent numbers that are too big to fit on the screen.

To write a float literal in E notation, type a number followed by the letter e and then another number. Python takes the number to the left of the e and multiplies it by 10 raised to the power of the number after the e. So 1e6 is equivalent to 1×10⁶.

Python also uses E notation to display large floating-point numbers:

>>> 200000000000000000.0
2e+17
The float 200000000000000000.0 gets displayed as 2e+17. The + sign indicates that the exponent 17 is a positive number

-------------------------------------------------------------------------------------------------------------

												Boolean
												-------

-->The Python Boolean type is one of Python’s built-in data types. It’s used to represent the truth value of an expression. For example, the expression 1 <= 2 is True, while the expression 0 == 1 is False. Understanding how Python Boolean values behave is important to programming well in Python.

The Python Boolean type has only two possible values:
1)True
2)False

No other value will have bool as its type. You can check the type of True and False with the built-in type():

>>> type(False)
<class 'bool'>
>>> type(True)
<class 'bool'>

boolean data type note by madhu:
--------------------------------
is_active = True
print("Are you active ??",is_active, type(is_active))

x = 0
print(x, type(x))
x = bool(0)
print(x, type(x))


x = None
print(x, type(x))
x= False
print(x, type(x))

'''
if False -->  False
if None  -->  False
if 0     -->  False

if True    --> True
if not None -> True
if -5   -->  True
'''

-------------------------------------------------------------------------------------------------------------

											Type conversion
											----------------

Type conversions : Python defines type conversion functions to directly convert one data type to another type.
----------------
int()
float()
complex()
bool()
--------
str()
list()
tuple()
dict()
set()

-->There are 2 types of the conversions
1)Implicit conversion
2)Explicit conversion

Implicit convesion:
-------------------
-->In Implicit type conversion of data types in Python, the Python interpreter automatically converts one data type to another without any user involvement. To get a more clear view of the topic see the below examples.


Example:
--------
x = 10

print("x is of type:",type(x))

y = 10.6
print("y is of type:",type(y))

x = x + y

print(x)
print("x is of type:",type(x))

Output:
-------
x is of type: <class 'int'>
y is of type: <class 'float'>
20.6
x is of type: <class 'float'>

-->As we can see the type of ‘x’ got automatically changed to the “float” type from the “integer” type. this is a simple case of Implicit type conversion in python.

Explicit conversion:
--------------------
-->In Explicit Type Conversion in Python, the data type is manually changed by the user as per their requirement. Various forms of explicit type conversion are explained below:

# initializing string
s = "10010"

# printing string converting to int base 2
c = int(s,2)
print ("After converting to integer base 2 : ", end="")
print (c)

# printing string converting to float
e = float(s)
print ("After converting to float : ", end="")
print (e)

Output:
-------
After converting to integer base 2 : 18
After converting to float : 10010.0



"""