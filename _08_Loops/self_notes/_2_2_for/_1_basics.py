'''
syntax
 for variable in sequence
 or
 for variable in range (sequence)
'''


"""for i in range(10):
    x=10
    print(i)
print(i)  #9
print(x)  #10"""


for i in 'Rinky':
    print(i)

for i in [1,'Rinky',2,'Kumari',3]:
    print('List ',i)

for i in (1,'Rinky',2,'Kumari',3):
    print('tuple', i)

for i in {1,'Rinky',2,'Kumari',3}:
    print('set', i)


for key,val in {'eid': 1,'ename' :'Rinky', 'sal' :20000}.items():
    print('dic with key val', key,val)

for i in {'eid': 1,'ename' :'Rinky', 'sal' :20000}.keys():
    print('dic', i)

for i in {'eid': 1, 'ename': 'Rinky', 'sal': 20000}.values():
    print('dic', i)


