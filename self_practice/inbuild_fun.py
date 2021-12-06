''' zip() - The Python zip() function accepts iterable items and merges them into a single tuple.
 The resultant value is a zip object that stores pairs of iterables. You can pass lists, tuples, sets,
 or dictionaries through the zip() function.
'''

zip_lst=[1,2,'sal',4,5]
zip_lst1=['MCS','Rinky','48000','S/W','Python']
final_zip_lst=zip(zip_lst,zip_lst1)
print("After zipping : ",final_zip_lst)
print("After zipping using list : ",list(final_zip_lst))

#ip_lst,zip_lst1=zip(final_zip_lst)
#print("After unzipping : ", zip_lst,zip_lst1)




zip_lst=(1,2,'sal',4,5)
zip_lst1=('MCS','Rinky','48000','S/W','Python')
final_zip_lst=zip(zip_lst,zip_lst1)
print("After zipping using set: ",set(final_zip_lst))

zip_lst={1,2,'sal',4,5}
zip_lst1={'MCS','Rinky','48000','S/W','Python'}

final_zip_lst=zip(zip_lst,zip_lst1)
print("After zipping using dic : ", dict(final_zip_lst))


zip_lst=(1,2,'sal',4,5)
zip_lst1=('MCS','Rinky','48000','S/W','Python')

final_zip_lst=zip(zip_lst,zip_lst1)
print("After zipping using tuple : ",tuple(final_zip_lst))


for i,j in zip(zip_lst,zip_lst1):
    print("iterate using for loop :", i,j
          )











"""
The abs() function returns the absolute value of the given number. If the number is a complex number, abs() returns
its magnitude.

abs() Syntax
The syntax of abs() method is:

abs(num)
"""


number = -20

absolute_number = abs(number)
print(absolute_number)

number = -20.53

absolute_number = abs(number)
print(absolute_number) #20.53

'''
number = "Rinky"
print('-------asign string value-------')
absolute_number = abs(number)   # bad operand type for abs(): 'str'
print(absolute_number)   

'''

number = 5-4j

absolute_number = abs(number)
print(absolute_number) #6.4031242374328485


'''
all()- all() Return Value  true or false
all() function returns:

True - If all elements in an iterable are true
False - If any element in an iterable is false
When	Return Value
All values are true	True
All values are false	False
One value is true (others are false)	False
One value is false (others are true)	False
Empty Iterable	True


'''


# all values true
l = [1, 3, 4, ]
print(all(l))   #True



l = (1, 3, 4, 5,)
print(all(l)) #true



# all values true
l = {1, 3, 4, 5}
print(all(l))     #True

# empty
l = [1, 3, 4, 5,'']
print(all(l))    # False

# all values false
l = [0, False]
print(all(l))    #False

# one false value
l = [1, 3, 4, 0]
print(all(l))   #False

# one true value
l = [0, False, 5]
print(all(l))

# empty iterable
l = []
print(all(l))   #True


l = { }
print(all(l))   #True



'''


any()	Returns True if any item in an iterable object is true

Syntax
any(iterable)

'''
# all values true
l = {1, 3, 4, 5}
print(any(l))     #True

# empty
l = [1, 3, 4, 5,'']
print(any(l))    # true

# all values false
l = [0, False]
print(any(l))    #False

# one false value
l = [1, 3, 4, 0]
print(any(l))   #True

# one true value
l = [0, False, 5]
print(any(l))    #true

# empty iterable
l = []
print(any(l))   #false


l = { }
print(any(l)) #false




'''
ascii()	-Returns a readable version of an object. Replaces none-ascii characters with escape character

'''

l='Rinky'
print(ascii(l))








