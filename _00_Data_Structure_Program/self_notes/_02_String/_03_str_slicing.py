# P01. REQ : String slicing

'''
1. CRUD
2. STATE      - Data types/structures
3. BEHAVIOR   - DTS / Operators / DM or Loops
'''
'''
1. CRUD       -->  Retrieval
2. STATE      -->  string 
3. BEHAVIOR   -->   int | =             
'''

# 0. Mathematics 80%
'''
1. Define the string 
2. Start reading it. 
3. Specify the start index and the end index, separated by a colon, to return a part of the string
'''

# 1.Builtin functions 80%

print("-----1. Builtin Functions--------")

message = 'This is my first program'  # static way# String slicing
# Using slice constructor

s1 = slice(3)
s2 = slice(1, 5, 2)
s3 = slice(-1, -12, -2)
print("String slicing")
print(message[2:5])    #is
print(message[2:6])     #is i
print(message[s1])     #Thi
print(message[s2])     #hs
print(message[s3])     #meoptr


# 2. Algorithm  80%

print("--------2. Algorithm----------")

msg = 'Using Algorithm'
print(msg[1:8])


# 3 Using Functions  ==> 50 programs
print("--------3 Using Functions----------")
print("--------Without return type----------")
message = 'This is using function'
def slc(msg):

    print(msg[0:8])

slc(message)

print("--------With return type----------")
#State
message=input("Enter String  ")

def slc(msg):

    return msg[0:8]

strslc=slc(message)
print("After slicing the string  "  , strslc)




# 4 OOPS              ==> 30 programs
print("--------4 Object Oriented----------")
class Slc_String:
    def __init__(self,str):
     self.str=str
    def leg_of_string(self):

     print("After Slicing the string  " , self.str[2:6])

leg=input("Enter a string   ")
length=Slc_String(leg)
length.leg_of_string()




# 5 Exception handling  ==> 15 programs
print("--------5 Exception handling----------")

# 6 File Handling  ==> 10 programs
print("--------6 File Handling----------")

# 7 Database interaction MVC  ==> 5 programs
print("--------7 Database interaction----------")



# 8 UI Interaction   ==> 3 programs
print("--------8 UI Interaction----------")
