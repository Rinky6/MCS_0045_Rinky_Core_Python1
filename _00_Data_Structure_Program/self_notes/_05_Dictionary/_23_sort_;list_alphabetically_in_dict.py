num = {'n1': [2, 3, 1], 'n2': [5, 1, 2], 'n3': [3, 2, 4]}
for x,y in num.items():
    num[x]=sorted(y)
print(num)

