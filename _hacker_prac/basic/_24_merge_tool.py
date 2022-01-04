s = 'AAABCADDE'

k = 3

value = len(s) // k

print(value)

list1 = [[] for i in range(k)]

for i, j in zip(range(0, len(s), value), range(k)):
    for ch in s[i: i + value]:
        list1[j].append(ch)

print(list1)

list2 = [[] for i in range(k)]
for i in range(len(list1)):
    for j in list1[i]:
        if j not in list2[i]:
            list2[i].append(j)

for i in list2:
    print(''.join(i))