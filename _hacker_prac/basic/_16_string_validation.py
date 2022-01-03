"""
You are given a string S.

Your task is to find out if the string S contains: alphanumeric characters,
alphabetical characters, digits, lowercase and uppercase characters.



str.isalnum()
==============
This method checks if all the characters of a string are alphanumeric (a-z, A-Z and 0-9).


str.isalpha()
==============
This method checks if all the characters of a string are alphabetical (a-z and A-Z).

str.isdigit()
=============
This method checks if all the characters of a string are digits (0-9).

str.islower()
=============

This method checks if all the characters of a string are lowercase characters (a-z).


str.isupper()
=============

This method checks if all the characters of a string are uppercase characters (A-Z).


"""

s = input("Enter the string : ")
print(any(map(str.isalnum, s)))
print(any(map(str.isalpha, s)))
print(any(map(str.isdigit, s)))
print(any(map(str.islower, s)))
print(any(map(str.isupper, s)))