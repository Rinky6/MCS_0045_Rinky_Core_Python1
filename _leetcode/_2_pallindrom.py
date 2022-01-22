"""
Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward.

For example, 121 is a palindrome while 123 is not.


Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.


Constraints:

-231 <= x <= 231 - 1

"""




'''

def check(n):
    r = ""
    temp = n
    if n >0:
        while n > 0:
            r1 = n % 10

            r = str(r1) + r

            n = n//10
        if temp == r:
          print("true")

    else:
        print("false")

n = int(input("Enter the integer no : "))

check(n)

'''
def isPalindrome(x):
 return str(x) == str(x)[::-1]
print(isPalindrome(-121))