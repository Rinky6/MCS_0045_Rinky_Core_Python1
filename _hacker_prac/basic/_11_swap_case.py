"""
You are given a string and your task is to swap cases. In other words, convert all lowercase
letters to uppercase letters and vice versa.

For Example:

Www.HackerRank.com → wWW.hACKERrANK.COM
Pythonist 2 → pYTHONIST 2

"""


def swap_case(s):
    num = ""
    for let in s:
        if let.isupper() == True:
            num+=(let.lower())
        else:
            num+=(let.upper())
    return num
s = input("Enter the String")
result = swap_case(s)
print(result)