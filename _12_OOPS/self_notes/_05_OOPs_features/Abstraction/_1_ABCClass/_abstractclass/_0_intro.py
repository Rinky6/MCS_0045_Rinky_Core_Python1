'''
from abc import ABC, abstractmethod
class A(ABC):
    @abstractmethod
    def fun(self):
        pass

    @abstractmethod
    def fun1(self):
        pass


class B(A):
    def fun(self):
        print("main func")

    def fun1(self):
        print("2nd func")


obj = B()
obj.fun()
obj.fun1()
'''
from abc import ABC, abstractmethod


class A(ABC):

    def fun(self):
        pass


    def fun1(self):
        pass
A.fun = abstractmethod(A.fun)
A.fun1 = abstractmethod(A.fun1)

class B(A):
    def fun(self):
        print("main func")

    def fun1(self):
        print("2nd func")


obj = B()
obj.fun()
obj.fun1()









dict1 = {1:1,2:2}
dict2 = {3:1,4:2}

#dict2.update(dict1)
#print(dict2)


lst = [1,2,3,4,5,6,7,8,9]
#[3,6,9]
#[2,5,8]
#[1,4,7]

lst1 = []
for i in range(len(lst)):


    if lst[i] == 1:
        l2 = lst[i:: 3]
        lst1.append(l2)
    if lst[i] == 2:
        l1 = lst[i:: 3]
        lst1.append(l1)
    if lst[i] == 3:
        l = lst[i:: 3]
        lst1.append(l)

print(lst1)





