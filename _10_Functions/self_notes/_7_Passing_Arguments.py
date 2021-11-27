# Passing Arguments
'''
1. Positional arguments (Required arguments)
2. Default arguments
3. Keyword arguments (Named arguments)
'''

# 1. Positional arguments (Required arguments)

'''Positional Arguments

An argument is a variable, value or object passed to a function or method as input. Positional
arguments are arguments that need to be included in the proper position or order.

The first positional argument always needs to be listed first when the function is called. 
The second positional argument needs to be listed second and the third positional argument listed third, etc. 
'''
#State
list1=["lilli","chameli","samni"]
st={1,2,3}
def list(lst):
    #lst.append("sunflower")
  print("list of candidates    " ,lst)    #['lilli', 'chameli', 'samni']
#list(list)  #TypeError: list() missing 1 required positional argument: 'st'
#list(list,st)    #list() takes 1 positional argument but 2 were given
list(list1)


a=40
#b=30
def add():
    b=10
    c=a+b
    print("Addition of two no : " , c)
add()
#print("value of b", b) #NameError: name 'b' is not defined




str1="hello"
str2="world"
def concatinate(str1,str2):
    #str2="India"
    fstr=str1+" "+str2
    print("After concatination string  ", fstr)    #After concatination string   hello world

concatinate(str1,str2)


#State
list1=["lilli","chameli","samni"]
st={1,2,3}
def list(lst):
    #lst.append("sunflower")
  print("list of candidates    " ,lst)    #['lilli', 'chameli', 'samni']
#list(list)  #TypeError: list() missing 1 required positional argument: 'st'
#list(list,st)    #list() takes 1 positional argument but 2 were given
list(list1)





