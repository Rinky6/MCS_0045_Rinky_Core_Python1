
#String method
#capitalize(): it doesn't take parameter ,it simply convert a first character in capital
# it doesn't change the original string

s = "rinky kumari "
sj  = ""
for i in s[:].split():
     si = i.capitalize()
     print(si + " " , end = "")


print("\n-----------------------")
s = "10rinky kumari"

sj  = ""
for i in s[:].split():
     si = i.capitalize()
     print(si + " " , end = "")

"""
If we start with any string with number the capitalize() is skip the that string.

"""



"""
center:
The center() method retuns a string which is padded with the specified character.
syntax : string.center(width[, fillchar])
The center() takes 2 arguments : 
width : lenth of the string with padded character
fillchar(optional) : padding character. The fillchar argument is optional. if not provided 
space is take as default argument. for fillchar we can give any character like %, & (,), etc.

"""

print("\n --------------")
string = "hii"

print(string.center(15,"*")) #******hii******

print(string.center(15)) #     hii









