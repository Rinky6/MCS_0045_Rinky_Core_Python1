
# Python Numbers
"""
There are three numeric types in Python:
1. int
2. float
3. complex
Variables of numeric types are created when you assign a value to them.

Integers – This value is represented by int class. It contains positive or negative
whole numbers (without fraction or decimal). In Python there is no limit to how
long an integer value can be.

Float – This value is represented by float class. It is a real number with floating
point representation. It is specified by a decimal point. Optionally, the character e or
E followed by a positive or negative integer may be appended to specify scientific
notation.
Float can also be scientific numbers with an "e" to indicate the power of 10.
x = 35e3      #35000.0
y = 12E4      #120000.0
z = -87.7e100 #-8.77e+101

print(x)
print(y)
print(z)

Complex Numbers – Complex number is represented by complex class. It is
specified as (real part) + (imaginary part)j. For example – 2+3j

Example
x = 1    # int
y = 2.8  # float
z = 1j   # complex

*********To verify the type of any object in Python, use the type() function:**********

Example
print(type(x))
print(type(y))
print(type(z))



Type Conversion
================
We can convert from one type to another with the int(), float(), and complex() methods:
x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

"""