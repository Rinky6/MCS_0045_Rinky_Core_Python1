"""
In this challenge, the user enters a string and a substring. You have to print the number
of times that the substring occurs in the given string. String traversal will take place
from left to right, not from right to left.

NOTE: String letters are case-sensitive.


st = input("Enter the string : ")
for i in ( st):
    print (i)

"""
def count_substring(string, sub_string):
    count = 0
    for i in range(0, len(string) - len(sub_string) + 1):

        if string[i] == sub_string[0]:
            flag = 1
            for j in range(0, len(sub_string)):
                print(string[i + j])
                print("  ",sub_string[j])

                if string[i + j] != sub_string[j]:
                    flag = 0
                    break
            if flag == 1:
                count += 1
    return count

string = input("Enter string : ").strip()
sub_string = input("enter sub string : ").strip()

count = count_substring(string, sub_string)
print(count)