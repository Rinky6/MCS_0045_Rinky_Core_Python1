"""
										join()
									   --------

-->The join() string method returns a string by joining all the elements of an iterable
(list, string, tuple), separated by a string separator.

Syntax : string.join(iterable)

Some of the example of iterables are:
-------------------------------------
Native data types - List, Tuple, String, Dictionary and Set.
File objects and objects you define with an __iter__() or __getitem()__ method.
Note: The join() method provides a flexible way to create strings from iterable objects.
It joins each element of an iterable (such as list, string, and tuple) by a string separator
(the string on which the join() method is called) and returns the concatenated string.

-->If we want make the string version of comma seperated values from our list. we use the
 method join().
join() method returns the value of str data type, split() method returns the value in the
 list format. The join() method takes only one argument either the single string value or the
 list of string.

example:
--------
sample = ['apple','mango','cherry']
sample1 = ' , '.join(sample)#this means all the elements will be joined by putting comma in
 between them
print(sample1)
new_sample = sample1.split(' , ') #this method removes the comma seperation and forms the new list.
print(new_sample)
output:
-------
apple , mango , cherry
['apple', 'mango', 'cherry']


example:
--------
list1 = [ 'hello', 'world', 'python']
result = '-'.join(list1)
print(result)
output:
-------
hello-world-python

-->here I mentioned the string seperator as '-'. it join all the elements in the list
by putting the '-' between them. we call '-' as the string seperator. in that single quotes,
we can mention any other characters or any symbols.


example : passing the other data types to the join return the error.
---------
list1 = [ 'hello', 'world', 'python', 1,2]
result = '-'.join(list1)
print(result)
output:
-------
Traceback (most recent call last):
  File "C:\Users\this\Desktop\sample1.py", line 2, in <module>
    result = '-'.join(list1)
TypeError: sequence item 3: expected str instance, int found


example: but we can give only tuple, but they should  contain the string data.
--------
list1 = [ 'hello', 'world', 'python', ('hello')]
result = '-'.join(list1)
print(result)
output:
-------
hello-world-python-hello


example: we can't the data type other than tuple()
--------
list1 = [ 'hello', 'world', 'python', ['list'], {'set'}, {'a' : 'apple'}]
result = '-'.join(list1)
print(result)
output:
-------
Traceback (most recent call last):
  File "C:\Users\this\Desktop\sample1.py", line 2, in <module>
    result = '-'.join(list1)
TypeError: sequence item 3: expected str instance, list found


example : .join() with tuples
---------
tuple = ('a', 'b', 'c')
result = '-'.join(tuple)
print(result)
output:
-------
a-b-c


example : in the string seperator ' ', we can give another string also
---------
string1  = 'abc'
list1 = ['1', '2', '3']
result = string1.join(list1)
print(result)
output:
-------
1abc2abc3


example : .join() with sets.
---------
set1 = {'a', 'b', 'c'}
result = '->'.join(set1)
print(result)
output:
-------
b->c->a
-->here the output, the alphabets are not in the order, because sets don't maintain the order


example : .join() with dictionaries
---------
dict1 = {'a' : 'apple' , 'b' : 'box'}
result = '-->'.join(dict1)
print(result)
output:
-------
a-->b

-->here by defualt keys are joined. we can also write ''.join(dict1.keys()). here keys are strings.
 if the keys are not string, it will be error.

example: ''.join(dict1.values())
--------
dict1 = {'a' : 'apple' , 'b' : 'box'}
result = '-->'.join(dict1.values())
print(result)
output:
-------
apple-->box


example: ''.join(dict1.items()) dont' work. because the items() return key, value in a tuple format.
--------
dict1 = {'a' : 'apple' , 'b' : 'box'}
result = '-->'.join(dict1.items())
print(result)
output:
-------
Traceback (most recent call last):
  File "C:\Users\this\Desktop\sample1.py", line 2, in <module>
    result = '-->'.join(dict1.items())
TypeError: sequence item 0: expected str instance, tuple found


-------------------------------------------------------------------------------------------------------------


					replace()
				     ---------

-->The replace() method replaces each matching occurrence of the old character/text in the
string with the new character/text.

Syntax : str.replace(old, new [, count])
old - old substring you want to replace
new - new substring which will replace the old substring
count (optional) - the number of times you want to replace the old substring with the new substring
Note: If count is not specified, the replace() method replaces all occurrences of the old substring
with the new substring.

-->The replace() method returns a copy of the string where the old substring is replaced with
 the new substring. The original string is unchanged. If the old substring is not found,
 it returns the copy of the original string.

example:
--------
string = 'python program'
print(string.replace('p', 'P'))
output:
-------
Python Program

-->if I want to replace only first 'p'. then use the count.
example:
--------
string = 'python program'
print(string.replace('p', 'P', 1))
output:
-------
Python program


example: it there is empty string, it returns the empty line.
--------
string = ''
print(string.replace('p', 'P', 1))



-------------------------------------------------------------------------------------------------------------


																						split()
																						-------

-->The split() method breaks up a string at the specified separator and returns a list of strings.
be default it splits by space ' '.

Syntax : str.split(separator, maxsplit)

separator (optional)- Delimiter at which splits occur. If not provided, the string is splitted
at whitespaces.
maxsplit (optional) - Maximum number of splits. If not provided, there is no limit on the number
 of splits.

Note : The split() method returns a list of strings.

example: by default it splits based on space ' '.
--------
string = 'this is python program'
print(string.split())
output:
-------
['this', 'is', 'python', 'program']

example:
--------
string = 'this is python program'
print(string.split(' ', 2))
output:
--------
['this', 'is', 'python program']
-->here i mentioned the max split is 2. so it stops splitting after 2 splits.


example : we can use the string seperator any character
---------
string = 'this is python program'
print(string.split('i', 2))
output:
-------
['th', 's ', 's python program']


example: it the seperator string is not found, it returns the entire string as the list element.
--------
string = 'this is python program'
print(string.split('z', 2))
output:
-------
['this is python program']"""