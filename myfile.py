from math import comb

n = 65675
m = 6768769
k = 478

sum = 0
for i in range(1,k+1):
    sum += comb(n,i)
print(sum*m)