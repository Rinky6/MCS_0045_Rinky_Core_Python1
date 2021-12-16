

fileptr = open("file2.txt", "w")

# appending the content to the file
fileptr.write('''Python is the modern day language. It makes things so simple.
     It is the fastest-growing programing language''')

# closing the opened the file
fileptr.close()

'''

f_open = open("text.txt", 'r')
print(f_open.read())  # read all content



f_open = open("text.txt", 'r')
print(f_open.readline())    # read first line

f = open("myfile.txt", "x")
print("file created")

f = open("myfile.txt", "w")
print(f.writelines("After creation file"))



f_open = open("text.txt", 'r')
print(f_open.readline())



f_write=open("text.txt", 'w')
print(f_write.write("Write the content"))   #17f_write=open("text.txt", 'w')
print(f_write.write("Write the content 1"))




import os
os.remove("myfile.txt")


#Check if file exists, then delete it:
import os
if os.path.exists("myfile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")
  
'''



with open("file2.txt") as f:
	size = 10
	content = f.read(size)

	while len(content) > 0:
		print(content, end = '*')
		content = f.read(size)
"""
output : Python is *the modern* day langu*age. It ma*kes things* so simple*.
     It *is the fas*test-growi*ng program*ing langua*ge*
"""





