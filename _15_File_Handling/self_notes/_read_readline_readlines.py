'''Example 1: Reading lines using readline() function'''


#open the file.txt in read mode. causes error if no such file exists.
fileptr = open("file2.txt","r");
#stores all the data of the file into the variable content
content = fileptr.readline()
content1 = fileptr.readline()
#prints the content of the file
print("first content output : ", content)   #first content output :  Python is the modern day language. It makes things so simple.
print("second content output : ",content1)     #second content output :        It is the fastest-growing programing language
#closes the opened file
fileptr.close()

'''Example2: Reading Lines Using readlines() function'''

# open the file.txt in read mode. causes error if no such file exists.
fileptr = open("file2.txt", "r");

# stores all the data of the file into the variable content
content = fileptr.readlines()

# prints the content of the file
print("content output : " , content)

# closes the opened file
fileptr.close()