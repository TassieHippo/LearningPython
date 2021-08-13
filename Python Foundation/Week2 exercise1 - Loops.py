# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 17:31:07 2021

@author: Dhaniel Lukman

Learning Loops
"""

for i in range(1,11):
    print(i)


x = 1
while x <= 10:
    print(x)
    x += 1


import random as r

while  20 <= r.randint(16, 35) <= 30:
    print('The Weather is Fine')


    
week_days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
for i in week_days:
    print(i)
    
