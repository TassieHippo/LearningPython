# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 19:36:28 2021

@author: Dhaniel Lukman

Purpose: Compound boolean
"""

count = int(input('Enter an INT number '))  # Input always return as string! need to change it to int

"First Practice"
# Checking if in between 0 and 20 inclusively
check_1 = count >= 0 and count <= 20
# check_1 = 0 <= count <= 20                  # Alternative way
print('Check 1 results = ',check_1)

"Second Practice"
# Checking if in between 0 and 20 inclusively
check_2 = count < 0 and count > 20
# check_2 = not (0 <= count <= 20)            # Alternative way
print('Check 2 results = ',check_2)

"Third Practice"
# Enter the length of triangle sides
s1 = 3
s2 = 1
s3 = 3
check_triangle = (s1+s2 > s3 and s1+s3 > s2 and s2+s3 > s1) and (s1 >0 and s2 >0 and s3 >0 )
print('Check Triangle results = ',check_triangle)

triangle_equilateral = s1 == s2 == s3               # Same all sides
print('Is the triangle equilateral = ',triangle_equilateral)

triangle_isosceles = s1 == s2 or s2 == s3 or s1 == s3       # Same two sides
print('Is the triangle isosceles = ',triangle_isosceles)

triangle_scalene = s1 != s2 and s2 != s3 and s1 != s3         # None of the sides are the same
print('Is the triangle scalene = ',triangle_scalene)

if s1 != s2:
    if s1 != s3:
        print('All different')
    else:
        print('s1 and s3 is the same')
else:
    print('s1 and s2 is the same')

ts_1 = s1-s2 ==0 or s1-s3==0 or s2-s3 == 0
print('Is the triangle scalene v3 = ',triangle_scalene)

ts_1 = not (s1 == s2 or s2 == s3 or s1 == s3 )
print('Is the triangle scalene v4 = ',triangle_scalene)