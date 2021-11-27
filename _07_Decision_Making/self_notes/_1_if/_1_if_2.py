''''
Arithmetic ops: +-*/ // %       ==> 0 / nonzero
Relational ops: > >= < <= == != ==> True/False
Assignment ops:                     x = 10  x = -10.4
                                    x = 0   x = None
Logical  ops   :                ==> True/False
Bitwise       :                 ==> 0 or 1   False/True
Membership    : in not in       ==> True/False
Identity      : is is not       ==> True/False
'''

print("Arithmetic operator")
if 10+20>20:
     print("if st executed")


print("Relational operator")

if 10+20==30:
    print("if statement execute")

if 10+2>=30:
    print("if statement execute")


if 10+20<=30:
    print("if statement execute")



print("Assignment operator")


x=10
if x >100 :
    print("if statement execute")



print("Logical operator")

if True and False:
    print("done")


if True and True:
    print("Done")


if True or False:
    print("done")

if False and False:
    print("!!!!!!!!")




if False and True:
    print("!!!!!!!!")