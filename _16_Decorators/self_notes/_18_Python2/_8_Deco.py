
'''
-->first take a look at the inner functions. Decorators are the higher order functions,
becuase they take the function as the argument and returns a new function as the return value.
For implementing decorator we need 2 functions like one function to take the the decorated
function as the argument and an inner function to call the decorated function. min 2 function
one parent and one child to make the program more readable.

-->first of all let's see what happens when we create a new function in python.
example:
--------
def outer():
	print("this is the outer function")
	def inner():
		print("this is the inner function")
	inner()
	return inner
print(outer())

output :
--------
this is the outer function
this is the inner function
<function outer.<locals>.inner at 0x7f88ce1446a8>

-->In the above program we have 2 functions outer() and inner(). here when we create a function,
 the 'def' do 2 things.
1)it creates a function object, here the function objects are outer() and inner().
2)it creates a function variables outer, inner and make those variables pointing to those objects
 outer() and inner().
Here 'return inner' means we are returning the function variable. if we print it, it returns the
address. "inner" is just a name or function variable created in the namespace. inner means
function variable, only the paranthesis () will call the function. Here the outer() returns the
function variable 'inner' and we can call that function variable, which again calls the inner().

example:
--------
def outer():
	print("this is the outer function")
	pycon = 2020
	def inner():
		print("this is the inner function")
	inner()
	return inner
outer()

-->the above program returns 2 kinds of the output. when this program runs in the IDLE
it gives the following output.

this is the outer function
this is the inner function


-->in the interactive python it gives the values returned by return statement,
but in the idle it don't dispaly those values.


=
example:
--------
def outer():
	print("this is the outer function")
	pycon = 2020
	def inner():
		print("this is the inner function")
	inner()
	return inner
inside = outer()
print(inside)

-->the above program give the below output.

this is the outer function
this is the inner function
<function outer.<locals>.inner at 0x0096F348>

-->in the above result it gives the 2 print statements and the "inside" which is a
 function variable. when we try to print the function it gives the memory location.
 We can also call a function variable. see the below program

example:
--------
def outer():
	print("this is the outer function")
	pycon = 202
	def inner():
		print('this is the inner function')
	inner()
	return inner
inside = outer()
print(inside())

-->the inside varible contains the return value of the functio outer().
so inside contains inner. when we call the function vairable inside(),
it means we are calling the inner(). It returns the following output.
this is the outer function
this is the inner function
this is the inner function
None

-->In the above it returns None at the last, because the inner function is not returning

anything, it only has one print statement and when we try to print the result of a function
when it dont' have a return statement, it gives the result None. FOR FUNCTIONS THE DEFAULT
 RETURN VALUE IS NONE.

'''





def decorator(fun):
    def inner():
        print('before main function')
        fun()
        print('after main function')

    return inner


@decorator
def func():
    print('this is the main function')


func()


def decorator(fun):
    def inner():
        print('before main function')
        fun()
        print('after main function')

    return inner


def func():
    print('this is the main function')


func = decorator(func)
func()

from functools import wraps


def decorator(fun):
    @wraps(fun)
    def inner():
        print('before main function')
        fun()
        print('after main function')

    return inner


@decorator
def func():
    print('this is the main function')


func()


