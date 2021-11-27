# P01. REQ : Count characters in string"

'''
1. CRUD
2. STATE      - Data types/structures
3. BEHAVIOR   - DTS / Operators / DM or Loops
'''
'''
1. CRUD       -->  Retrieval
2. STATE      -->  string 
3. BEHAVIOR   -->  int  |  =   +=    |   for   
'''

# 0. Mathematics 80%
'''
1. Define the string 
2. Take initial count as 0
3. Start reading it. 
4. While reading each char, increase the count
'''

# 1.Builtin functions 80%

print("-----1. Builtin Functions--------")

message = 'This is my first program'  # static way
# message = input("Enter any string : ")
#res = len([ele for ele in message if ele.isalpha()])
lg=0
for ele in message:
 if ele.isalpha():
     lg+=1
print("Length of given string : ", lg)


# 2. Algorithm  80%

print("--------2. Algorithm----------")

message = 'This is my second program'
le = 0
for char in message:
    if char !=" ":
     le += 1
print("Length of given string : ", le)

# 3 Using Functions  ==> 50 programs
print("--------3 Using Functions----------")

print("--------Without return type----------")
#State
msg = input("Enter a string ")
def count_chars(m):
 leg = 0
 for char in m:

    if char !=" ":
     leg += 1
 print("Length of  string : ", leg)
count_chars(msg)

print("--------With return type----------")
#State
msg = input("Enter a string ")
def count_chars(m):
 leg = 0
 for char in m:

    if char !=" ":
     leg += 1
 return leg
tchar=count_chars(msg)
print("total no of character  ", tchar)

# 4 OOPS              ==> 30 programs
print("--------4 Object Oriented----------")
class Leg_String:
    def __init__(self,legstr):
     self.legstr=legstr
    def leg_of_string(self):

     self.legstr=0
     for i in leg:
        if i != " ":
         self.legstr+=1
     print("Total no of character in string  " , self.legstr)

leg=input("Enter  string   ")
length=Leg_String(leg)
length.leg_of_string()



# 5 Exception handling  ==> 15 programs
print("--------5 Exception handling----------")

# 6 File Handling  ==> 10 programs
print("--------6 File Handling----------")

# 7 Database interaction MVC  ==> 5 programs
print("--------7 Database interaction----------")



# 8 UI Interaction   ==> 3 programs
print("--------8 UI Interaction----------")
