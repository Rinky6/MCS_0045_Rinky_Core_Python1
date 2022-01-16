"""

Task
ABC is a right triangle, 90o at B.
Therefore, angle ABC = 90o.
Point M is the midpoint of hypotenuse AC.

You are given the lengths AB and BC.
Your task is to find angle MBC in degrees.

Input Format
The first line contains the length of side AB.
The second line contains the length of side BC.

Constraints
0 < AB <= 100
0 < BC <= 100
Lengths AB and BC are natural numbers.
Output Format
Output angle MBC in degrees.

Note: Round the angle to the nearest integer.

Examples:
If angle is 56.5000001°, then output 57°.
If angle is 56.5000000°, then output 57°.
If angle is 56.4999999°, then output 56°.

Sample Input

10
10
Sample Output

45°

"""

"""
/_ABC = 90°
BM = 1/2AC = 1/2(AM + MC)
BM = 1/2(MC+MC) = 1/2(2MC) = MC
MBC = Isosceles trangle
MB = BC = CM

We have length of AB AND BC
SO tan = ab/bc
thita = tan`-(ab/bc)



"""

import math
ab=int(input("Enter length of AB : "))
bc=int(input("Enter length of BC : "))
print(str(int(round(math.degrees(math.atan2(ab,bc)))) ) + "°")

"""
The mmath.degrees() method converts an angle from radians to degrees.

Tip: PI (3.14..) radians are equal to 180 degrees, which means that 1 radian is equal
 to 57.2957795 degrees.

Tip: See also math.radians() to convert a degree value into radians.


The math.atan2() method returns the arc tangent of y/x, in radians. Where x and y are 
the coordinates of a point (x,y).

The returned value is between PI and -PI.



"""







"""
import math

ab=int(input("Enter length of AB"))
bc=int(input("Enter length of BC"))

ca=math.hypot(ab,bc)
mc=ca/2
print(mc)
bca=math.asin(1*ab/ca)
bm=math.sqrt((bc**2+mc**2)-(2*bc*mc*math.cos(bca)))
print(bm)
mbc=math.asin(math.sin(bca)*mc/bm)
print(mbc)
print(int(round(math.degrees(mbc),0)),'\u00B0',sep='')


"""