#Identity Operators:
"""is and is not are the identity operators both are used to check if two values are located
on the same part of the memory. Two variables that are equal do not imply that they
are identical."""

"""is True if the operands are identical"""


"""a = 10
b = 20
c = a
print(a is not b)
print(a is c)"""


"""
R = "Seeta"
r = "Seeta"
m = r
m = R
print( r is  m)       #true
print( R is not m)    #false
"""

"""
R = "Seeta"
r = "Seeta"
m = r
m = R
print( r is not  m)     #false
print( R is not m)      #false
"""
"""
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)

# returns True because z is the same object as x

print(x is y)

# returns False because x is not the same object as y, even if they have the same content

print(x == y)

# to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y

"""