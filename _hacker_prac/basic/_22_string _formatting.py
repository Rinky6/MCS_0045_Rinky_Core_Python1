"""
Given an integer, n, print the following values for each integer i from 1 to n:

Decimal
Octal
Hexadecimal (capitalized)
Binary
The four values must be printed on a single line in the order specified above for each
i from 1 to n. Each value should be space-padded to match the width of the binary value of n.

"""
n = int(input("Enter a no : "))
for i in range(1,n+1):
    oc=oct(i)[2:]
    he=hex(i)[2:].upper()
    bi=bin(i)[2:]
    print(i ,   oc ,    he ,     bi)