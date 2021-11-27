# Python program to shuffle a deck of card




import time

list1 = [i for i in range(1,14)]
list2 = [i for i in range(1,14)]
list3 = [i for i in range(1,14)]
list4 = [i for i in range(1,14)]

def rand_val(y):
   random=int(time.time()**2)
   random//=2
   random %=y
   return random

def sum_list(l):
    sum = 0
    for i in l:
        sum += i
    return sum

list5 = list1+list2+list3+list4
print(list5)
list6 = []
while len(list5)>0:
    a = rand_val(len(list5))
    list6.append(list5[a])
    del list5[a]
print(list6)
player_1 = []
player_2 = []
run = 0
while run < 26:
    a = rand_val(len(list6))
    player_1.append(list6[a])
    del list6[a]
    b = rand_val(len(list6))
    player_2.append(list6[b])
    del list6[b]
    run += 1

sum_player1 = sum_list(player_1)
sum_player2 = sum_list(player_2)

if sum_player1 > sum_player2:
    print(f"Player 1 is the Winner with point {sum_player1}")
else:
    print(f"Player 2 is the Winner with point {sum_player2}")









# importing modules
'''
import itertools, random

# make a deck of cards
deck = list(itertools.product(range(1,14),['Spade','Heart','Diamond','Club']))
#print("value of deck : ", deck)
#deck = list(itertools.product(["A","2","3","4","5","6","7","8","9","10","J","Q","K"],['Spade','Heart','Diamond','Club']))

print("value of deck : ", deck)
# shuffle the cards
random.shuffle(deck)

def players1(n):
  for i in range(n):
     print("player1 :", deck[i][0],deck[i][1])
     deck.remove(deck[i])

def players2(n):
     for j in range(n):
        print("player2 :", deck[j][0], deck[j][1])
        deck.remove(deck[j])
players1(2)
players2(2)

'''

'''
suits = ["Diamonds", "Spades", "Hearts", "Clubs"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

def create_deck():
    deck = set()
    j = ranks.index("Jack")
    ranks[j] = 11
    q = ranks.index("Queen")
    ranks[q] = 12
    k = ranks.index("King")
    ranks[k] = 13
    a = ranks.index("Ace")
    ranks[a] = 14
    for suite in suits:
        for rank in ranks:
            print("Rank is  " , rank)
            print("suite is ", rank)
           # suite_cards ={{rank} ,{suite}}
    for suite, rank in zip([i for i in suits[0: 4]], [j for j in ranks[26:]]):
               print("Suite is " , suite)
               print("rank is ", rank)
            # suite_cards = {f'The {rank} of {suite}' for rank in ranks}
           # deck.update(suite_cards)
    print("deck", deck)

    #return deck


def main():
    deck = create_deck()

    playerA = []
    playerB = []
    fst = input('Enter the player name who want to play 1st i.e. A or B:')
    if fst == 'A':
        for i, j in zip([i for i in deck[0: 26]], [j for j in deck[26:]]):
            playerA.append(i)
            playerA.append(j)

    elif fst == 'B':
        for i, j in zip([i for i in deck[0: 26]], [j for j in deck[26:]]):
            playerA.append(j)
            playerA.append(i)

    print("Player 1 : ", playerA)
    print("Player 1 : ", playerB)


main()



    players = int(input("How many players?"))
for index in range(1, players + 1):
 print(f"\nplayer {index}:")
 for _ in range(5):
     print(deck.pop())'''

'''

values_dict = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'K': 12, 'Q': 13,
               'A': 14}
total_dict = {}
shapes_dict = {'D': 4, 'H': 3, 'S': 2, 'C': 1}
deck = {}

for i in shapes_dict.keys():
    for j in values_dict.keys():
        deck[j + i] = values_dict[j] + shapes_dict[i]
    print("deck : ", deck)

for i, j in deck.items():
    print(i, ' : ', j)

cards = set(deck.keys())

cards_list = list(cards)
print("print :" , cards_list)

player_A_cards = []
player_B_cards = []

first = input('enter which player starts first, enter A or B :')
if first == 'A':
    for i, j in zip([i for i in cards_list[0: 26]], [j for j in cards_list[26:]]):
        player_A_cards.append(i)
        player_B_cards.append(j)

elif first == 'B':
    for i, j in zip([i for i in cards_list[0: 26]], [j for j in cards_list[26:]]):
        player_A_cards.append(j)
        player_B_cards.append(i)

print(f'\n-----------player A cards are-----------\n {player_A_cards}')
print(f'\n-----------player B cards are-----------\n {player_B_cards}')

player_A_count = 0
player_B_count = 0

for i in player_A_cards:
    player_A_count += deck[i]

for j in player_B_cards:
    player_B_count += deck[j]

if player_A_count > player_B_count:
    print('player A count is :', player_A_count)
    print('player B count is : ', player_B_count)
    print('player A wins')

elif player_A_count < player_B_count:
    print('player A count is :', player_A_count)
    print('player B count is : ', player_B_count)
    print('player B wins')

else:
    print('player A count is :', player_A_count)
    print('player B count is : ', player_B_count)
    print('the count is equal')
'''