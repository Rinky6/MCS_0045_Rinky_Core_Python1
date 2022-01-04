"""
You are given a two lists A and B. Your task is to compute their cartesian product AXB.

"""
'''
from itertools import product

ls=[1,2,3,4]
ls2 = [2,4,5]
print(*product(ls,ls2))

'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product
a = map(int, input().split())
b = map(int, input().split())

print(*product(a, b))

