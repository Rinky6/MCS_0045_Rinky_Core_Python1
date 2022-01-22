"""
reshape - reshape the array without changing its data.


numpy.reshape(array,shape,order)
by default order value is "C"
we can give the order as
C - row wise
A - fortern like
F - column wise

return : - returns ndarray with mentioned shape.
return ndarray element may be copy of original element or view of original element





"""
import numpy as np

n = np.arange(10)
print(n)  #[0 1 2 3 4 5 6 7 8 9]
print(n.shape) #(10,)

#here shape(no of the array) printing 10 because array is 1 dimentional
#we can change the shape of array using reshape

print(np.reshape(n,(5,2)))
"""
[[0 1]
 [2 3]
 [4 5]
 [6 7]
 [8 9]]
"""
print(np.reshape(n,(5,2) , order="F"))

"""
[[0 5]
 [1 6]
 [2 7]
 [3 8]
 [4 9]]

"""
print(np.reshape(n,(5,2) , order="A"))

# here I didnt mention the order so it is take by default c type order

#print(np.reshape(n,(3,2)))

"""
here we cant reshape the element because in array 10 element is there so we cant arrange in 3x2 dimentional 
of 10 elements   

because reshape wont change data of the array
cannot reshape array of size 10 into shape (3,2)

"""


ele = np.arange(9)
print(np.reshape(ele,(3,3)))

print(n.reshape(2,5))

"""
[[0 1 2 3 4]
 [5 6 7 8 9]]
"""


"""
resize - return resize of array

diff between reshape and resize is the reshape() doesn't change the element of the array 
whereas resize()we can change the element of array

"""


rs = np.arange(5)

print(np.resize(rs,(4,4)))

"""
[[0 1 2 3]
 [4 0 1 2]]
"""

#here we create  2x3 array its fill all elements of array once it completed it take again
# start from the element



"""
Task
You are given a space separated list of nine integers. Your task is to convert this list into a 3 X 3 NumPy array.

Input Format
A single line of input containing 9 space separated integers.

Output Format
Print the 3 X 3 NumPy array.

Sample Input

1 2 3 4 5 6 7 8 9
Sample Output

[[1 2 3]
 [4 5 6]
 [7 8 9]]


"""

import numpy as np
n = int(input("Enter till what you want to element"))
lst = []
for i in range(1,n):
    lst.append(i)
c=np.array(lst)

c.resize(3,3)
print(c)
