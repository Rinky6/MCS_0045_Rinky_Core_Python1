# 2. NESTED FUNCTIONS :
print("---------------2. NESTED FUNCTIONS------------------")


def outer_func():
    def inner_func():
        print("Hello, World!")
    return inner_func
    print("Ssssssssss")
outer_func()


def parent(rcv):
    def child():
        print("hello", rcv)
    child()

parent("world")







def parent():
    print("Im parent class")
    def child():
        print("My child func")
    child()
    print(child) #<function parent.<locals>.child at 0x0000013A68E62320>
parent()



def operation(number):
    print("Im parent function")
    def inner_operation():
        sum1 = number ** 3
        print("sum of given no" , sum1)   #sum of given no 1000
    inner_operation()
print(operation(10))   #None


def pallindrom(s):

    def constr():
        wd = input("Enter the any word")
        afrcnct = s+wd
        print(afrcnct)
        return afrcnct
    rst = constr()
    print("befor reverse : ",rst)
    rev = ''.join(reversed(rst))
    print("after reverse : ",rev)
    if(rst == rev):
        print("given string is  pallindrom")
    else:
        print("Given string is not pallindrom")

wrd = input("Enter any word : ")

pallindrom(wrd)




rst1=""
def pallindrom(s):

    def constr():
        wd = input("Enter the any word")
        afrcnct = s+wd
        print(afrcnct)
        return afrcnct
    rst = constr()
    print("before reverse : ",rst)
    #print("rvrs : ", rst[::-1])
    rst1 = rst[::-1]
    print("after reverse : ",rst1)
    if(rst == rst1):
        print("given string is pallindrom")
    else:
        print("Given string not pallindrom")

wrd = input("Enter any word")

pallindrom(wrd)














'''
def parent():
    print("Before Nested Function")

    def first_child():  # nested function
        return "In nested func : first_child()"

    print("After Nested Function")

    print("Inside parent :", first_child())
    print("Inside parent :", first_child)

    return first_child  # <function parent.<locals>.first_child at 0x000001B0034A3BF8>

# print(parent.first_child())

f_child = parent()
print("Outside parent :", f_child)
print("Outside parent :", f_child())

# parent.first_child()  # It gives error
# parent.first_child()  This is not the way to call nested function

print("Parent function address: ", parent)  # parent = <function parent1 at 0x000001BF373B1E18>   x = 10

print("---Parent function call :-----")
print(parent())
nest_func_addr = parent()

print("Calling  nested function from outside function      : ",nest_func_addr())  # 12 line
print("Printing nested function name from outside function : ",nest_func_addr)    # 13 line

print("------Using EXCEPTION HANDLING ---------------- ")
try:
    #parent.first_child()
    f_child = parent()
    print("Calling child function : ",f_child())
except AttributeError as err:
    print("Exception :: ", err)
    print("--You cannot call nested function directly------")

'''