'''
try -->exceptions can be handled using a try statement.

except --> The critical operation which can raise an exception is placed inside the try clause.
           The code that handles the exceptions is written in the except clause.

finally --> The try statement in Python can have an optional finally clause. This clause is executed no matter what,
            and is generally used to release external resources.
else --> Python try with else clause
In some situations, you might want to run a certain block of code if the code block inside try ran without any errors.
For these cases, you can use the optional else keyword with the try statement.

Note: Exceptions in the else clause are not handled by the preceding except clauses.
'''
#syntax

try:
   # do something
   pass

except ValueError:
   # handle ValueError exception
   pass

except (TypeError, ZeroDivisionError):
   # handle multiple exceptions
   # TypeError and ZeroDivisionError
   pass

except:
   # handle all other exceptions
   pass



'''
Raising Exceptions in Python
============================
Exceptions are raised when errors occur at runtime. We can also manually raise exceptions using
the raise keyword.
'''
#raise KeyboardInterrupt

#raise MemoryError("This is an argument")

#MemoryError: This is an argument

try:
  a = int(input("Enter a positive integer: "))
  if a <= 0:
     raise ValueError("That is not a positive number!")
except ValueError as ve:
   print("Exception")

#Enter a positive integer: -2
#That is not a positive number!



'''
Python try with else clause
In some situations, you might want to run a certain block of code if the code block inside try ran without any errors. 
For these cases, you can use the optional else keyword with the try statement.

Note: Exceptions in the else clause are not handled by the preceding except clauses.


'''


# program to print the reciprocal of even numbers

try:
    num = int(input("Enter a number: "))
    assert num % 2 == 0
except:
    print("Not an even number!")
else:
    reciprocal = 1/num
    print(reciprocal)



try:
    num=int(input("Enter a number: "))
    rslt=num/0
    print(rslt)
except ZeroDivisionError:
    print(ZeroDivisionError)




