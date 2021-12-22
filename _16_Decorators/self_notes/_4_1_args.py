# *ARGS
def my_fun(*args):
    print(args, "******", type(args))
    for val in args:
        print(" value are : ",val)
    print("------------------")

my_fun()
print("***************************")
my_fun('Hello', 'Welcome', 'to', 'My world')
my_fun(1, 2, 3, 4, 5)
my_fun(1, 2.4, 'Rinky', True, [1, 2, 3], (1, 2, 3), {1:1, 2:2}, {11, 2, 3})



print("-------Program 2----------------")
def myFun(val, *args):
    print("First argument: ", val, "------", args)
    for arg in args:
        print("Next argument through *args :", arg)

# myFun()  # Error
myFun(100)
myFun(100, 'Rinky')
myFun('', 'Welcome', 'to', 'my world')

