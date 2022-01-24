sen = input("Enter sentence : ")
word = sen.split()
for i in range(len(word)):
    word[i] = word[i].lower()
s =" ".join(word)
print(s)