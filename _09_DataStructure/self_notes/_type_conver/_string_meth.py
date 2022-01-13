"""
% ---->>>	Format - Performs String formatting


Format Symbol	    Conversion
=============      ===========
%c	                character
%s	                string conversion via str() prior to formatting
%i                  signed decimal integer
%d	                signed decimal integer
%u	                unsigned decimal integer
%o	                octal integer
%x	                hexadecimal integer (lowercase letters)
%X	                hexadecimal integer (UPPERcase letters)
%e                 	exponential notation (with lowercase 'e')
%E	                exponential notation (with UPPERcase 'E')



"""

print("my name is %s and my height %d : " %("rinky" , 7))   #my name is rinky and my height 7 :








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
string = "hi"

print(string.center(15,"*")) #******hii******

print(string.center(15)) #     hii

print(string.center(10 , "-"))


#print(string.center(10 , "-_"))

#print(string.center(15,"**"))

"""
we can use only one fillchar if we use more than that it through error

    print(string.center(15,"**"))
TypeError: The fill character must be exactly one character long
"""

"""
If length of the string is greater that width then string return without padding.
"""


string  = "Im learning python"
print(string.center(5,"*"))    #Im learning python


"""
The center() through an TypeError whenever we ddint provide width:
"""

string = "Rinky"
print(string.center())   #TypeError: center expected at least 1 argument, got 0














