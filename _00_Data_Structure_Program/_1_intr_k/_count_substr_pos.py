string = 'malayalam'
sub_string = 'a'
length = len(sub_string)
for i in range(len(string)):
    if string[i :i + length] == sub_string:
        print(string[i :i + length] ,i)




