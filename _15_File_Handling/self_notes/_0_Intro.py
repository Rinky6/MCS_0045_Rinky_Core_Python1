
f_open = open("text.txt", 'r')
print(f_open.read())  # read all content



f_open = open("text.txt", 'r')
print(f_open.readline())    # read first line

'''
f = open("myfile.txt", "x")
print("file created")

f = open("myfile.txt", "w")
print(f.writelines("After creation file"))

'''

f_open = open("text.txt", 'r')
print(f_open.readline())



f_write=open("text.txt", 'w')
print(f_write.write("Write the content"))   #17f_write=open("text.txt", 'w')
print(f_write.write("Write the content 1"))



'''
import os
os.remove("myfile.txt")
'''

#Check if file exists, then delete it:
import os
if os.path.exists("myfile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")