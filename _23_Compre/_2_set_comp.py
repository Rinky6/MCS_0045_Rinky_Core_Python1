lst = [1,2,3,4,5,6,7,8,9]
st = set()
for i in lst:
    if i % 2 == 0:
        st.add(i)
print("After operation : ", st)


#lst = [1,2,3,4,5,6,7,8,9,]
st1 = {i for i in lst if i%2 == 0}
print("After operation : ", st1)





fruits = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for i in sorted(fruits):
  print(i)


for i in sorted(set(fruits)):
    print("After sorted : ", i)



