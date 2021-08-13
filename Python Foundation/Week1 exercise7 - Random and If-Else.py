# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 12:50:29 2021

@author: Dhaniel Lukman

Random and If-Else
"""

import random as r
comp_guess = r.randint(1, 10)

user_guess = int(input('Guess a number (1 - 10): '))

print('You Guessed: ', user_guess)
print('The random number is: ', comp_guess)

if user_guess == comp_guess:
    print ('Well done - you guessed it!')
else:
    print('Too bad - better luck next time!')

