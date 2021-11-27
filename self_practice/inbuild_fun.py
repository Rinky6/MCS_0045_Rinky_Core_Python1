''' zip() - The Python zip() function accepts iterable items and merges them into a single tuple.
 The resultant value is a zip object that stores pairs of iterables. You can pass lists, tuples, sets,
 or dictionaries through the zip() function.
'''

zip_lst=[1,2,'sal',4,5]
zip_lst1=['MCS','Rinky','48000','S/W','Python']
final_zip_lst=zip(zip_lst,zip_lst1)
print("After zipping : ",final_zip_lst)
print("After zipping using list : ",list(final_zip_lst))

zip_lst,zip_lst1=zip(final_zip_lst)
print("After unzipping : ", zip_lst,zip_lst1)




zip_lst=(1,2,'sal',4,5)
zip_lst1=('MCS','Rinky','48000','S/W','Python')
final_zip_lst=zip(zip_lst,zip_lst1)
print("After zipping using set: ",set(final_zip_lst))

zip_lst={1,2,'sal',4,5}
zip_lst1={'MCS','Rinky','48000','S/W','Python'}

final_zip_lst=zip(zip_lst,zip_lst1)
print("After zipping using dic : ", dict(final_zip_lst))


zip_lst=(1,2,'sal',4,5)
zip_lst1=('MCS','Rinky','48000','S/W','Python')

final_zip_lst=zip(zip_lst,zip_lst1)
print("After zipping using tuple : ",tuple(final_zip_lst))


for i,j in zip(zip_lst,zip_lst1):
    print("iterate using for loop :", i,j)





