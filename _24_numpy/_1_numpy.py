"""
												numpy by jake vanderplas
												------------------------
why numpy is fast like c, fortran:
----------------------------------
The way numpy does this is it recognizes the things that are slow and when you are looping over
the small operations and building up the little overhead because of the repeated operations in
python. So it takes those looped operations and pushes them into the compiled code, so that they
can be done quickly. Basically in the compiled code the type checking happens only one
time for the entire loop of one million repetitions.

four strategies to speeding up the code with numpy:
---------------------------------------------------
1)use numpy's universal functions(ufuncs)
2)use numpy's aggregations
3)use numpy's broadcasting
4)use numpy's slicing, masking, fancy indexing.

1)ufuncs:
---------
the universal function are the special type of the functions, that they operate element
wise on arrays.
element wise operation with python lists:
a = [1,2,3,4,5]
result = [val + 5 for val in a]
print(r  esult)
output : [6,7,8,9,10]

element wise operation with numpy arrays:
import numpy as np
a = np.array([1,2,3,4,5])
result = a + 5
print(result)
output : [6,7,8,9,10]

-->here you can just treat the array a as the number, and a + b,
here the numpy overloads that "+" operator and actually produces the result element
wise. if you add 5 to the array , it means you are adding 5 to the every value of the array.
the ufuncs in numpy are
arithmetic operators : + , - , *, / , // %, **
bitwise operators: &, |, ~, ^, >>, <<
comparison operator: <, >, <=, >=, ==, !=
Trig family:np.sin, np.cos, np.tan etc
exponential family:np.exp, np.log, np.log10
special function: scipy.special.*

2)Aggregations:
---------------
the aggregations are the functions which summarize the values in an array
 e.g min, max, sum, mean, etc. Numpy aggegations are much faster than python built-ins. Let's compare

python's min() function:
from random import random
c = [random() for i in range(10000)]
print(min(c)) #we can't write like c.min(). list object has no attribute min().

numpy's min() function:
import numpy as np
c = np.array([random() for i in range(10000)])
print(np.min(c)) #we can also write c.min().

-->Here in the first program the python's min() function goes to the every element in
the list and asks what is the type of that value, the again compare that type to the
current minimum value, then compare to the type of the next minimum value, it takes
 lot of time and it is a complex operation.

-->Another advantage of the numpy aggregations is these methods also work on the multi
 dimensional arrays.
import numpy as np
m = np.random.randint(0,10, (3,5))
array([[2,9,2,1,3],
			2,1,5,2,4],
			8,9,1,3,5]])
m.sum(axis = 0)
array([12,19,8,6,12])

m.sum(axis = 1)
array([17,14,26])

-->here sum(axis = 0) means sum of all the columns. sum(axis = 1) means sum of all the rows.
 The randint() method only produces the integers value like 1, 2,3 etc. not the decimal numbers.

3)Broadcasting:
----------------
it is set of rules by which ufuncs operate on arrays of different sizes and dimensions.
rules:
------
1)If array shapes differs, left-pad the smaller shape with 1's.
2)If any dimension does not match, broadcast the dimension with size = 1
3)if neither non-matching dimension is 1, raise an error.
example:
--------
import numpy as np
lista = [[1,2,3],[2,3,4],[3,4,5]]
listb = [1,0,2]
A = np.array(lista, dtype = np.int32)
B = np.array(listb , dtype = np.int32)
print(A.shape) #prints(3,3)
print(B.shape) #prints(3,)

-->numpy allows us to do the mathematical operations using the arrays with the different shapes.
 This is called broadcasting.
print(A + B)
this gives the result [[2 2 5]
						[3 3 6]
						[4 4 7]]
-->Here each of the row in the A is increased by B. what happens in the background is the
numpy takes the array B = [1, 0, 2] and increase this into the same number of dimensions that
A is which means B = [[1,0,2],[1,0,2], [1,0,2]]
this is all done by the numpy internally making the scripts little bit more efficient and make
the process the very faster. there are certain rules to follow while doing the broadcasting.
It must be either of the same number of the dimensions as the other, or dimension of 1.
If one array is smaller than the other, that means that it has to have the dimension of 1.
So whenever this happens we just repeat the dimension to the same number of the dimension as
the the other. Because the broadcasting is allowed when all dimensions are compatible.
After we do the broadcasting each of the 2 arrays are treated as just like they are of same shape.

"""