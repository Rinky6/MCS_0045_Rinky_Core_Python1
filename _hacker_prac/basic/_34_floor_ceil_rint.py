'''

floor --->  The tool floor returns the floor of the input element-wise.
The floor of x is the largest integer i where i <= x.

ceil ---> The tool ceil returns the ceiling of the input element-wise.
The ceiling of x is the smallest integer i where i => x.

rint ---> The rint tool rounds to the nearest integer of input element-wise.
'''
import numpy as np



a = np.array(input().split(),float)


print(np.floor(a))
print(np.ceil(a))
print(np.rint(a))