class WithdrawException(Exception):
    pass

try:

    amount = int(input("Enter amount how much you want to withdraw"))
    print("Your enter amount : ", amount)
    if amount==100 or amount==200 or amount==500 or amount==2000 or amount%500==0:
     print(" your Withdraw amount : ", amount)
    else:
     raise WithdrawException(amount)
except WithdrawException as e:
   print("Please enter  amount multiply of 100 ")
else:
    print("else block execute")
finally:
    print("Your transaction process completed")