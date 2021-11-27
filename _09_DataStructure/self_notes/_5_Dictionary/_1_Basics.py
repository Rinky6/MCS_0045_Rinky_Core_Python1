#Dictionary
"""
Dictionaries are used to store data values in key:value pairs.

A dictionary is a collection which is ordered*, changeable and does not allow duplicates.

Dictionaries are written with curly brackets, and have keys and values:

Example
Create and print a dictionary:

data = {
             "e_no": "mcs_001",
             "e_name": "Rummy",
             "sal": 350000
           }
print(data)


Dictionary Items
=================
Dictionary items are ordered, changeable, and does not allow duplicates.

Dictionary items are presented in key:value pairs, and can be referred to by using the key name.

Example
Print the "e_name" value of the dictionary:
data = {
             "e_no": "mcs_001",
             "e_name": "Rummy",
             "sal": 350000
           }
print(data["e_name"])


dictionary DS does not allow the duplicate key,but the values can be duplicate
ex.
data = { "e_no" : 101
         "e_name" : "Ravi"
         "sal" :  58000
          "ename" : "shyama"  # error
          }

data = { "e_no" : 101
         "e_name" : "Ravi"
         "sal" :  58000
          "e_no" :102  # error
          }

Dictionary Length
-------------------
To determine how many items a dictionary has, use the len() function:

Example
Print the number of items in the dictionary:

print(len(data))

Dictionary Items - Data Types
The values in dictionary items can be of any data type:

Example
String, int, boolean, and list data types:

           dict = {
                "brand": "Ford",
                "electric": False,
                "year": 1964,
                "colors": ["red", "white", "blue"]
                 }






"""
