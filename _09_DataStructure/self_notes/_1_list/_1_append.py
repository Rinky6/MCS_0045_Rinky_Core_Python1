"""
a = [1,5,2,9]
b=[]
c = b.append([8])
print(c)
print(b.append([8]))






a=[1,5,8,4,3]

b=a.append(5)
print(b) #None
print(a.append(5)) #None

print(a) #[1, 5, 8, 4, 3, 5, 5]

import collections
from array import *
arr_lst = array('m', [4,5,2,8,7])   #ValueError: bad typecode (must be b, B, u, h, H, i, I, l, L, q, Q, f or d)
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

"""
"""
The methods of comparing two lists are given below.

The cmp() function
The set() function and == operator
The sort() function and == operator
The collection.counter() function
The reduce() and map() function
The cmp() function


The cmp() function -->
==================

The Python cmp() function compares the two Python objects and returns the integer 
values -1, 0, 1 according to the comparison.

Note - It doesn't use in Python 3.x version.

list1, list2 = [123, 'xyz'], [456, 'abc']
print(cmp(list1, list2))
print (cmp(list2, list1))
list3 = list2 + [786];
print (cmp(list2, list3))

"""




"""
The set() function and == operator
==================================
set()function manupulate the list  without taking care the order of the element
we use the == operator for the compare the this two set
"""
list1 = [11, 12, 13, 14, 15]
list2 = [12, 13, 11, 15, 14]


s1 = set(list1)
s =set(list2)
print(s,s1)   #{11, 12, 13, 14, 15} {10, 11, 12, 13, 14, 15}


print(set(list1) == set(list2))  #True



"""
The sort() method with == operator
Python sort() function is used to sort the lists. The same list's elements are the same index position it means; lists are equal.

Note - In the sort() method, we can pass the list items in any order because we are sorting the list before comparison.
Let's understand the following example -


"""
import collections

list1 = [10, 20, 30, 40, 50, 60]
list2 = [10, 20, 30, 50, 40, 70]
list3 = [50, 10, 30, 20, 60, 40]

# Sorting the list
print(list1.sort())  #None
print(list2.sort() ) #None
list3.sort()


if list1 == list2:
    print("The list1 and list2 are the same")
else:
    print("The list1 and list3 are not the same")

if list1 == list3:
    print("The list1 and list2 are not the same")
else:
    print("The list1 and list2 are not the same")



"""


The collection.counter() function
The collection module provides the counter(), which compare the list efficiently. It stores the data in dictionary format <value>:<frequency> and counts the frequency of the list's items.

Note - The order of the list's elements doesn't matter in this function.
"""

import collections

list1 = [10, 20, 30, 40, 50, 60]
list2 = [10, 20, 30, 50, 40, 70]
list3 = [50, 10, 30, 20, 60, 40]


if collections.Counter(list1) == collections.Counter(list2):
    print("The lists l1 and l2 are the same")
else:
    print("The lists l1 and l2 are not the same")

if collections.Counter(list1) == collections.Counter(list3):
    print("The lists l1 and l3 are the same")
else:
    print("The lists l1 and l3 are not the same")










"""
The reduce() and map()
The map() function accepts a function and Python iterable object (list, tuple, string, etc) as an arguments and
 returns a map object. The function implements to each element of the list and returns an iterator as a result.

Besides, The reduce() method implements the given function to the iterable object recursively.

Here, we will use both methods in combination. The map() function would implement the function
 (it can be user-define or lambda function) to every iterable object and the reduce() function take
  care of that would apply in recursive manner.

Note - We need to import the functool module to use the reduce() function.

"""

import functools

list1 = [10, 20, 30, 40, 50]
list2 = [10, 20, 30, 50, 40, 60, 70]
list3 = [10, 20, 30, 40, 50]

if functools.reduce(lambda x, y: x and y, map(lambda a, b: a == b, list1, list2), True):
    print("The list1 and list2 are the same")
else:
    print("The list1 and list2 are not the same")

if functools.reduce(lambda x, y: x and y, map(lambda a, b: a == b, list1, list3), True):
    print("The list1 and list3 are the same")
else:
    print("The list1 and list3 are not the same")

