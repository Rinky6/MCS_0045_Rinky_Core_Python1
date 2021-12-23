print("--------------For Decorator purpose-----------")
def myFun(*args, **kwargs):
    print("args: ", args)
    print("kwargs: ", kwargs)
# Now we can use both *args ,**kwargs to pass arguments to this function :
myFun()
myFun('geeks', 'for', 'geeks', first="Geeks", mid="for", last="Geeks", address={'hno':25,'area':'BLR'})
myFun('geeks', 'for', 'geeks', {1:1,2:2,3:3})




my_frst_dict = {"C": 9, "D": 10}
my_scnd_dict = {"A": 11, "B": 12}

my_scnd_dict.update(my_frst_dict)
res = my_scnd_dict | my_frst_dict
print("dict merging using pipe :", res)

print("After merging of dict : ", my_scnd_dict )


my_first_dict = {"A": 1, "B": 2}
my_second_dict = {"C": 3, "D": 4}


my_merged_dict = {**my_first_dict, **my_second_dict}


print("after merging : " , my_merged_dict)


