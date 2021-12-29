import datetime
x = datetime.datetime.now()
print("Current date and time" ,x)   #2021-12-29 11:01:39.664509

print("current year" , x.year) #2021
print(" Day ", x.strftime("%A"))  #Wednesday



"""
Creating Date Objects
To create a date, we can use the datetime() class (constructor) of the datetime module.

The datetime() class requires three parameters to create a date: year, month, day.

"""

x = datetime.datetime(2020, 5, 17 , 20 ,40,12,42)

print(" Object of date time : ",x) # 2020-05-17 20:40:12.000042



x = datetime.datetime(2020, 5, 17 , 20 ,40,12)

print(" Object of date time : ",x)   #2020-05-17 20:40:12



x = datetime.datetime(2020, 5, 17 , 20 ,40)
print(" Object of date time : ",x)  #2020-05-17 20:40:00



x = datetime.datetime(2020, 5, 17 , 20 )   #2020-05-17 20:00:00
print(" Object of date time : ",x)



x = datetime.datetime(2020, 5, 17)
print(" Object of date time : ",x)  #2020-05-17 00:00:00



x = datetime.datetime(2020, 5)

print(" Object of date time : ",x)   #function missing required argument 'day' (pos 3)