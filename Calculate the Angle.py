#A program that reads the values of a1, a2, b1, b2 and calculates the cos(th) and the angle 'th' in degrees. The program shows the values of cos(th) and angle 'th'. No need to check the inputs, consider that they are all numerals and !=0.
#also in display there is an image of the vectors and axes

import math

a1= float(input('a1= '))
a2= float(input('a2= '))
b1= float(input('b1= '))
b2= float(input('b2= '))
ab= a1*b1+a2*b2
_a_= math.sqrt(a1**2+a2**2)
_b_= math.sqrt(b1**2+b2**2)
costh= ab/(_a_*_b_)
goniath=90-(math.degrees(math.atan(a2/a1))+math.degrees(math.atan(b2/b1)))
print(costh, goniath, sep=' ')            
