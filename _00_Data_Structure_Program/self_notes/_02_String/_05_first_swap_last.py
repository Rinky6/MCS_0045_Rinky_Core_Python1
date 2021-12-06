# P01. REQ : Swap last char with first ,first with last  ie., "Python" <===> "nythop"

'''
1. CRUD
2. STATE      - Data types/structures
3. BEHAVIOR   - DTS / Operators / DM or Loops
'''
'''
1. CRUD       -->  update
2. STATE      -->  string 
3. BEHAVIOR   -->  int  |  = |  +  
'''

# 0. Mathematics 80%
'''
1.We initialize a variable frst, which stores the first character of the string (str[0])
2.We initialize another variable lst that stores the last character (str[-1])
3.Then we will use string slicing, str[1:-1], this will access all the characters from the 2nd position excluding the last character.
4.Then we add these three as required forming a new string that has the first and last characters of the original string swapped. 
    And then we will print it.
'''

# 1.Builtin functions 80%

print("-----1. Builtin Functions--------")

str = 'This is my first program'  # static way
# message = input("Enter any string : ")
frst=str[0]
print(frst)
lst=str[-1]
print(lst)
swap=lst + str[1:-1]+frst
print("Length of given string : ", swap)





# 2. Algorithm  80%

print("--------2. Algorithm----------")

message = 'Hello World'
le = 0
for char in message:
    le += 1
print("Length of given string : ", le)

# 3 Using Functions  ==> 50 programs
print("--------3 Using Functions----------")
print("--------Without return type----------")
#State
msg=input("Enter String  ")

def leng(str): #function definition
    #function body
 leg = 0
 for char in str :
  leg += 1
 print("Length of String  : " , leg) #responsibility

leng(msg)

print("--------With return type----------")
#State
msg=input("Enter String  ")
def leng(str):     #function definition
    #function body
 leg = 0
 for char in str :
  leg += 1
 return leg   #Return type

length=leng(msg)
print("Lenth of string  " ,length)



# 4 OOPS              ==> 30 programs
print("--------4 Object Oriented----------")
class Leg_String:
    def __init__(self,legstr):
     self.legstr=legstr
    def leg_of_string(self):
     self.legstr=0
     for i in leg:
         self.legstr+=1
     print("Length of string  " , self.legstr)

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
