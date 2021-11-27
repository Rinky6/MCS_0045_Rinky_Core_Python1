import itertools

var = input("Enter your  no : ")

lst = []
if var.isdigit():
    var = int(var)
    print(var)
    for i in range(0, var + 1):
        lst.append(i)
    print(lst)

    crs_pdct = list(itertools.product(lst, lst))
    print(crs_pdct)

    crs_pdct1 = []
    for i in crs_pdct:
        if sum(i) == 7:

            tuple1 = tuple(sorted(list(i)))
            if tuple1 not in crs_pdct1:
             print(tuple1)
             crs_pdct1.append(tuple1)
    print(crs_pdct1)



else:
    print("Enter only integer value")




'''
var=input("Enter your  no : ")

res=[]
res1=()
if var.isdigit() == True:
    var=int(var)
    print(var)

    for i in range(0,var+1):
        for j in range (0,var+1):
            if i + j == 7:
                tuple1 = tuple(sorted([i, j]))
                if tuple1 not in res:
                    res.append(tuple1)
                res1=tuple(res)
    print(res1)

else:
    print("Enter only integer value")

'''