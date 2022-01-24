"""
Method           	Description
clear()     	    Removes all items from the dictionary.
copy()	            Returns a shallow copy of the dictionary.
fromkeys(seq[, v])	Returns a new dictionary with keys from seq and value equal to v (defaults to None).
get(key[,d])	    Returns the value of the key. If the key does not exist, returns
                    d (defaults to None).
items()	            Return a new object of the dictionary's items in (key, value) format.
keys()  	        Returns a new object of the dictionary's keys.
pop(key[,d])    	Removes the item with the key and returns its value or d if key is not found.
                    If d is not provided and the key is not found, it raises KeyError.
popitem()	        Removes and returns an arbitrary item (key, value). Raises KeyError if
                    the dictionary is empty.
setdefault(key[,d])	Returns the corresponding value if the key is in the dictionary. If not,
                    inserts the key with a value of d and returns d (defaults to None).
update([other])    	Updates the dictionary with the key/value pairs from other, overwriting
                    existing keys.
values()	        Returns a new object of the dictionary's values











all()	        Return True if all keys of the dictionary are True (or if the dictionary is empty).
any()	        Return True if any key of the dictionary is true. If the dictionary is empty,
                return False.
len()	        Return the length (the number of items) in the dictionary.
cmp()	        Compares items of two dictionaries. (Not available in Python 3)
sorted()    	Return a new sorted list of keys in the dictionary.

"""
data={"name" : "Rinky","age": 45, "edu": [10,12,"BCA","MCA"],"sal":45000 }
print(data)
data1 ={}
print(data1.fromkeys("n15k" , "rinky")) #{'n': 'rinky', '1': 'rinky', '5': 'rinky', 'k': 'rinky'}



marks = {}.fromkeys(['Math', 'English', 'Science'], 95)
print(marks)  #{'Math': 95, 'English': 95, 'Science': 95}


print(data["edu"]) #[10, 12, 'BCA', 'MCA']

print(data["edu"][1])# 12
#print(data["eid"])#KeyError: 'eid'
print(data.get("eid")) #None
print(data.get("name","sal")) #Rinky





print(sorted(data.items())) #[('age', 45), ('edu', [10, 12, 'BCA', 'MCA']), ('name', 'Rinky'), ('sal', 45000)]

