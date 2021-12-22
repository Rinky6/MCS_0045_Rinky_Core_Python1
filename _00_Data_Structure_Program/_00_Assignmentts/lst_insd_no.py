# [[1], [2], [3], ..]

'''
#solution 1:
lst = []
for i in range(1,11):

    lst.append([i])


print(lst)
'''


#solution 2:
print([[i] for i in range(1,11)])


'''
#solution 3:
list1 = []
for i in range(1,11):
    list1.append([])

for i in range(0, len(list1)):
    list1[i].append(i + 1)

print(list1)
'''

