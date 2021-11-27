amt = float(input("Enter Amount"))
r = 0.04
total_amt=0
total_amt1=0
total_amt2=0
yr=int(input("Enter yours"))

if yr==1:
  total_amt = amt + amt * 0.04
elif yr==2:
  total_amt1 = total_amt + total_amt * 0.04
else:
  total_amt2 = total_amt1+total_amt1*0.04
print("Total amount in account after adding interest after 1 year ", round(total_amt, 2))
print("Total amount in account after adding interest after 2 years ", round(total_amt1, 2))
print("Total amount in account after adding interest after 3 years ", round(total_amt2, 2))







