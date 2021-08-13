# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 20:37:40 2021

@author: Dhaniel Lukman

Random Number Generation
"""

import random as r

random_number = r.randint(1, 10)

user_input = int(input ('Guess a number between 1 and 10 '))

print ('You guessed:', user_input)
print ('The random number is:', random_number)