"""
Python Regular Expressions The regular expressions can be defined as the sequence of characters which are used to
search for a pattern in a string. The module re provides the support to use regex in the python program. The re
module throws an exception if there is some error while using the regular expression.

The re module must be imported to use the regex functionalities in python.

"""
'''
import re


Regex Functions
The following regex functions are used in the python.

SN	Function	Description
1	match	  This method matches the regex pattern in the string with the optional flag. It returns true if a match is 
                    found in the string otherwise it returns false.
2	search	  This method returns the match object if there is a match found in the string.
3	findall	  It returns a list that contains all the matches of a pattern in the string.
4	split	  Returns a list in which the string has been split in each match.
5	sub	      Replace one or many matches in the string.


Forming a regular expression
A regular expression can be formed by using the mix of meta-characters, special sequences, and sets.

Meta-Characters
Metacharacter is a character with the specified meaning.

Metacharacter	Description	                                             Example
[]	It represents the set of characters.	                             "[a-z]"
\	It represents the special sequence.                                  "\r"
.	It signals that any character is present at some specific place. 	 "Ja.v."
^	It represents the pattern present at the beginning of the string.	 "^Java"
$	It represents the pattern present at the end of the string.	         "point"
*	It represents zero or more occurrences of a pattern in the string.	 "hello*"
+	It represents one or more occurrences of a pattern in the string.	 "hello+"
{}	The specified number of occurrences of a pattern the string.	     "java{2}"
|	It represents either this or that character is present.	             "java|point"
()	Capture and group


Special Sequences
Special sequences are the sequences containing \ followed by one of the characters.

Character	Description
\A	         It returns a match if the specified characters are present at the beginning of the string.
\b	         It returns a match if the specified characters are present at the beginning or the end of the string.
\B	       It returns a match if the specified characters are present at the beginning of the string but not at the end.
\d	         It returns a match if the string contains digits [0-9].
\D	         It returns a match if the string doesn't contain the digits [0-9].
\s	         It returns a match if the string contains any white space character.
\S	         It returns a match if the string doesn't contain any white space character.
\w	         It returns a match if the string contains any word characters.
\W	         It returns a match if the string doesn't contain any word.
\Z  	     Returns a match if the specified characters are at the end of the string.

Sets
A set is a group of characters given inside a pair of square brackets. It represents the special meaning.

SN	Set	         Description
1	[arn]	    Returns a match if the string contains any of the specified characters in the set.
2	[a-n]	    Returns a match if the string contains any of the characters between a to n.
3	[^arn]	    Returns a match if the string contains the characters except a, r, and n.
4	[0123]	    Returns a match if the string contains any of the specified digits.
5	[0-9]	    Returns a match if the string contains any digit between 0 and 9.
6	[0-5][0-9]	Returns a match if the string contains any digit between 00 and 59.
10	[a-zA-Z]	Returns a match if the string contains any alphabet (lower-case or upper-case).



The findall() function
This method returns a list containing a list of all matches of a pattern within the string. It returns the patterns in 
the order they are found. If there are no matches, then an empty list is returned.

Consider the following example.

Example

str_1 = "How are you. How is everything"

matches = re.findall("How", str_1)

print(matches)


The match object
The match object contains the information about the search and the output. 
If there is no match found, the None object is returned.


Example
print("-------------------------------------------------------------------------------------------")

str_2 = "How are you. How is everything"

matches = re.search("How", str_2)

print(type(matches))

print(matches)  # matches is the search object


The Match object methods
There are the following methods associated with the Match object.

span(): It returns the tuple containing the starting and end position of the match.
string(): It returns a string passed into the function.
group(): The part of the string is returned where the match is found.

print("-------------------------------------------------------------------------")

str_3 = "How are you. How is everything"

matches = re.search("How", str_3)

print(matches.span())

print(matches.string)

print(matches.group())

print("-------------------------------------------------------------------------------------")

We usegroup(num) or groups() function of match object to get matched expression.

Sr.No.	Match Object Method & Description
1	    group(num=0)

        This method returns entire match (or specific subgroup num)

2	    groups()

        This method returns all matching subgroups in a tuple (empty if there weren't any)

Example
line = "Cats are smarter than dogs"

matchObj = re.match(r'(.*) are (.*?) .*', line, re.M | re.I)

if matchObj:
    print("matchObj.group() : ", matchObj.group())
    print("matchObj.group(1) : ", matchObj.group(1))
    print("matchObj.group(2) : ", matchObj.group(2))

else:
    print("No match!!")

print("---------------------------------------------------------------------------------")

# Module Regular Expression is imported
# using __import__().
import re

# compile() creates regular expression
# character class [a-e],
# which is equivalent to [abcde].
# class [abcde] will match with string with
# 'a', 'b', 'c', 'd', 'e'.
p = re.compile('[a-e]')

# findall() searches for the Regular Expression
# and return a list upon finding
print(p.findall("Aye, said Mr. Gibenson  Stark"))


Output: 

['e', 'a', 'd', 'b', 'e', 'a']
Understanding the Output: 

First occurrence is ‘e’ in “Aye” and not ‘A’, as it being Case Sensitive.
Next Occurrence is ‘a’ in “said”, then ‘d’ in “said”, followed by‘b’ and ‘e’ in “Gibenson”, the Last ‘a’ matches with 
  “Stark”.
Metacharacter backslash ‘\’ has a very important role as it signals various sequences. If the backslash is to be used 
without its special meaning as metacharacter, use’\\’


print("-------------------------------------------------------------------------")

from re import split

# '\W+' denotes Non-Alphanumeric Characters
# or group of characters Upon finding ','
# or whitespace ' ', the split(), splits the
# string from that point
print(split('\W+', 'Words, words , Words'))
print(split('\W+', "Word's words Words"))

# Here ':', ' ' ,',' are not AlphaNumeric thus,
# the point where splitting occurs
print(split('\W+', 'On 12th Jan 2016, at 11:02 AM'))

# '\d+' denotes Numeric Characters or group of
# characters Splitting occurs at '12', '2016',
# '11', '02' only
print(split('\d+', 'On 12th Jan 2016, at 11:02 AM'))

print("----------------------------------------------------------------------")

# Splitting will occurs only once, at
# '12', returned list will have length 2
print(re.split('\d+', 'On 12th Jan 2016, at 11:02 AM', 1))

# 'Boy' and 'boy' will be treated same when
# flags = re.IGNORECASE
print(re.split('[a-f]+', 'Aey, Boy oh boy, come here', flags=re.IGNORECASE))
print(re.split('[a-f]+', 'Aey, Boy oh boy, come here'))


re.sub() 
The ‘sub’ in the function stands for SubString, a certain regular expression pattern is searched in the given 
string(3rd parameter), and upon finding the substring pattern is replaced by repl(2nd parameter), count checks and 
maintains the number of times this occurs. 

Syntax:

 re.sub(pattern, repl, string, count=0, flags=0)
Example 1:

import re

# Regular Expression pattern 'ub' matches the
# string at "Subject" and "Uber". As the CASE
# has been ignored, using Flag, 'ub' should
# match twice with the string Upon matching,
# 'ub' is replaced by '~*' in "Subject", and
# in "Uber", 'Ub' is replaced.
print(re.sub('ub', '~*', 'Subject has Uber booked already',
             flags=re.IGNORECASE))

# Consider the Case Sensitivity, 'Ub' in
# "Uber", will not be reaplced.
print(re.sub('ub', '~*', 'Subject has Uber booked already'))

# As count has been given value 1, the maximum
# times replacement occurs is 1
print(re.sub('ub', '~*', 'Subject has Uber booked already',
             count=1, flags=re.IGNORECASE))

# 'r' before the pattern denotes RE, \s is for
# start and end of a String.
print(re.sub(r'\sAND\s', ' & ', 'Baked Beans And Spam',
             flags=re.IGNORECASE))


re.subn() 
subn() is similar to sub() in all ways, except in its way to providing output. It returns a tuple with count of total of
replacement and the new string rather than just the string. 

Syntax:

 re.subn(pattern, repl, string, count=0, flags=0)
Example:


print(re.subn('ub', '~*', 'Subject has Uber booked already'))

t = re.subn('ub', '~*', 'Subject has Uber booked already',
            flags=re.IGNORECASE)
print(t)
print(len(t))

# This will give same output as sub() would have
print(t[0])


re.escape()
Return string with all non-alphanumerics backslashed, this is useful if you want to match an arbitrary literal string 
that may have regular expression metacharacters in it.

Syntax:

re.escape(string)
Example:

print("--------------------------------------------------------------------------------------")
# escape() returns a string with BackSlash '\',
# before every Non-Alphanumeric Character
# In 1st case only ' ', is not alphanumeric
# In 2nd case, ' ', caret '^', '-', '[]', '\'
# are not alphanumeric
print(re.escape("This is Awesome even 1 AM"))
print(re.escape("I Asked what is this [a-9], he said \t ^WoW"))


re.search()
his method either returns None (if the pattern doesn’t match), or a re.MatchObject contains information about the 
matching part of the string. This method stops after the first match, so this is best suited for testing a regular 
expression more than extracting data.

Example: Searching an occurrence of the pattern

# A Python program to demonstrate working of re.match().
import re

# Lets use a regular expression to match a date string
# in the form of Month name followed by day number
regex = r"([a-zA-Z]+) (\d+)"

match = re.search(regex, "I was born on June 24")

if match is not None:

    # We reach here when the expression "([a-zA-Z]+) (\d+)"
    # matches the date string.

    # This will print [14, 21), since it matches at index 14
    # and ends at 21.
    print("Match at index %s, %s" % (match.start(), match.end()))

    # We us group() method to get all the matches and
    # captured groups. The groups contain the matched values.
    # In particular:
    # match.group(0) always returns the fully matched string
    # match.group(1) match.group(2), ... return the capture
    # groups in order from left to right in the input string
    # match.group() is equivalent to match.group(0)

    # So this will print "June 24"
    print("Full match: %s" % (match.group(0)))

    # So this will print "June"
    print("Month: %s" % (match.group(1)))

    # So this will print "24"
    print("Day: %s" % (match.group(2)))

else:
    print("The regex pattern does not match.")



Match Object
A Match object contains all the information about the search and the result and if there is no match found then None 
will be returned. Let’s see some of the commonly used methods and attributes of the match object.

Getting the string and the regex
math.re attribute returns the regular expression passed and match.string attribute returns the string passed.

Example: Getting the string and the regex of the matched object

print("-------------------------------------------------------------------------------")
s = "Welcome to Good For Goods"

# here x is the match object
res = re.search(r"\bG", s)

print(res.re)
print(res.string)


Getting index of matched object
start() method returns the starting index of the matched substring
end() method returns the ending index of the matched substring
span() method returns a tuple containing the starting and the ending index of the matched substring
Example: Getting index of matched object 

print("------------------------------------------------------------")
s = "Welcome to Getting index of matched object "

# here x is the match object
res = re.search(r"\bGe", s)

print(res.start())
print(res.end())
print(res.span())

Getting matched substring
group() method returns the part of the string for which the patterns match. See the below example for a better 
understanding.
Example: Getting matched substring 

print("----------------------------------------------------------------------------------")
s = "Welcome to Getting matched"

# here x is the match object
res = re.search(r"\D{2} t", s)

print(res.group())

'''


"""
RegEx Functions

Function	Description
findall	    Returns a list containing all matches
search	    Returns a Match object if there is a match anywhere in the string
split	    Returns a list where the string has been split at each match

sub	Replaces one or many matches with a string



The Match object has properties and methods used to retrieve information about the search, and the result:

.span() returns a tuple containing the start-, and end positions of the match.
.string returns the string passed into the function
.group() returns the part of the string where there was a match
"""
"""
import re

txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)




import re

txt = "The rain in Spain"
x = re.findall("Portugal", txt)
print(x)



import re

txt = "The rain in Spain"
x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start())


import re

txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)


import re

txt = "The rain in Spain"
x = re.split("\s", txt, 1)
print(x)



import re

txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)



import re

txt = "The rain in Spain"
x = re.sub("\s", "9", txt, 2)
print(x)

import re

txt = "The rain in Spain"
x = re.search("ai", txt)
print(x) #this will print an object


import re
m = re.search('(?<=ab)cdef', 'abcdef')
print("simple pattern " ,m.group(0))  #cdef

m = re.search('(?<=ab)\w+', 'abcdef')
print(" pattern matching ", m.group(0))

m = re.search(r'(?<=-)\w+', 'spam-abc')
print(m.group(0))

m = re.search(r'(?<=-)\w+', 'spam-egg')
print(m.group(0))




import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
#print("print", x)   #<re.Match object; span=(0, 17), match='The rain in Spain'>

"""

import re

s = 'A computer science portal for geeks'

match = re.search('science', s)

print('Start Index:', match.start())    #Start Index: 11
print('End Index:', match.end())  #End Index: 18


#The above code gives the starting index and the ending index of the string portal.

import re
s = 'rinky.kumari'
match = re.search(r'.', s)
print("without Backslash " ,match)   #<re.Match object; span=(0, 1), match='r'>

match = re.search(r'\.', s)
print("with Backslash", match)   #<re.Match object; span=(5, 6), match='.'>

"""
re.findall()
Return all non-overlapping matches of pattern in string, as a list of strings. 
The string is scanned left-to-right, and matches are returned in the order found.

"""

#Example: Finding all occurrences of a pattern


import re

# A sample text string where regular expression
# is searched.
string = """Hello my Number is 123456789 and
            my45478822 friend's number is 987654321"""

# A sample regular expression to find digits.
regex = '\d+'  # printing decimal no.

match = re.findall(regex, string)   #['123456789', '45478822', '987654321']
print(match)

import re

# A sample text string where regular expression
# is searched.
string = """Hello my Number is 123456789 and
            my friend's number is 987654321"""

# A sample regular expression to find digits.
regex = '\w+'

match = re.findall(regex, string)
print(match)   #['Hello', 'my', 'Number', 'is', '123456789', 'and', 'my', 'friend', 's', 'number', 'is', '987654321']



"""
re.compile() 
============
Regular expressions are compiled into pattern objects, which have methods for various 
operations such as searching for pattern matches or performing string substitutions. 
"""


import re
strg= """Grab Holdings Inc., commonly known as Grab, is a +91 8596588542 Southeast Asian technology company
     headquartered in Singapore and Indonesia. In addition to transportation, the company offers
        food delivery and digital payments services via a mobileeeeeeeeeee mobile"""

pttr = re.compile(r'Grab')
print("after matching " , pttr.findall(strg))

pttr = re.compile(r'.es')
print("after matching 1 " , pttr.finditer(strg))
matches = pttr.finditer(strg)
for match in matches:
    print("using finditer method: ", match)

#pttr = re.compile(r'.')
#print("after matching 1 " , pttr.findall(strg))

pttr = re.compile(r'co+')
print("after matching 2 " , pttr.findall(strg)) #['co', 'co', 'co']


pttr = re.compile(r'co*')
print("after matching 2 " , pttr.findall(strg)) # ['c', 'co', 'c', 'co', 'co', 'c']


pttr = re.compile(r'^Grab')
print("after matching 2 " , pttr.findall(strg)) #['Grab']

pttr = re.compile(r'ile$')
print("after matching 3 " , pttr.findall(strg)) #after matching 3  ['ile']

pttr = re.compile(r'ile{2}')
print("after matching 4 " , pttr.findall(strg))   #after matching 4  ['ilee']



pttr = re.compile(r'ile{1}|Grab')
print("after matching 5 " , pttr.findall(strg))  # ['Grab', 'Grab', 'ile', 'ile']


pttr = re.compile(r'\AGrab')
print("after matching 6 " , pttr.findall(strg)) #['Grab']

pttr = re.compile(r'\bGrab')
print("after matching 6 " , pttr.findall(strg)) #['Grab', 'Grab']


pttr = re.compile(r'Grab\b')
print("after matching 6 " , pttr.findall(strg)) #['Grab', 'Grab']


pttr = re.compile(r'\BGrab')
print("after matching 6 " , pttr.findall(strg))

patt=re.compile(r'.+91 \d{10}')
matches=patt.finditer(strg)
for match in matches:
    print("matching ....." ,match)

p = re.compile('[a-e]')
print(p.findall("Aye, said Mr. Gibenson Stark"))  #  ['e', 'a', 'd', 'b', 'e', 'a']



# \d is equivalent to [0-9].
p = re.compile('\d')
print(p.findall("I went to him at 11 A.M. on 4th July 1886"))  #['1', '1', '4', '1', '8', '8', '6']

# \d+ will match a group on [0-9], group
# of one or greater size
p = re.compile('\d+')  #
print(p.findall("I went to him at 11 A.M. on 4th July 1886"))  #['11', '4', '1886']

"""
\w , \w+  , \W
"""

# \w is equivalent to [a-zA-Z0-9_].
p = re.compile('\w')
print(p.findall("He said * in some_lang."))
#['H', 'e', 's', 'a', 'i', 'd', '_', 'i', 'n', 's', 'o', 'm', 'e', '_', 'l', 'a', 'n', 'g']
# \w+ matches to group of alphanumeric character.
p = re.compile('\w+')
print(p.findall("I went to him at 11 A.M., he \
said *** in some_language."))
#['I', 'went', 'to', 'him', 'at', '11', 'A', 'M', 'he', 'said', 'in', 'some_language']

# \W matches to non alphanumeric characters.
p = re.compile('\W')
print(p.findall("he said *** in some_language."))
#[' ', ' ', '*', '*', '*', ' ', ' ', '.']


# '*' replaces the no. of occurrence
# of a character.
p = re.compile('ab*')
print(p.findall("ababbaabbbcccbbbabbbaaab"))

#['ab', 'abb', 'a', 'abbb', 'abbb', 'a', 'a', 'ab']



"""
re.split() 
Split string by the occurrences of a character or a pattern, upon finding that pattern, 
the remaining characters from the string are returned as part of the resulting list. 

Syntax : 

re.split(pattern, string, maxsplit=0, flags=0)

"""

from re import split

# '\W+' denotes Non-Alphanumeric Characters
# or group of characters Upon finding ','
# or whitespace ' ', the split(), splits the
# string from that point
print(split('\W+', 'Words, words , Words'))   #['Words', 'words', 'Words']
print(split('\W+', "Word's words Words"))  #['Word', 's', 'words', 'Words']

# Here ':', ' ' ,',' are not AlphaNumeric thus,
# the point where splitting occurs
print(split('\W+', 'On 12th Jan 2016, at 11:02 AM')) #['On', '12th', 'Jan', '2016', 'at', '11', '02', 'AM']

# '\d+' denotes Numeric Characters or group of
# characters Splitting occurs at '12', '2016',
# '11', '02' only
print(split('\d+', 'On 12th Jan 2016, at 11:02 AM')) #['On ', 'th Jan ', ', at ', ':', ' AM']

import re

# Splitting will occurs only once, at
# '12', returned list will have length 2
print(re.split('\d+', 'On 12th Jan 2016, at 11:02 AM', 1))

# 'Boy' and 'boy' will be treated same when
# flags = re.IGNORECASE
print(re.split('[a-f]+', 'Aey, Boy oh boy, come here', flags=re.IGNORECASE))
print(re.split('[a-f]+', 'Aey, Boy oh boy, come here'))





"""
re.sub() 
The ‘sub’ in the function stands for SubString, a certain regular expression pattern is searched 
in the given string(3rd parameter), and upon finding the substring pattern is replaced by
 repl(2nd parameter), count checks and maintains the number of times this occurs. 
 re.sub(pattern, repl, string, count=0, flags=0)
"""


import re

# Regular Expression pattern 'ub' matches the
# string at "Subject" and "Uber". As the CASE
# has been ignored, using Flag, 'ub' should
# match twice with the string Upon matching,
# 'ub' is replaced by '~*' in "Subject", and
# in "Uber", 'Ub' is replaced.
print(re.sub('ub', '~*', 'Subject has Uber booked already',
			flags=re.IGNORECASE))

# Consider the Case Sensitivity, 'Ub' in
# "Uber", will not be reaplced.
print(re.sub('ub', '~*', 'Subject has Uber booked already'))

# As count has been given value 1, the maximum
# times replacement occurs is 1
print(re.sub('ub', '~*', 'Subject has Uber booked already',
			count=1, flags=re.IGNORECASE))

# 'r' before the pattern denotes RE, \s is for
# start and end of a String.
print(re.sub(r'\sAND\s', ' & ', 'Baked Beans And Spam',
			flags=re.IGNORECASE))


