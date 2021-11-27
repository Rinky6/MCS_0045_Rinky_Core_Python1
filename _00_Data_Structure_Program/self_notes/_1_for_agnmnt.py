'''

name=input('Enter your name : ')
e_id=int(input("Enter emp id : "))
mno=int(input("Enter months : "))
net_amount1=0
net_amount=[]
total_amt=0
total=0
if mno>=1:
  for i in range(mno):
    print("Enter amount for", )
    basic=int(input("Enter basic salary amount : "))
    special=int(input("Enter special salary amount : "))
    hs = int(input("Enter hs salary amount : "))
    tax=int(input("Enter tax:  "))
    total=(basic+special+hs)-tax
    net_amount.append(total)
total_amt=sum(net_amount)

sum1=[]
n = input("Do you have any expd")
if n == 'yes':
 exp = int(input("Enter no of exped"))
 for j in range(exp):

      print("What type of expd u having")
      rent=float(input("Enter amount"))
      shopping=float(input("Enter  amount"))
      food= float(input("Enter amount"))
      sm=rent+shopping+food
      sum1.append(sm)
else:
 print("I dont have any expd so I want to quit")
print("Total amount I have : ",total_amt)
total_expd=sum(sum1)
print("total expd ", total_expd)
net_saving = total_amt-total_expd
if net_saving>=1:
    print("you are great")
else:
    print("you are looser")

'''
'''

name=input('Enter your name : ')
e_id=int(input("Enter emp id : "))
mno=int(input("Enter months : "))
net_amount1=0
net_amount=[]
total_amt=0
total=0
if mno>=1:
  for i in range(mno):
    print("Enter amount for", )
    basic=int(input("Enter basic salary amount : "))
    special=int(input("Enter special salary amount : "))
    hs = int(input("Enter hs salary amount : "))
    tax=int(input("Enter tax:  "))
    total=(basic+special+hs)-tax
    net_amount.append(total)
total_amt=sum(net_amount)
'''
sum1=[]
expd_lst=[]
n = input("Do you have any expd")
if n == 'yes':
  while True:
    exp_n     = int(input("Enter name of exped"))
    expd_lst.append(exp_n)
    for j in range(expd_lst):
      print("What type of expd u having")
      rent=float(input("Enter amount"))
      shopping=float(input("Enter  amount"))
      food= float(input("Enter amount"))
      sm=rent+shopping+food
      sum1.append(sm)
else:
 print("I dont have any expd so I want to quit")
#print("Total amount I h    ave : ",total_amt)
total_expd=sum(sum1)
print("total expd ", total_expd)
net_saving = total_amt-total_expd
if net_saving>=1:
           print("you are great")
else:
    print("you are looser")
