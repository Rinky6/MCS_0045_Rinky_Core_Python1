"""
Raghu is a shoe shop owner. His shop has X number of shoes.

He has a list containing the size of each shoe he has in his shop.

There are N number of customers who are willing to pay xi amount of money only
if they get the shoe of their desired size.

Your task is to compute how much money Raghu earned.


from collections import Counter
numShoes = int(input("Entet shoes no : "))
shoes = Counter(map(int, input("count the no of shoe").split()))
print(shoes)
numCust = int(input("enter total no of customer"))
income = 0
for i in range(numCust):
     size = map(int, input("enter size of shoes").split())
     print(size)
     price = map(int, input("price of shoes").split())
     print(price)
     income += price
     shoes[size] -= 1

 #if shoes[size]:

print("Total income : ",income)

"""
