"""
Conversion from one data type to another data type is called type conversion.

There are two type of data type --
1. implicite  type  conversion
2. explicite type conversion



1. implicite  type  conversion - in this conversion no need to user involment

"""
x= 10
print("type of x " , type(x))

y = 10.1
print("type of y " , type(y))


x = x+y
print("type of x : ", type(x))


#type of x  <class 'int'>
#type of y  <class 'float'>
#type of x :  <class 'float'>


#In explicite conversion the user need to involve according to the requirement

x = 10
print(type(x))

# If we want to convert from interger data type to float we need to use the float()


print(type(float(x)))



s = "10011011"

print(type(s))

s1 = int(s,8)
print("octa "  , s1)

ss = int(s,2)
print(ss,type(ss))



#Convert from deci to binary
a = 20
lst = []
while a >0:
  n = int(a % 2)
  lst.append(n)
  a = int(a/2)
  #print(a)

b = reversed(lst)

for i in b:
    print(i,end = "")

print("\n ---------Fabonicci---------------")
a= 0
b=1
n = 8
for i in range(n):
    print(a)
    a,b = b , a+b




"""

type conversion functions:
--------------------------
1)int(a, base): This function converts any data type to integer. ‘Base’ specifies the base in which string is if the data type is a string.

2)float(): This function is used to convert any data type to a floating-point number.

3)ord() : This function is used to convert a character to integer.

4)hex() : This function is to convert integer to hexadecimal string.

5)oct() : This function is to convert integer to octal string.

6) tuple() : This function is used to convert to a tuple.

7) set() : This function returns the type after converting to set.

8) list() : This function is used to convert any data type to a list type.

9) dict() : This function is used to convert a tuple of order (key,value) into a dictionary.

10) str() : Used to convert integer into a string.

11) complex(real,imag) : This function converts real numbers to complex(real,imag) number.

12) chr(number): This function converts number to its corresponding ASCII character. 


"""

print(ord('A'))  #65


"""
Indexing  = reffering the element of iterable by its position within the element: In indexing ww can use the
+ve or -ve no both .
Slicing - It is use for get the subset of element or portion of the element from a iterable based onits indeces
to access the range of the string we need to use method.Slicing in string done using the slice operator(:)

"""

s = "Hello world"
print(s[2]) # l
print(s[-1]) #d


"""
Slicing behavior is diff based on the mutableand immutable DS
"""
a = "Rinky"
print(a[:])   #Rinky
print(a is a[:])  #True

lst = [1,5,8,9]
print(lst[:])   #[1, 5, 8, 9]
print(lst is lst[:]) #False




tpl = (5,9,6)
print(id(tpl))
print(id(tpl[:]))   #(5, 9, 6)
print(id(tpl is tpl[:]))#True

"""
In Immutable the slicing doesn't copy the element its return the same address and the element
but in mutable the slicing  copy it and return so both address are different.  
"""

#if the string has 3 consecutive numbers, print the their position.

st = "Hello542world475rin452"

for i in range(len(st)):
    s = st[i:i+3]
    #print(i, ' : ', s)
    if s.isdigit() and len(s) == 3:
        print("position of ",i , s)



















