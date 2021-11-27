class A:
	def __init__(self, x):
		self.x = x

a = A(1)
print(a.x)
a.__dict__['x'] = 2
print(a.x)





class A:
	pass

a = A()
print(type(a.__dict__))





class Employee:
	def __init__(self, name, age):
		self.name = name
		self.age = age

employee1 = Employee(23 ,'jahn')
employee2 = Employee('Rambo', 28)

print("The output of employee1.__dict__ is : ", employee1.__dict__)
print("The output of employee2.__dict__ is : ", employee2.__dict__)








class Person:
	def __init__(self, name):
		self.name = name

person = Person('John')

print(person)

person.__dict__['name']

print(person)



class A:
	def __init__(self, x):
		self.x = x

a = A(1)
a.__dict__['y'] = 7
print(a.y)
print(a.__dict__)




def square(n):
    '''Takes in a number n, returns the square of n'''
    return n**2

print(square.__doc__)
print(print.__doc__)
