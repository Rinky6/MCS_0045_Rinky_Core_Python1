"""
Some points on Python class:

Classes are created by keyword class.
Attributes are the variables that belong to a class.
Attributes are always public and can be accessed using the dot (.) operator. Eg.: Myclass.Myattribute
Class Definition Syntax:

class ClassName:
   # Statement-1
   .
   .
   .
   # Statement-N




self represents the instance of the class. By using the “self” keyword we can access the attributes and methods of the
class in python. It binds the attributes with the given arguments.
The reason you need to use self. is because Python does not use the @ syntax to refer to instance attributes. Python
decided to do methods in a way that makes the instance to which the method belongs be passed automatically, but not
received automatically: the first parameter of methods is the instance the method is called on.


"""




class Dog:

	# class attribute
	attr1 = "mammal"

	# Instance attribute
	def __init__(self, name):
		self.name = name

# Driver code
# Object instantiation
Rodger = Dog("Rodger")
Tommy = Dog("Tommy")

# Accessing class attributes
print("Rodger is a {}".format(Rodger.__class__.attr1))
print("Tommy is also a {}".format(Tommy.__class__.attr1))

# Accessing instance attributes
print("My name is {}".format(Rodger.name))
print("My name is {}".format(Tommy.name))
