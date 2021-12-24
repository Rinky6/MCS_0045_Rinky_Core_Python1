"""
List comprehension offers a shorter syntax when you want to create a new list based on the values
of an existing list.

The Syntax
newlist = [expression for item in iterable if condition == True]


Advantages of List Comprehension
More time-efficient and space-efficient than loops.
Require fewer lines of code.
Transforms iterative statement into a formula.


"""

lst1 = ["apple", "banana", "cherry", "kiwi", "mango"]
lst2 = []

for i in lst1:
        if 'a' in i:
            lst2.append(i)
print("list : ", lst2)  #['apple', 'banana', 'mango']



# using list - comp

lst2 = [i.upper() for i in lst1 ]
print("list2 : ", lst2 )   #list2 :  ['APPLE', 'BANANA', 'CHERRY', 'KIWI', 'MANGO']




#touple



tpl1 = ("apple", "banana", "cherry", "kiwi", "mango")
tpl2 = (i for i in tpl1 if 'a' in i)
print("tuple : ", tpl2)  #tuple :  <generator object <genexpr> at 0x000001FAF8C06340>
for i in tpl2:
    print("print...", i)

'''
print... apple
print... banana
print... mango
'''

lst1 = [i +'k' for i in "Who are you"  ]
print(lst1)


import time

def for_loop(n):
    result = []
    for i in range(n):
        result.append(i ** 2)
    return  result

def list_comp(n):
    return[i**2 for i in range(n)]

begin= time.time()
for_loop(10**6)
end = time.time()

print('Time taken for_loop:',round(end-begin,2))

begin = time.time()
list_comp(10 ** 6)
end = time.time()

print('Time taken for list_comprehension:', round(end-begin,2))



matrix= []
for i in range(3) :
    matrix.append([])

    for j in range(5):
        matrix[i].append(j)
print("After iteration : " ,matrix)


#using list

matrix =[[i for i in range(5)] for j in range(3)]
print("using list comp :", matrix)



fruits = ["apple",  "cherry", "kiwi", "mango"]

newlist = [x if x == "mango" else "orange" for x in fruits]

print(newlist)



fruits = ["apple",  "cherry", "kiwi", "mango"]

newlist = [x if x != "mango" else "orange" for x in fruits]

print(newlist)




numbers = [i * 10 for i in range(1, 6)]

print(numbers)



# using lambda to print table of 10
numbers = list(map(lambda i: i * 10, [i for i in range(1, 6)]))

print(numbers)

# Assign matrix
twoDMatrix = [[10, 20, 30],
              [40, 50, 60],
              [70, 80, 90]]

# Generate transpose
trans = [[i[j] for i in twoDMatrix] for j in range(len(twoDMatrix))]

print(trans)

# Initializing string
string = 'Rinky Kumari'

# Toggle case of each character
List = list(map(lambda i: chr(ord(i) ^ 32), string))

# Display list
print(List)



List = [string[::-1] for string in ('This', 'is', 'for', 'you')]

# Display list
print(List)

# Getting square of even numbers from 1 to 10
squares = [n ** 2 for n in range(1, 11) if n % 2 == 0]

# Display square of even numbers
print(squares)




# Display the sum of digits of all the odd elements in a list.


def digitSum(n):
    dsum = 0
    for ele in str(n):
        dsum += int(ele)
    return dsum


# Initializing list
List = [367, 111, 562, 945, 6726, 873]

# Using the function on odd elements of the list
newList = [digitSum(i) for i in List if i & 1]

# Displaying new list
print(newList)



'''
Key Points
Comprehension of the list is an effective means of describing and constructing lists based on
 current lists.
Generally, list comprehension is more lightweight and simpler than standard list formation
 functions and loops.
We should not write long codes for list comprehensions in order to ensure user-friendly code.
Every comprehension of the list can be rewritten in for loop, but in the context of list
 interpretation, every for loop can not be rewritten.

'''