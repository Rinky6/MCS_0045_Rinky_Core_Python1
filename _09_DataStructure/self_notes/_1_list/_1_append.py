"""a=[1,5,8,4,3]

b=a.append(5)
print(b) #None
print(a.append(5)) #None

print(a) #[1, 5, 8, 4, 3, 5, 5]

import collections
from array import *
arr_lst = array('H', [4,5,2,8,7])   #ValueError: bad typecode (must be b, B, u, h, H, i, I, l, L, q, Q, f or d)
i = 0
print(len(arr_lst)) #5
n = len(arr_lst)
print(arr_lst)  #array('H', [4, 5, 2, 8, 7])
while i < n:
    print(arr_lst[i], end = "") #45287
    i+=1
print("\n after append in array")
arr_lst.append(9)
arr_lst.append(5)
arr_lst.append(5)
arr_lst.append(8)
print(arr_lst)   #array('H', [4, 5, 2, 8, 7, 9])
print(collections.Counter(arr_lst))  #Counter({5: 3, 8: 2, 4: 1, 2: 1, 7: 1, 9: 1})
i=0
while i < len(arr_lst):
    print((str(arr_lst[i]) + " "), end = "") #4 5 2 8 7 9 5 5 8
    i+=1
"""
print("\n ----------------------------")
a= [4,5,6]
a.append(8)
print(a.append(5)) #None
print(a)
b=[5,6,8]
a.append(b)
print(a)  #[4, 5, 6, 8, 5, [5, 6, 8]]


a.extend([5,9,8])
print(a)


#insert(): Inserts an elements at specified position.
a.insert(2,9)
print(a)




