"""
The map() function applies a given function to each item of an iterable (list, tuple etc.)
and returns an iterator.
syntax
======

map(fun,iterator1 ,iterator2.....)



map() Parameter
The map() function takes two parameters:

function - a function that perform some action to each element of an iterable
iterable - an iterable like sets, lists, tuples, etc
You can pass more than one iterable to the map() function.



map() Return Value
The map() function returns an object of map class. The returned value can be passed to functions like

list() - to convert to list
set() - to convert to a set, and so on.



"""
num = [4,5,3,2,7]
def sqr(num):
    return num * num

sr=map(sqr,num)
print(list(sr))



numbers = (1, 2, 3, 4)
result = map(lambda x: x*x, numbers)
print(result)

numbersSquare = set(result)
print(numbersSquare)


num1 = [4, 5, 6]
num2 = [5, 6, 7]

result = map(lambda n1, n2: n1+n2, num1, num2)
print(list(result))



