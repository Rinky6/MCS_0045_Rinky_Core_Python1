from collections import Counter
c = Counter()
list = [1,2,3,4,5,7,8,5,9,6,10]
print(Counter(list))
print(Counter({1:5,2:4}))
list = [1,2,4,7,5,1,6,7,6,9,1]
c = Counter(list)
print(c[1])


"""
Counter is a container included in the collections module. Now you all must be wondering
what is a container. Don’t worry first let’s discuss about the container.

A Counter is a subclass of dict. Therefore it is an unordered collection where elements
and their respective count are stored as a dictionary. This is equivalent to a bag or multiset
of other languages.






Why use Python Counter?
Here, are major reasons for using Python 3 Counter:

The Counter holds the data in an unordered collection, just like hashtable objects.
The elements here represent the keys and the count as values.
It allows you to count the items in an iterable list.
Arithmetic operations like addition, subtraction, intersection, and union can be
easily performed on a Counter.
A Counter can also count elements from another counter



Initialization :
The constructor of counter can be called in any one of the following ways :

With sequence of items
With dictionary containing keys and counts
With keyword arguments mapping string names to counts

"""

from collections import Counter

# With sequence of items
print(Counter(['B', 'B', 'A', 'B', 'C', 'A', 'B', 'B', 'A', 'C']))

# with dictionary
print(Counter({'A': 7, 'B': 9, 'C': 8}))

# with keyword arguments
print(Counter(A=3, B=5, C=2))



"""
we can create empty counter using following:

*****cout=collection.counter()


And can be updated via update() method .Syntax for the same :

coun.update(Data)

"""


from collections import Counter
cou = Counter()
print(cou)
cou.update((1,5,4,1,2,6,8,8,5,2,3,6,9,5,2,5,5,6,2,5,5,6))
print(Counter(cou))

cou.update((4,5,6,3))
print(cou)


co =Counter()
co.update("now I'm learning python")
print("Before update ", co)
print('g' , co['g'])
for char in 'python':
    print(char , co[char])




"""
Deleting an Element from Counter
"""

d =Counter([1,2,5,1,2,4,6,3,4,5,7,8,5,8,2,4,6,4,2])
print("Before the deleting element",d)
del d[5]
print("After deleting the element : ", Counter(d))











counter1 =  Counter({'x': 4, 'y': 2, 'z': -2})

counter2 = Counter({'x1': -12, 'y': 5, 'z':4 })

#Addition
counter3 = counter1 + counter2 # only the values that are positive will be returned.

print(counter3)

#Subtraction
counter4 = counter1 - counter2 # all -ve numbers are excluded.For example z will be z = -2-4=-6, since it is -ve value it is not shown in the output

print(counter4)

#Intersection
counter5 = counter1 & counter2 # it will give all common positive minimum values from counter1 and counter2

print("counter : ",counter5)

#Union
counter6 = counter1 | counter2 # it will give positive max values from counter1 and counter2

print(counter6)



"""
Methods Available on Python Counter
There are some important methods available with Counter, here is the list of same:
elements() : This method will return you all the elements with count >0. Elements with 
0 or -1 count will not be returned.
most_common(value): This method will return you the most common elements from Counter list.
subtract(): This method is used to deduct the elements from another Counter.
update(): This method is used to update the elements from another Counter.

"""
c=Counter({'X': 4,'Y': 0,'Z':6,'P':-6})
cc = c.elements()
print("---------- ",cc) #<itertools.chain object at 0x000001B551A5FF70>
for i in cc:
    print(i)


#most_common(value)


counter1 =  Counter({'x': 5, 'y': 12, 'z': -2, 'x1':0})

common_element = counter1.most_common(2) # The dictionary will be sorted as per the most common element first followed by next.
print(common_element)

common_element1 = counter1.most_common() # if the value is not given to most_common , it will sort the dictionary and give the most common elements from the start.The last element will be the least common element.
print(common_element1)


co = Counter({'name': 'ram',"sal":"20",'dept': "HR",'eid': "12"})
print(co)
co_c=co.most_common(3)
print(co_c)  #[('name', 'ram'), ('dept', 'HR'), ('sal', '20')]





#subtract()
counter1 =  Counter({'x': 5, 'y': 12, 'z': -2, 'x1':0})
counter2 = Counter({'x': 2, 'y':5})

counter1.subtract(counter2)
print(counter1)





