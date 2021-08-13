# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 20:29:31 2021

@author: Dhaniel Lukman

Learning If and else
"""

# Program A
a = 2
b = 1

if a < b:
    print ('a is larger than b')
else:
    print ('b is larger than a')
    b -= a
    a += 1

print ('a=', a, 'b=', b)


# Program B
if a + b > 3:
    if b < 5:
        print(b)
    elif a > 2:
        print(a)
    else: 
        print(a + b)
else:
    print (a - b)
print(a, b)