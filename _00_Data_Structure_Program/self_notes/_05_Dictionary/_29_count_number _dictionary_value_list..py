'''count number of items in a dictionary value that is a list.'''

dict =  {'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2']}
# ctr = sum(map(len, dict.values()))
# print(ctr)


# print(len(dict.values()))
for x,y in dict.items():
    dict[x]=len(y)
print(dict)
