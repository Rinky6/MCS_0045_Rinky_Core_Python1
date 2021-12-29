def minion(string):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    stuart_score = 0
    kevin_score = 0
    kevin_words = []
    stuart_words = []

    for i in range(len(string)):

        if string[i] not in vowels:
            temp = string[i:]
            print("temp", temp)
            # this count the combinations based on the count like for 'hell' it takes h, he, hel, hell
            stuart_score += len(string[i:])
            print("stuart_score" , stuart_score)
            for i in range(len(temp)):
                stuart_words.append(temp[0: i + 1])
                print(stuart_words)


        elif string[i] in vowels:
            temp = string[i:]
            # this count the combinations based on the count like for 'hell' it takes h, he, hel, hell
            kevin_score += len(string[i:])
            for i in range(len(temp)):
                kevin_words.append(temp[0: i + 1])

    print('stuart score is :', stuart_score)
    print('stuart combination words :', stuart_words)
    print('kevin score is : ', kevin_score)
    print('kevin combination words :', kevin_words)

    if stuart_score > kevin_score:
        print('\nstuart wins')

    elif stuart_score < kevin_score:
        print('\nkevin wins')

    else:
        print('\nboth wins')


minion(input('enter the string : '))