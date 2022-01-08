for i in range(1,6):
    print()
    for j in range(1,i+1):
        print(j ,end = "")

"""
1
12
123
1234
12345
"""
print("\n-------------------------------------")

for i in range(6,1,-1):
    print()
    for j in range(1,i):
        print(j, end="")


"""
12345
1234
123
12
1
"""


print("\n----------------s1---------------------")

for i in range(1,6):
    print()
    for j in range(1,i+1):
        print(i ,end = "")

print("\n----------------s2---------------------")

for i in range(1,6):
    print(str(i) *i)

"""
1
22
333
4444
55555
"""

for i in range(1,11):

    if i%2 == 0:
        print((str(i) +" ")*i )


"""
2 2 
4 4 4 4 
6 6 6 6 6 6 
8 8 8 8 8 8 8 8 
10 10 10 10 10 10 10 10 10 10 
"""


lst = ([chr(i) for i in range(97,103)])
print(lst)
for i in range(len(lst)):
    print()
    for j in range(i+1):
        print(lst[j] , end = '')
   # for j in range(1,lst[]):
        #print(j)
print("\n ----------------------------")
"""
a
ab
abc
abcd
abcde
abcdef
"""
lst = [chr(i) for i in range(97,104)]

for i in range(0, len(lst), 2):
    print(' '.join(lst[0 : i + 1 : 2]))
'''
a
a c
a c e
a c e g
'''
print("-------------------------")
for i in range(1,6):
    print()
    for j in range(1, i + 1):
        lst = list([j])
        print(lst, end = '')

"""
[1]
[1][2]
[1][2][3]
[1][2][3][4]
[1][2][3][4][5]

"""
print("\n---------------")
n =int(input("Enter a no "))
for i in range(1,n):
    print(' ' * (n-i),"*" * i )
"""
     *
    **
   ***
  ****
"""