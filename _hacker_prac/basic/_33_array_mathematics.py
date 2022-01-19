"""
Task
You are given two integer arrays, A and B of dimensions N X M.
Your task is to perform the following operations:

Add (A + B)
Subtract (A – B)
Multiply (A * B)
Integer Division (A / B)
Mod (A % B)
Power (A ** B)
Note
There is a method numpy.floor_divide() that works like numpy.divide() except it performs
 a floor division.

Input Format
The first line contains two space separated integers, N and M.
The next N lines contains M space separated integers of array .
The following N lines contains M space separated integers of array B.

Output Format
Print the result of each operation in the given order under Task.

Sample Input

1 4
1 2 3 4
5 6 7 8
Sample Output

[[ 6  8 10 12]]
[[-4 -4 -4 -4]]
[[ 5 12 21 32]]
[[0 0 0 0]]
[[1 2 3 4]]
[[    1    64  2187 65536]]



"""





import numpy as np
a1 = int(input("Enter the 1st array element : "))

lst1 = []
lst2=[]
for i in range(1,a1) :
    lst1.append(i)

c = np.array(lst1)

for i in range(a1,9) :
    lst2.append(i)

d = np.array(lst2)

print(np.add(c,d))
print(np.subtract(c,d))
print(np.multiply(c,d))
print(np.floor_divide(c,d))
print(np.mod(c,d))
print(np.power(c,d))
