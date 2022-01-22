
'''class Hello:
    def run(self):
        for i in range(5):
         print("Hello")

class Hi:
    def run(self):
        for i in range(5):
         print("Hi")

obj1 = Hello()
obj2 = Hi()

obj1.run()
obj2.run()

'''
"""
In normal class generally if we want to call the any function we need to call the that function using 
object of that class .
"""

#If we want to call the these two function simultaneouly we use thread

'''
import threading
from time import sleep

class Hello(threading.Thread):
    def run(self):
        for i in range(5):

            print("Hello")
            sleep(1)


class Hi(threading.Thread):
    def run(self):
        for i in range(5):
            print("Hi")
            sleep(1)


obj1 = Hello()
obj2 = Hi()

obj1.start()
#obj1.join()
obj2.start()
#obj2.join()
'''
"""
Hello
Hi
HelloHi

HiHello

HelloHi

we are getting above output because of collision
generally it is happening because may be two thread come to cpu at same time.
we thought they are working parllely but whenever the thread is sleeping mode till the woke up the another
thread access the  cpu.
if we want to avoid this collision we have to give some gap between them
see below

"""
'''


import threading
from time import sleep

class Hello(threading.Thread):
    def run(self):
        for i in range(5):

            print("Hello")
            sleep(1)


class Hi(threading.Thread):
    def run(self):
        for i in range(5):
            print("Hi")
            sleep(1)


obj1 = Hello()
obj2 = Hi()

obj1.start()

sleep(0.5)
obj2.start()




'''
'''  
import threading
from time import sleep

class Hello(threading.Thread):
    def run(self):
        for i in range(5):

            print("Hello")
            sleep(1)


class Hi(threading.Thread):
    def run(self):
        for i in range(5):
            print("Hi")
            sleep(1)


obj1 = Hello()
obj2 = Hi()

obj1.start()

sleep(0.5)
obj2.start()


print("bye")

'''

'''
Hello
Hibye

Hello
Hi
Hello
Hi
Hello
Hi
Hello
Hi




Here its bye printing after obj2.start execution what happening here actually
here three threads are there obj1 , obj2,main thread 
after 1st execution of obj1 and obj2 the main thread  execute
after that remaining part are execute for avoid that we use join()
it work like once there obj1 and obj2 thread completed the main thread execute
main thread waiting for the obj1 thread and obj2 thread complete

'''





import threading
from time import sleep

class Hello(threading.Thread):
    def run(self):
        for i in range(5):

            print("Hello")
            sleep(1)


class Hi(threading.Thread):
    def run(self):
        for i in range(5):
            print("Hi")
            sleep(1)


obj1 = Hello()
obj2 = Hi()

obj1.start()

sleep(0.5)
obj2.start()
obj1.join()
obj2.join()

print("bye")
