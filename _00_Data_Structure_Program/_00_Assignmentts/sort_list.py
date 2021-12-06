''''
I/P
list =[1,2,3,"MCS",4,"Software",5,Python",6]

O/P
list=["MCS","Software","Python",1,2,3,4,5,6]
'''
'''def srt(lst):
 num=[]
 str=[]
 for i in lst:
      if type(i)== int:
       num.append(i)
      else:
         str.append(i)
 flist= num + str
 return flist
list =[1,2,3,"MCS",4,"Software",5,"Python",6]
final_list=srt(list)
print("final list :",final_list)'''

'''
I/P
str1 = "abc"
str2="defg"          
O/P
adbecfg
'''

'''str1 = "abc"
str2="defg"
#adbecfg
str= str1[0]+str2[0]
fstr= str+str1[1]+str2[1]+str1[2]+str2[2]+str2[3]
print(fstr)
#adbecfg
print(str)
fstr=[]
for str in zip(str1,str2):
    fstr.append(str)
    print(fstr)'''

'''chars = "karnataka"
for char in chars:
  count = chars.count(char)
  if count > 1:
   print (char,count)'''

'''list = ['apple', 'mango', 'cherry']

lst = [x.upper() for x in list]

# printing output
print(lst)'''

data = {'Ram':23, 'Shyam':8, 'Seeta': 75, 'Ramesh' : 85}
key=(lambda k: data[k])
print(key)

max_value = max(data.keys(), key=(lambda k: data[k]))
min_value = min(data.keys(), key=(lambda k: data[k]))

print('Maximum Value: ',data[max_value])
print('Minimum Value: ',data[min_value])

'''from collections import Counter

data = {'A': 67, 'B': 23, 'C': 45,
           'D': 56, 'E': 12, 'F': 69}

k = Counter(data)
high = k.most_common(3)

print("Initial Dictionary:")
print(data, "\n")

print("Dictionary with 3 highest values:")
print("Keys: Values")

for i in high:
    print(i[0], " :", i[1], " ")'''









