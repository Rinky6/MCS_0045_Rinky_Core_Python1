"""
iterable -----> __iter__ or __getitem__,
iterator ------> __next__ , Whenever there is no element it returns StopIteration Exception
iteration -----> process of iterator

return terminate the function but yield not



def gen(n):

    for i in n:
        for j in i:
           yield j


a = gen([[1,2,3]])

for i in range(2):
    print(next(a))

"""
1
2
"""



def gen(n):

    for i in n:
        yield from i


a = gen([[1,2,3]])

for i in range(2):
    print(next(a))

"""

1
2
"""











def gen():

    return 5

value=gen()

print(value)



def gen():
    yield 1
    yield 2
    yield 3
    yield 4

value=gen()
print(value)  #<generator object gen at 0x000001C276896030>
print(value.__next__())
print(value.__next__())
print(value.__next__())
print(value.__next__())
#print(value.__next__()) #StopIteration







def topten():
    n=1
    while n<=10:
        sq=n*n
        yield sq
        n+=1

value = topten()
for i in value:
    print(i)

lst = [ 1,3,5,7,6,2]
i = lst.__iter__()
print(i)   #<list_iterator object at 0x00000221E7793EE0>
print(dir(i))
ii=iter(lst)
print(ii)#<list_iterator object at 0x00000221E7793EB0>
print(dir(i))
print(dir(lst))
print(next(ii))
print(next(ii))



print("-------------------------")
while True:
    try :
        item =next(i)
        print(item)
    except StopIteration:
        break


print("---------------Class-----------------")

class My_Range:
    current=0
    def __init__(self,start , end):
        self.start = start
        self.end=end
    def __iter__(self):
        return self

    def __next__(self):

          current = self.start
          self.start += 1

          if self.start >self.end:

            raise StopIteration

      #except StopIteration:
        #  print("iteration completed")

          return current

obj = My_Range(11,19)
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))

print("-------------------Problem--------------------")


class Sentence():
    def __init__(self,s):
        self.s=s
        self.index = 0
        self.word = self.s.split()
        print(self.word)
    def __iter__(self):
        print(self)
        return self

    def __next__(self):

         if self.index >= len(self.word ):
            raise StopIteration
        #except StopIteration:
          #  print("Iteration completed")
         index = self.index
        #print(index)
         self.index += 1
         return self.word[index]
obj = Sentence("This is a test")
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))

"""

# send() in generator
def prac():
    rs = yield
    yield rs




rst = prac()

print(next(rst))   #None

print(rst.send('Rinky'))


"""
In this program the first execution start from prac()  thn control goes to def prac() 
enter in the function its return generator object after that it's come to a print(next(rst))
and control goes to fun and after that is goes to the next line where when it found yield it pause the execution 
and then its print the None because there yield contain now None. after that we send a any data which one yield
contain and print the data whatever we send.


"""
