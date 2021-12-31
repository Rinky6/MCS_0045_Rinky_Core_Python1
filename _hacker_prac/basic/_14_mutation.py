"""
Read a given string, change the character at a given index and then print the modified string.
"""
st = input("Enter the String : ")
lst = list(st)
inx=int(input("Enter index where you want to modify : "))
ch=input("enter character which one you want to enter : ")
lst[inx]= ch
print(lst)
st = ''.join(lst)
print("converting : ",st)

'''
st=st[:4]+"h"+st[5:]
print("using slicing : ",st)
'''

"""

def mutate_string(string, position, character):
    n = list(string)
    n[position] = character
    string = "".join(n)
    return string
s = input()
i, c = input().split()
s_new = mutate_string(s, int(i), c)
print(s_new)


"""