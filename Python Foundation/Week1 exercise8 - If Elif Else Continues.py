# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 13:07:58 2021

@author: Dhaniel Lukman

If Elif Else continues
"""

import random as r

random_number = r.randint(1, 10)

user_number = int(input('Guess a number between 1 and 10: '))

print('You guesed: ', user_number)
print('The random number is: ', random_number)

if user_number == random_number:
    print('Well done - you guessed it!')
else:
    if user_number > random_number:
        print('Too high!')
    else:
        print('Too low!')



