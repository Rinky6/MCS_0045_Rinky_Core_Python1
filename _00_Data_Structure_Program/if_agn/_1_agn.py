'''

take 6 subjects from theuser
if he scores more than 90% distinction must and should in three subjects he get 90%
a=90
b=90
c=92
res=90 distinction
95% distinction +gold

a student will be awarded he scores between 75 to 90 in all subjects average
< 75 fail

'''
'''
msub1=float(input("Enter 1st subject marks"))
msub2=float(input("Enter 1st subject marks"))
msub2=float(input("Enter 1st subject marks"))
msub3=float(input("Enter 1st subject marks"))
msub4=float(input("Enter 1st subject marks"))
msub5=float(input("Enter 1st subject marks"))
msub6=float(input("Enter 1st subject marks"))
lst =[msub1,msub2,msub3,msub4,msub5,msub6]
print(lst)
lst1=[]
for i in lst:

    if i>95:
     lst1.append(i)

print(lst1)
print("distinction +gold")


'''



lst=[]
for i in range (1,7):
    marks=float(input("Enter the marks"))
    lst.append(marks)
    lst.sort()
print(lst)

if lst[3]>=95 and  lst[4]>=95 and lst[5]>=95:
    print(" gold")



avg= sum(lst)/6
print(avg)

if avg>=90 and avg<95:

    print("dic")

elif avg<90 and avg >=75:

    print("Average")
elif avg<75:

    print("Fail")

















"""
num = input("Enter the number"))
if num == int:
    print("This is Integer")
else:
    print("Enter valid input")
n1 = int(input("Enter a range"))
n2 = int(input("Enter a range"))
list1 = [i for i in range(n1, n2)]
list2 = []
for i in list1:
    for j in list1:
        if i + j == num:
            if i <= num/2:
                a = i, j
                tuple(a)
                list2.append(a)
 print(list2)

"""