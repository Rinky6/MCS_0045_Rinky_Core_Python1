"""
Task
You are given n words. Some words may repeat. For each word, output its number of occurrences.
The output order should correspond with the input order of appearance of the word.
 See the sample input/output for clarification.

Note: Each input line ends with a “\n” character.

Constraints
1 <= n <= 105
The sum of the lengths of all the words do not exceed 106
All the words are composed of lowercase English letters only.
Input Format
The first line contains the integer, n.
The next n lines each contain a word.

Output Format
Output 2 lines.
On the first line, output the number of distinct words from the input.
On the second line, output the number of occurrences for each distinct word according to their appearance in the input.

Sample Input

4
bcdef
abcdefg
bcde
bcdef
Sample Output

3
2 1 1
Explanation

There are 3 distinct words. Here, “bcdef” appears twice in the input at the first and
last positions. The other words appear once each. The order of the first appearances are
“bcdef”, “abcdefg” and “bcde” which corresponds to the output.

"""

from collections import OrderedDict
op = OrderedDict()
n = int(input("Enter how many words you want to enter : "))
for i in range(n):
    ip=input("Enter words : ")
    if ip not in op:
        op[ip] = 1
    else:
        op[ip] += 1
print(len(op))
print(*op.values())

"""
for i in range(1,int(input())):
    print(((10**(i)//9)*i))
    
    
    
5
1
22
333
4444    
"""