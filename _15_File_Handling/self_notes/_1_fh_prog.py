with open("text.txt" , 'r') as file:
    data = file.read()
    print(data)



with open("text.txt", "r") as file:
    data = file.readlines()
    for line in data:
        word = line.split()
        print (word)





with open("text.txt", "r") as file:
    data = file.readlines()
    for line in data:
        word = line.split()
        print(word)





with open("text.txt", "w") as file:
    data = file.write(" this is write block")
    print(data)
   

''' for line in data:
        word = line.split()
    print (word)
'''