"""
sort(): Sorts the list in ascending order.
type(list): It returns the class type of an object.
append(): Adds one element to a list.
extend(): Adds multiple elements to a list.
index(): Returns the first appearance of a particular value.
max(list): It returns an item from the list with a max value.
min(list): It returns an item from the list with a min value.
len(list): It gives the overall length of the list.
clear(): Removes all the elements from the list.
insert(): Adds a component at the required position.
count(): Returns the number of elements with the required value.
pop(): Removes the element at the required position.
remove(): Removes the primary item with the desired value.
reverse(): Reverses the order of the list.
copy():  Returns a duplicate of the list.

"""
from collections import Counter

lst = [5,7,1,3,4,9,4]
lst.sort()
print(lst) #[1, 3, 4, 4, 5, 7, 9]
print(type(lst)) #<class 'list'>
print(lst.copy()) #[1, 3, 4, 4, 5, 7, 9]
#print(lst) #

lst.append(10)
print(lst.append(10)) #None

print(lst) #[1, 3, 4, 4, 5, 7, 9, 10, 10]



lst.extend([4,5,3])
print(lst.extend([4,5,3])) #None
print(lst) #[1, 3, 4, 4, 5, 7, 9, 10, 10, 4, 5, 3, 4, 5, 3]

lst.insert(2,74)
print(lst.insert(3,45))  #none
print(lst) #[1, 3, 74, 45, 4, 4, 5, 7, 9, 10, 10, 4, 5, 3, 4, 5, 3]


print(lst.pop()) # # 3delete last element of list
print(lst) #[1, 3, 74, 45, 4, 4, 5, 7, 9, 10, 10, 4, 5, 3, 4, 5]
print(lst.pop(3)) #15
print(lst)  #[1, 3, 74, 4, 4, 5, 7, 9, 10, 10, 4, 5, 3, 4, 5]
s = Counter(lst)
print(Counter(lst))
print(s)#Counter({4: 4, 5: 3, 3: 2, 10: 2, 1: 1, 74: 1, 7: 1, 9: 1})
print(lst.index(74)) #2
print(lst[2]) #74
print(lst.count(3)) #2


print(reversed(lst))  #<list_reverseiterator object at 0x0000023B6A4F7FD0>
for i in lst:
    print(i ,end = "") #137444579101045345

print("\n --------")
lst.reverse()
#print(lst.reverse()) #None
print(lst) #[5, 4, 3, 5, 4, 10, 10, 9, 7, 5, 4, 4, 74, 3, 1]





lst.remove(4)

print(lst) #[5, 3, 5, 4, 10, 10, 9, 7, 5, 4, 4, 74, 3, 1]
print(lst.remove(4)) #None
print(lst)  #[5, 3, 5, 10, 10, 9, 7, 5, 4, 4, 74, 3, 1]




print(lst.clear()) #None
lst.clear()
print(lst) #[]

#print(lst.index(4))  #4 is not in list

#print(lst[4]) #list index out of range

print("-----------------------------------------------------")
print(max(lst)) #74
print(min(lst)) #1
print(len(lst)) #17

