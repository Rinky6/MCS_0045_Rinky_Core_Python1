"""

												type metaclass
												--------------

-->the 2 ways of creating the classes. one is the common way using the keyword "class".
Other way is using the metaclass "type". Like objects are the instances of the class.
Then all the classes are the instances of the metaclass "type". But the parent class of all
the classes is "object", that is why while writing class we write like class Foo(object) and
the type of the objec is also "type" metaclass. So when I write type() means it creates an
object and logically that object is class. for example function = type(), here function is
the ojbect of the metaclass "type", logically whatever the object derived form type metaclass
is a class.
"type()" takes 3 arguments.
syntax : type(name, bases, dictionary)
<name> specifies the class name. This becomes the __name__ attribute of the class.
<bases> specifies a tuple of the base classes from which the class inherits. This becomes
 the __bases__ attribute of the class.
<dict> specifies a namespace dictionary containing definitions for the class body. This becomes
 the __dict__ attribute of the class.

example:
--------
Foo = type("Foo", (), {attr : 100, attr_val : labmda x : x.attr})
x = Foo()
print(type(x))
print(x.attr)
print(x.attr_val())

output :
Foo
100
100

-->Here the type() has 3 arguments, first it creates a class with name "Foo". Whatever the name
we write in the position <name> it creates the class with that name. next empty tuple() means,
 the class Foo is not inherited from any other class. next are the dictionary with attributes
 which will be added to the namspace.
Here the attr_val has the lambda function which makes the attr_val as the function variable.
when we cal the x.attr_val() it prints the value. Here the lambda function takes one positional
argument x. Here we didn't give any value. The reason when we call x.attr_val() means x is itself
 pass as an argument. we see previously  functions has the self as the first parameter. which means
  by default, when a function is called with an object, that object is goes as the first arugment of
  that function.

---------------------------------------------------------------------------------------------------------

class A:

	def add(self, a, b):
		return a +  b

print(A().add(10,20))

output : 30
-->In the above program we call the function in a different way. Normally we called the function
using the object. Here used the A(). it is also an object. it doesn't make any difference.
Since add() is a instance method, can we call like A.add(10,20). will this works. let's see

class A:

	def add(self, a, b):
		return a + b

print(A.add(10,20))

output : TypeError: add() missing 1 required positional argument: 'b'

-->the reason is add() is having 3 parameters self, a, b. when we call A.add(10,20),
this means we are passing only 2, those 2 are takes by self and a. b don't get any value.
if we call A().add(10,20) means we are calling with an object, so if we are calling with an
object means, that object is automatically takes as the first argument which is self in the
add() method.

-->We don't want any error when called like A.add(10,2), what we have to do is remove
the self for the add() method. see below, it don't give error.
WHEN WE ARE CALLING A METHOD DIRECTLY WITH THE CLASS NAME, THEN THAT METHOD'S DEFINITION DON'T
NEED self IN IT'S PARAMETERS LIST. THIS IS NOT APPLICABLE DURING THE INHERITANCE.
class A:

	def add(a, b):
		return a + b
print(A.add(10,20))

output : 30

"""