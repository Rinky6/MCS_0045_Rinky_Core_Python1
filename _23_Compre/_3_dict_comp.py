


lst = [1,2,3,4,5,6,7,8,9]
dic_out = {}
for i in lst:
    if i%2==0:
     dic_out[i] = i ** 3
print("After operation : " , dic_out)



lst = [1,2,3,4,5,6,7,8,9]
dic_op ={ i : i ** 3 for i in lst if i%2 == 0}
print("After operation : " ,dic_op)



state = ['Karnataka' , 'Telangana' , 'Jharkhand' , 'Maharashra']
city = ['Bangaluru', 'Hydrabad', 'Ranchi' , 'Mumbai']
dic_op = {key : val for key, val in zip(state,city)}
print("After operation : ", dic_op)





data = {"id" : 101 ,
         "name" : "Rinky",
         "sal" : 85000,
         "dept": "testing"}
print("information of emp", data)
del data["dept"]
print("information of emp", data)

data["dept"] = "development"
print("information of emp", data)

data["dob"] = "11/10/2020"

print(data)




