"""

An iterable is any object, not necessarily a data structure, that can return an iterator
(with the purpose of returning all of its elements). That sounds a bit awkward, but there
is an important difference between an iterable and an iterator.

"""


lst = [1,2,3,4]
y = iter(lst)
print(type(lst))
print(type(y))
print(next(y))





import dis
x = [1, 2, 3]
dis.dis('for _ in x: pass')





from itertools import count
counter = count(start=13)
print(next(counter)) #13

print(next(counter)) #14





from itertools import cycle
colors = cycle(['red', 'white', 'blue'])
next(colors)
#'red'
next(colors)
#'white'
next(colors)
#'blue'
next(colors)
#'red'






from itertools import islice
colors = cycle(['red', 'white', 'blue'])  # infinite
limited = islice(colors, 0, 4)            # finite
for x in limited:                         # so safe to use for-loop on
   print(x)

""" 
red
white
blue
red
"""





class fib:
   def __init__(self):
        self.prev = 0
        self.curr = 1
   def __iter__(self):
         return self

   def __next__(self):
          value = self.curr
          self.curr += self.prev
          self.prev = value
          return value

f = fib()
list(islice(f, 0, 10))
#[1, 1, 2, 3, 5, 8, 13, 21, 34, 55]