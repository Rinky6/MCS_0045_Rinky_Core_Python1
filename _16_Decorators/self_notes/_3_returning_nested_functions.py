# 3. RETURNING FUNCTIONS


print("---------------3. RETURNING NESTED FUNCTION NAME------------------")


def print_msg(msg):
    # This is the outer enclosing function
    def printer():
        # This is the nested function
        print("inner function ", msg)
    print(printer) #<function print_msg.<locals>.printer at 0x0000014222D72170>
    return printer # returns the nested function
# Now let's try calling this function.
# Output: Hello
print(print_msg("Hello"))  #<function print_msg.<locals>.printer at 0x0000014222D72170>







def print_msg(msg):
    # This is the outer enclosing function
    def printer():
        # This is the nested function
        print("inner function ", msg)  #inner function  Hello
    print(printer) #<function print_msg.<locals>.printer at 0x0000014222D72170>
    printer() # returns the nested function
# Now let's try calling this function.
# Output: Hello
print(print_msg("Hello"))  #None


def print_msg(msg):
    def printer():
        print("inner function : ", msg)  #inner function :  world
    printer()
print("after execution inner function 1 : ", print_msg("world")) #after execution inner function 1 :  None

def print_msg(msg):
    def printer():
        print("inner function : ", msg )  #inner function :  world
    return printer()
print("after execution inner function  2 : ", print_msg("world"))  #after execution inner function  2 :  None

def print_msg(msg):
    def printer():
        msg1 = msg +" " + "World"
        return msg1
    rst = printer()
    print(rst) #Hello World
print("after execution inner function  3 : ", print_msg("Hello")) # None




# Defining a Closure Function


def print_msg(msg):
    # This is the outer enclosing function

    def printer():
        # This is the nested function
        print(msg)

    return printer  # returns the nested function


# Now let's try calling this function.
# Output: Hello
another = print_msg("Hello")
another()






def generate_power(exponent):
    def power():
        return exponent ** 3
    print("---------------")
    print("----",power) ##<function generate_power.<locals>.power at 0x000001CC8D9D20E0>
    print("----------", power() ) #1728
    return power


print(generate_power(12))   #<function generate_power.<locals>.power at 0x00000128E96C20E0>
print(generate_power)   #<function generate_power at 0x0000028DCA8E3E20>
#


def check(n):

   def check():
       while True:
        if n % 2 == 0:
           return n
        else:
           print("Please enter even no")
           break


   print("result = " , check())

   print("After operation : ",check()**2)   # 4
no = int(input("enter your no : "))
check(no) #2




def check(n):

   def check():
       while True:
        if n % 2 == 0:
           return n
        else:
           print("Please enter even no")



   print("result = " , check())

   print("After operation : ",check()**2)    #unsupported operand type(s) for ** or pow(): 'NoneType' and 'int'
no = int(input("enter your no : "))
check(no) #3


def check(n):
    def check1():
        while True:
            if n % 2 == 0:
                return n
            else:
                print("Please enter even no")

    print("result = ", check1())

    print("After operation : ", check1() ** 2)  # unsupported operand type(s) for ** or pow(): 'NoneType' and 'int'


no = int(input("enter your no : "))
check(no)  # 3def check(n):

def check(n):
    def check1():
       while True:
        if n % 2 == 0:
           return n
        else:
           print("Please enter even no")



    print("result = " , check1())
    print("After operation : ",check1()**2 ) # 4 , print please enter no infinity times
no = int(input("enter your no : "))
check(no) #2 3



def check(n):
    def check1():
       while True:
        if n % 2 == 0:
           return n
        else:
           print("Please enter even no")
           break

    print("result = " , check1()) # after enter second inpute(odd) 'None'
    print("After operation : ",check1()**2 ) # 4 , unsupported operand type(s) for ** or pow(): 'NoneType' and 'int'
no = int(input("enter your no : "))
check(no) #2 3


def lsttotpl(lst):
    print("---",lst)   #[1, 2, 3, 4, 5, 6, 7, 8, 9]


    def cnvrttpl():
        tuple1 = tuple(lst)
        print("After conversion : ",tuple1)
        return tuple1
    acnvrt=cnvrttpl()

    sumoftuple= sum(acnvrt)

    print("After sum the tuple : ", sumoftuple)

    if sumoftuple % 2 == 0 :
        print("You can proceed")

    else:
        print("please go back")

lst = []
for i in range(1,10):
    lst.append(i)
print(" print ",lsttotpl(lst)) #None
#print(" print ",lsttotpl(lst) + 2) unsupported operand type(s) for +: 'NoneType' and 'int'





'''
def parent(num):

    def first_child():
        return "Printing from the first_child() function."

    def second_child():
        return "Printing from the second_child() function."

    if num == 10:
        return first_child
    else:
        return second_child
    
    try:
        assert num == 10
        print("Assertion is True.Continue to execute the remaining code")
        return first_child  # returning function name
    except AssertionError:
        return second_child # returning function name
    finally:
        print("Finally executed")
    '''
'''
f_c = parent(10)

print("*************")
print("Returning function name FC : ", f_c)
print("Executing function FC      : ", f_c())
print("*************")

s_c = parent(11)
print("Returning function name SC : ", s_c)
print("Executing function SC      : ", s_c())

print("-------------------------------------")

def parent1():
    def first_child():
        return "In First Child"
    # return first_child
    msg = first_child()
    return msg

# parent1 = 0x000002C5F8EA3D08
    # first_child = 0x0000020456463E18
x = 10
print(id(x))  # x = 1885629744
print(x)
print("Printing parent1 function : ", parent1)
print("Calling parent1 function : ", parent1())
x = parent1()  # 0x0000020456463E18
print("Printing child1  function : ", x)
# print("Calling child2 function : ", x())
print("Calling child3 function : ", parent1())
# print("Calling child4 function : ", parent1()())
'''